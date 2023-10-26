count = 0
leap_year = 2023

while count != 20:
    if (leap_year % 4 == 0 and leap_year % 100 != 0) or (leap_year % 400 == 0):
        print(leap_year)
        count += 1
    leap_year += 1
