import pandas as pd


def parse_dates(start_date, end_date=None):
    if pd.isnull(end_date):
        return f"{start_date}"
    else:
        return f"{start_date} -- {end_date}"
