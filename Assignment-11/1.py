import pandas as pd
from datetime import datetime

date_time_obj = pd.Timestamp('2012-01-15')
print("Date time object for Jan 15 2012:", date_time_obj)

specific_date_time = pd.Timestamp('2012-01-15 21:20:00')
print("Specific date and time of 9:20 pm:", specific_date_time)

local_date_time = pd.Timestamp.now()
print("Local date and time:", local_date_time)

date_without_time = local_date_time.date()
print("Date without time:", date_without_time)

current_date = pd.Timestamp.today().date()
print("Current date:", current_date)

time_from_datetime = local_date_time.time()
print("Time from a date time:", time_from_datetime)

current_local_time = datetime.now().time()
print("Current local time:", current_local_time)