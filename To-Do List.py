import sys

def to_do ():
    input_user = input("Do you want to add a new To-Do item? " + " inter y for yes " + " or inter n for no :")

    if input_user == "y" :
        user_input = input("Enter your to do :")
        file = open("C:\\Users\DELL\python4\FILE_IO\\to_do.txt", "a", encoding="utf-8")
        content = file.write(user_input+"\n")
        file.close()
        to_do()

    elif input_user == "n" :
        input_user = input("do you want to list your To-Do items ?" + " inter y for yes " + " or type n for EXIT :")
        if input_user == "y":
            file = open("C:\\Users\DELL\python4\FILE_IO\\to_do.txt", "r", encoding="utf-8")
            content = file.read()
            print(content)
            file.close()
            to_do()
            
        elif input_user == "n": 
            sys.exit(0)

to_do()