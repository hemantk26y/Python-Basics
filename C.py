# Program to print C with  asterisks

for row in range(6):
    for col in range(6):
        if (col == 0 and (0 < row < 5)) or (row == 0 and (0 < col < 5)) or (row == 5 and (0 < col < 5)) \
                or (col == 5 and (row == 1 or row == 4)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
