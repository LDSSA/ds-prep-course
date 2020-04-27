import datetime, random

def get_timestamp():
    return datetime.datetime.now().isoformat('|', 'seconds')


def get_random_number(start: int, stop: int):
    return random.randint(start, stop)
