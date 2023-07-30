import datetime

HOLIDAY_LIST = [
    {
        "name": "new year",
        "start": {"day": 1, "month": 1},
        "end": {"day": 6, "month": 1},
    },
    # add other holidays as needed
]


class MailsToSanta:
    @staticmethod
    def calculated_time_to_process(time_of_arrival: datetime.datetime) -> datetime.datetime:
        business_start_hour = 8
        business_end_hour = 16

        def is_holiday(dt):
            for holiday in HOLIDAY_LIST:
                start = datetime.datetime(dt.year, holiday["start"]["month"], holiday["start"]["day"])
                end = datetime.datetime(dt.year, holiday["end"]["month"], holiday["end"]["day"])
                if start.date() <= dt.date() <= end.date():
                    return True, end
            return False, None

        while True:
            isholiday, holiday_end = is_holiday(time_of_arrival)
            if isholiday:
                time_of_arrival = holiday_end + datetime.timedelta(days=1)
                time_of_arrival = time_of_arrival.replace(hour=business_start_hour, minute=0)
            elif time_of_arrival.weekday() > 4:  # If it's weekend
                time_of_arrival += datetime.timedelta(days=7 - time_of_arrival.weekday())
                time_of_arrival = time_of_arrival.replace(hour=business_start_hour, minute=0)
            elif time_of_arrival.hour < business_start_hour:
                time_of_arrival = time_of_arrival.replace(hour=business_start_hour, minute=0)
            elif time_of_arrival.hour >= business_end_hour:
                time_of_arrival += datetime.timedelta(days=1)
                time_of_arrival = time_of_arrival.replace(hour=business_start_hour, minute=0)
            else:
                return time_of_arrival
