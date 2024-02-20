# WAP to calculate days between two dates

from datetime import date

date1 = date(2022, 1, 26)
date2 = date(2022, 2, 26)
d = date2 - date1
print("Number of Days Between", date1, "and", date2, "is -->", d.days)
