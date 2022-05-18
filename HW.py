
'''
## Using what you learned about Python File I/O , we want to make a progeram called To-Do List , this program should do the following:
- Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
- If the user answers yes , then ask the user to type in his new To-Do item . Then save that To-Do item inside the a file to_do.txt on a new line.
- If the user answers no, then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no. 
- If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.
- Then return again to ther first question and ask again, you coninue this untill the user types in "exit" , then you exit the program. and print to the user "thank you for using the To-Do program, come back again soon"
'''

from tkinter.messagebox import YES

print("")
print("WELCOME YOU IN To-Do PROGERAM :)")
print("")


answered=False
while (not answered):
    ask=input("do you want to add a new To-Do item?\n *YES \n *NO \n *EXIT\n")
    if ask.lower()=="yes":
        answer=input("Enter in his new To-Do item:")
        file=open("to_do.txt","a+",encoding="utf-8")
        file.write(answer + "\n")
        file.close()
    elif ask.lower()=="no":
        answer=input("do you want to list your To-Do items:")
        if answer.lower()=="yes":
           file=open("to_do.txt","r",encoding="utf-8")
           for x in file:
               print(x)
    elif ask.lower()=="exit":
        answered=True
        print("thank you for using the To-Do program, come back again soon :)")
        
    




