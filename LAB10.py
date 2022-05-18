# Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
# If the user answers yes , then ask the user to type in his new To-Do item .
# Then save that To-Do item inside the a file to_do.txt on a new line.

exit_from_program = True
while exit_from_program :
    print("Do you want to add a new To-Do item? answer by 'y' for yes and 'n' for no") #input_of_q1
    print("if you want to close the program type 'exit' ")
    input_of_q1 = input()
    if input_of_q1 == "y":
        to_do_item = input()
        file_writing = open('file to_do.txt', "a+", encoding="utf-8")
        file_writing.write("\n"+to_do_item)
        file_writing.close()
        exit_from_program =False # to exit from program

 # If the user answers no, then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no.   
    elif input_of_q1 == "n":
        print("Do you want to list your To-Do items? answer by 'y' for yes and 'n' for no") #input_of_q2
        input_of_q2 = input()

    # If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.
        if input_of_q2 == 'y':
            file_reading = open('file to_do.txt', "r")
            for items in file_reading.readlines():
                print(items)
            file_reading.close()
    # if the user ansswer exit, then exit the program
    elif(input_of_q1 or input_of_q2 =="exit"):
        print("thank you for using the To-Do program, come back again soon")
        exit_from_program = False
