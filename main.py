

from asyncore import write
from fileinput import close


check = True
while check :
    answer = input("do you want to add a new To-Do item?\nAnswer by \"Y\" for Yes and \"N\" for No or \"Exit\" to out: ")
    answer_lower = answer.lower()
    
    if answer_lower == "y":
        to_do_list_file = open("to_do.txt" ,"a" , encoding="utf-8")
        to_do_list_file.write("- "+input("Type your To-Do list item:")+"\n")
        to_do_list_file.close()

    elif answer_lower == "n":
        answer_2 = input("Do you want to list your To-Do items ?\nAnswer by \"Y\" for Yes and \"N\" for No or \"Exit\" to out: ")
        answer_lower_2 = answer_2.lower()
        if answer_lower_2 == "y":
            to_do_list_file = open("to_do.txt" ,"r" , encoding="utf-8")
            print(to_do_list_file.read())
            to_do_list_file.close()
        elif answer_lower_2 == "n":
            continue
        else:
            print("Answer by \"Y\" for Yes and \"N\" for No or \"Exit\" to out: ")
            break
        
    elif answer_lower == "exit":
        check = False
    else:
        print("Answer by \"Y\" for Yes and \"N\" for No or \"Exit\" to out: ")
        continue