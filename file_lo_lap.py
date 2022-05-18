answer = []
input_user = []
file = open('to_do.txt', "w", encoding="utf-8")
while answer !='exit' :
    answer = input("do you want to add a new To-Do item?  [y] for yes and [n] for no")
    if answer == 'y':
        input_user = input("what new To-Do item ?") +'\n'
        file.write(input_user)
    elif answer == 'n':
        answer2 = input("do you want to list your To-Do items ? answer [y] for yes and [n] for no")
        if answer2 == 'y':
            file = open('to_do.txt')
            print(file.read())
            file.close()
else:
    print("thank you for using the To-Do program, come back again soon")