import calendar


def print_calendar(year):
    print(calendar.calendar(year))


y = int(input("Enter the Year: "))
print_calendar(y)
