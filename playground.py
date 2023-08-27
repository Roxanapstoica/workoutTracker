from datetime import datetime

print(datetime.now())

today = datetime.now()
today_date = today.strftime("%Y-%m-%d")
today_hour = today.strftime("%I:%M:%S %p")
print("Today date is: ",today_date)
print("Today hour is ",today_hour)