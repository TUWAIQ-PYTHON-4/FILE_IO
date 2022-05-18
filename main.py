are_you_done = "n"
user_input= input('do you want to add a new To-Do item? answer by "y" for yes and "n" for no \n')

while are_you_done == "n":
    if user_input=='y':

        user_item = input('type in your To-Do item: \n')
        are_you_done = input('Are you done? type "n" for no or type "exit" \n')

        write_file = open('to_do.txt', 'a+', encoding='utf-8')
        write_file.write(user_item + '\n')
        write_file.close()

        if are_you_done == 'exit':
            option = input('do you want to list your To-Do items ? answer "y" for yes or type "exit".\n')
            if option == 'y':
                read_file = open("to_do.txt", "r", encoding="utf-8")
                content = read_file.read()
                print(content)
                read_file.close()
            else:
                exit()

    elif user_input =='n':
        option = input('do you want to list your To-Do items ? answer "y" for yes or type "exit".\n')
        if option == 'y':
            read_file = open("to_do.txt", "r", encoding="utf-8")
            content = read_file.read()
            print(content)
            read_file.close()
        else:
            exit()       