""" %age>=60 (grade A) 
%age b/w 51 to 60 (grade B)
%age b/w 41 to 50 (grade C) 
%age b/w 31 to 40 (grade D) 
otherwise FAIL. 
Write a program to input the marks of five subjects by the user and calculate total marks of five subjects, and assign 
grades accordingly """

eng = int(input("English marks : "))
hindi = int(input("Hindi marks : "))
sci = int(input("Science marks : "))
maths = int(input("Mathematics marks : "))
sst = int(input("Social Science marks : "))
t_marks = eng + hindi + sci + maths + sst
p = t_marks/5

if p >= 60:
    print("A")
elif (p >= 51) and (p < 60):
    print("B")
elif (p >= 41) and (p <= 50):
    print("C")
elif (p >= 31) and (p <= 40):
    print("D")
else:
    print("Fail")

