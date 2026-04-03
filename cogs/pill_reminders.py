import discord
from discord.ext import tasks, commands
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# ── configurable schedule ──────────────────────────────────────────
# type: "daily" → every day within the hour window
# type: "recurring" → every interval_days, anchored to a specific date
#
# start_hour / end_hour are in 24h Mountain Time.
# if end_hour < start_hour, the window wraps past midnight.

PILL_SCHEDULE = {
    "vyvanse": {
        "type": "daily",
        "start_hour": 8,
        "end_hour": 19,
    },
    "prog": {
        "type": "daily",
        "start_hour": 22,
        "end_hour": 3,  # wraps past midnight
    },
    "shot": {
        "type": "recurring",
        "interval_days": 6,
        "anchor": "2026-03-31",  # a known shot day
        "start_hour": 8,
        "end_hour": 23,
    },
}

TZ = ZoneInfo("America/Denver")


def _now():
    return datetime.now(TZ)


def _in_window(now, start_hour, end_hour):
    """Check if current hour is within [start_hour, end_hour).
    Handles windows that wrap past midnight (e.g. 22 -> 3)."""
    h = now.hour
    if end_hour > start_hour:
        return start_hour <= h < end_hour
    else:  # wraps past midnight
        return h >= start_hour or h < end_hour


def _is_shot_day(now, anchor_str, interval_days):
    anchor = datetime.strptime(anchor_str, "%Y-%m-%d").date()
    delta = (now.date() - anchor).days
    return delta % interval_days == 0


def _window_date_key(now, start_hour, end_hour):
    """Return a date string that identifies the current window.
    For overnight windows (e.g. 22-3), the hours after midnight
    still belong to the previous day's window."""
    if end_hour <= start_hour and now.hour < end_hour:
        return (now - timedelta(days=1)).strftime("%Y-%m-%d")
    return now.strftime("%Y-%m-%d")


class PillReminders(commands.Cog):

    def __init__(self, client):
        self.client = client
        # in-memory state — resets on restart, which is fine:
        # worst case is one extra reminder after a restart
        self.done = set()          # set of "pill:date" keys
        self.last_remind = {}      # pill_name -> datetime of last reminder
        self.pill_check.start()

    def cog_unload(self):
        self.pill_check.cancel()

    def _done_key(self, pill_name, now, cfg):
        """Unique key per pill per window, e.g. 'vyvanse:2026-04-03'."""
        date_key = _window_date_key(now, cfg["start_hour"], cfg["end_hour"])
        return f"{pill_name}:{date_key}"

    @tasks.loop(minutes=5)
    async def pill_check(self):
        now = _now()
        user = await self.client.fetch_user(self.client.special_one)

        for pill_name, cfg in PILL_SCHEDULE.items():
            if not _in_window(now, cfg["start_hour"], cfg["end_hour"]):
                continue

            if cfg["type"] == "recurring":
                if not _is_shot_day(now, cfg["anchor"], cfg["interval_days"]):
                    continue

            # already acknowledged this window?
            if self._done_key(pill_name, now, cfg) in self.done:
                continue

            # throttle: at most one DM per hour per pill
            last = self.last_remind.get(pill_name)
            if last and (now - last).total_seconds() < 60:
                continue

            # send reminder
            try:
                await user.send(f"you need to take {pill_name}")
                self.last_remind[pill_name] = now
            except Exception:
                pass

    @pill_check.before_loop
    async def before_pill_check(self):
        await self.client.wait_until_ready()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id != self.client.special_one:
            return
        if not isinstance(message.channel, discord.DMChannel):
            return
        if message.content.strip().lower() != "done":
            return

        now = _now()
        acknowledged = []

        for pill_name, cfg in PILL_SCHEDULE.items():
            if not _in_window(now, cfg["start_hour"], cfg["end_hour"]):
                continue
            if cfg["type"] == "recurring":
                if not _is_shot_day(now, cfg["anchor"], cfg["interval_days"]):
                    continue

            done_key = self._done_key(pill_name, now, cfg)
            if done_key not in self.done:
                self.done.add(done_key)
                acknowledged.append(pill_name)

        if acknowledged:
            pill_list = ", ".join(acknowledged)
            await message.channel.send(f"marked as done: {pill_list}")


def setup(client):
    client.add_cog(PillReminders(client))
