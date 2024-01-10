from datetime import datetime



def valid_start_date(start_date, format="%Y-%m-%d"):
    try:
        start_datetime = datetime.strptime(start_date, format)
        if datetime.now().date() > start_datetime.date():
            return False

        return True
    except ValueError:
        return False


def valid_end_date(start_date, end_date, format="%Y-%m-%d"):
    try:
        start_datetime = datetime.strptime(start_date, format)
        end_datetime = datetime.strptime(end_date, format)
        if start_datetime.date() >= end_datetime.date():
            return False

        return True
    except ValueError:
        return False

