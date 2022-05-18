
print("-"*80)
print ("Welcom in your personal assistant to To-Do-item list, \nIf you want to exit from file, \nEnter word \'exit\' \n")
print("-"*80)

file = open("To-Do-item.txt", "a", encoding="utf-8")

while True:
       user_ask1= input("Do you want to add a new To Do item? ")

       if user_ask1 == "yes":
          user_ask2= input("What type in his new To-Do item? ")
          file.write(user_ask2 + "\n")
         

       elif user_ask1 == "no":
            file = open("To-Do-item.txt", "r+", encoding="utf-8")
            user_ask3 = input("do you want to list your To-Do items ? ")
          
            if user_ask3 == "yes":
                show_items=file.readlines()
                
                print("-"*80)
                print(show_items)
                print("-"*80)
       
       elif user_ask1 or user_ask3  == "exit":
            file.close()

            print("\n thank you for using the To-Do program, come back again soon")
            break





