def is_leap(year):
    if year%4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    else:
        return False
    
        
def days_in_months(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year): 
       print("Leap year")
       month_days[1] = 29
       print(f"{month_days[1]}")
    else:
        print("Not leap year")
        print(f" { month_days[1]}")

days_in_months(2001, 2)
