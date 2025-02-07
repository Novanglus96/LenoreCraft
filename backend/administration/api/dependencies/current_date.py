import pytz
import os
import datetime
from django.utils import timezone


def current_date():
    """
    Gets a timezone adjusted date for todays date.

    Returns:
        (Date): Timezone adjusted date
    """
    today = timezone.now()
    tz_timezone = pytz.timezone(os.environ.get("TIMEZONE"))
    today_tz = today.astimezone(tz_timezone).date()
    return today_tz
