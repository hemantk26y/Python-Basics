# Program to print A with  asterisks

for row in range(6):
    for col in range(5):
        if ((col == 0 or col == 4) and row >= 3) or (row == 2 and (col == 0 or col == 4)) \
                or (row == 1 and (col == 1 or col == 3)) or (col == 2 and row == 0) or row == 3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
