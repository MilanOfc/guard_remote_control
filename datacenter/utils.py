from datetime import datetime, timezone, timedelta


def get_duration(visit):
    entered = visit.entered_at
    if visit.leaved_at:
        return visit.leaved_at - entered
    now = datetime.now().replace(tzinfo=timezone.utc)
    return now - entered


def format_duration(duration):
    seconds = duration.total_seconds()
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f'{int(hours)}ч {int(minutes)}мин'


def is_visit_long(visit, minutes=60):
    return get_duration(visit) > timedelta(minutes=minutes)
