

exit_user='exit'
exit_program= True

while exit_program:

    ask_user =input('Do you want to add a new To-Do item? answer "y" for yes and "n" for no if you want to end type exit: ')

    '''if ask_user != 'y' or 'n':
        print('Please answer with y or n if you want to end enter exit') '''
    
    if ask_user == 'y':
        user_items= input('Type in your new To-Do item: ')

        file = open('to_do.txt', "a+", encoding="utf-8")
        file.write(f'{user_items}\n')
        file.close()

    elif ask_user == 'n':
        show_list =input('Do you want to view your To-Do list ? answer "y" for yes and "n" for no to end type exit: ')
        if show_list == 'y':
            file_read = open("to_do.txt", "r")
            to_do_list =file_read.readlines()
            for items in to_do_list:
                print(items)

    elif ask_user == exit_user:
        print("Thank you")
        exit_program = False