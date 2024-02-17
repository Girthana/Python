"""
Program:Display number of days interms of years, weeks and days
Input: Number of days
"""
Num_days=int(input("Enter number of days:"))
Num_years=int(Num_days/365)
print("Number of years :", Num_years)
Num_weeks = int((Num_days%365)/7)
print("Number of weeks :", Num_weeks)
days=int((Num_days%365)%7)
print("Number of days :", days)