annual_fee = 124500
days_per_week = 5

price_per_day = annual_fee / (52 * days_per_week)

print("The price per day is:", price_per_day)

annual_fee = int(input("Enter the annual fee: "))
days_per_week = int(input("Enter the total days of classes in a week: "))
holidays_per_month = int(input("Enter the number of holidays in a month: "))

total_days_per_year = 52 * days_per_week
total_holidays_per_year = holidays_per_month * 12

price_per_day = annual_fee / (total_days_per_year - total_holidays_per_year)

print("The price per day is:", price_per_day)