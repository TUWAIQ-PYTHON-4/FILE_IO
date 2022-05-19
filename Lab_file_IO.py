# FILE_IO


## Using what you learned about Python File I/O , 
# we want to make a progeram called To-Do List , 
# this program should do the following:
#- Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
#- If the user answers yes , then ask the user to type in his new To-Do item . Then save that To-Do item inside the a file to_do.txt on a new line.
#- If the user answers no, then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no. 
#- If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.
#- Then return again to ther first question and ask again, you coninue this untill the user types in "exit" , then you exit the program. 
# and print to the user "thank you for using the To-Do program, come back again soon"

# User Input - bool 


to_do_item = input('Do you want to add a new 2Do item? (y/n) - type (exit) to end ')

while to_do_item != 'exit':
    if to_do_item == 'y':
        # write in a new line 
        item = input('Write your new 2Do item.. ')
        to_do = open('to_do.txt', 'a')
        to_do.write('\n%s'  % item)
    elif to_do_item == 'n':
        to_do_list = input('Do you want to list your 2Do items? (y/n) ')
        if to_do_list == 'y':
            # print the list
            with open('to_do.txt', 'r') as to_do:
                for line in to_do:
                    print(line.rstrip())
        elif to_do_list == 'n':
            to_do_item = input('Do you want to add a new 2Do item? (y/n) - type (exit) to end ')
        else:
            print('Wrong entry! try again.. ')
    else:
        print('Wrong entry! try again.. ')

    to_do_item = input('Do you want to add a new 2Do item? (y/n) - type (exit) to end ')
else:
    print('thank you for using the To-Do program, come back again soon')
    to_do.close()
