# file I/O
# To-Do List

print(" ")
# inform the user about how to exit the program
print("Note: to exit the program please type \"exit\"")

# Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
user_answer= input("Do you want to add a new To-Do item? (answer by \"y\" for yes and \"n\" for no) ")


# If the user answers yes , then ask the user to type in his new To-Do item.
# Then save that To-Do item inside the a file to_do.txt on a new line.
while user_answer!= "exit":
    if user_answer == 'y':
        to_do_item= input("Please type in your new To-Do item: ")
        file= open("to_do.txt", "a", encoding="utf-8") 
        file.write("{}\n".format(to_do_item))
        file.close()
        user_answer= input("Do you want to add a new To-Do item? (answer by \"y\" for yes and \"n\" for no) ")
     # If the user answers no, then ask the user : 
     # do you want to list your To-Do items ? answer "y" for yes and "n" for no.
    if user_answer == 'n':
        user_answer_listing_item= input("Do you want to list your To-Do items? (answer by \"y\" for yes and \"n\" for no) ")
    # If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.
        if user_answer_listing_item == 'y':
            file= open("to_do.txt", "r", encoding="utf-8")
            content= file.readlines()
            for line in content:
                print(line.strip())
            file.close()
        elif user_answer_listing_item == 'n':
            break
            
        
print("Thank you for using the To-Do program, come back again soon.")


