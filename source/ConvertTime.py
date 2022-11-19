from datetime import datetime


def convert(date):
    cat = datetime.strptime(date, "%a %b %d %H:%M:%S %z %Y")
    return cat.strftime("%Y-%m-%d %H:%M:%S")
