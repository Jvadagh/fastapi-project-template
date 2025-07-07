import pytz
from datetime import datetime

from app.core.config import settings

system_timezone = pytz.timezone(settings.TIME_ZONE)


def now_datetime_with_timezone() -> datetime:
    return datetime.now(tz=system_timezone).replace(tzinfo=None)
