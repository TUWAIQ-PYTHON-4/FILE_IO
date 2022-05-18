
while True:
    print("do you want to add a new To-Do item?[y>>yes,n>>no,exit]")
    f_qus=input()
    if f_qus == "y":
         print("What is your items to inside to the file?")
         list=[]
         n = int(input("Enter number of elements : "))
         for aa in range(0,n):
             ele = int(input())
             list.append(ele)
             print(list)
             with open('to_do.txt', 'w') as f:
                 for item in list:
                     f.write("%s\n" % item)
    elif f_qus == "n":
        print(": do you want to list your To-Do items ?[y>>yes,n>>no,exit]")
        second_qus=input()
        if second_qus=="y":
             a_file = open("to_do.txt")
             lines = a_file.readlines()
             for line in lines:
                 print(line)
        elif second_qus=="exit":
            break
    elif f_qus =="exit":
        break
print("thank you for using the To-Do program, come back again soon")
