import datetime

day = int(input("Enter a day: "))
month = int(input("Enter a month: "))
year = int(input("Enter a year: "))

lemme_see = datetime.datetime(year, month, day)
print(lemme_see)
