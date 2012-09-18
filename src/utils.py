from datetime import datetime

def parse_datetime(dt):
    return datetime.strptime(dt, '%a %b %d %H:%M:%S +0800 %Y')
