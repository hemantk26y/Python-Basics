# WAP to access of a nested dictionary 

dict_n = {'student1': {'Name': 'Hemant', 'Age': 20, 'Gender': 'Male'},
          'student2': {'Name': 'Himanshu', 'Age': 15, 'Gender': 'Male'}}
for a in dict_n:
    print(a)
    for b in dict_n[a]:
        print(b, ':', dict_n[a][b])
