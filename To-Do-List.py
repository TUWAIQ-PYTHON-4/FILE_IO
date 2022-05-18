result=''
print("Welcom to the To-Do program if you end the program Enter exit")
while result!="exit":
    result=input("do you want to add a new To-Do item? -answer by y for yes and n  for no-")
    if result=='y':
        item=input("what type in his new To-Do item?")
        file=open("to_do.txt",'a', encoding="utf-8")
        file.writelines(item+'\n')
    elif result=='n':
        result=input("do you want to list your To-Do items ? answer y for yes and n for no." )
        if result=='y':
            file= open("to_do.txt",'r',encoding="utf-8")
            print(file.read())
else:
    print("thank you for using the To-Do program, come back again soon")



    
