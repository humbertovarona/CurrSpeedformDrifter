def get_DayIndexes(dates, day):
    dates_datetime = [datetime.strptime(date, "%Y-%m-%d %H:%M:%S") for date in dates]
    day_str = str(day)
    try:
        day_datetime = datetime.strptime(day_str, "%Y-%m-%d")
    except ValueError:
        print("The specified day is not a valid date format")
        return None
    Indexes = [i for i, date_datetime in enumerate(dates_datetime) if date_datetime.date() == day_datetime.date()]
    return Indexes
