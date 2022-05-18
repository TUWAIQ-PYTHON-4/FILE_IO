answer = ""
user_input = ""
file = open('to_do.txt', "w", encoding="utf-8")
print("answer with \'y\' as yes , \'n\' or \'exit\' to exit from To-Do program")
while answer != "exit":
    answer = input("do you want to add a new To-Do item? ")
    if answer == "y":
        user_input = input("what new To-Do item ?") +"\n"
        file.write(user_input)
    elif answer == "n":
        answer2 = input("do you want to list your To-Do items ? ")
        if answer2 == "y":
            file = open("to_do.txt")
            print(file.read())
            file.close()
        elif answer2 != "n":
            print("Invalid value please try again")
    elif not "exit":
        print("Invalid value please try again")
print("thank you for using the To-Do program, come back again soon")