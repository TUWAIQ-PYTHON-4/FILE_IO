def To_Do_List():
  answer = input ("do you want to add a new To-Do item? answer by 'y' for yes and 'n' for no. or exit to exit the program ") 
  while answer != "exit":
     if answer == "y":
      answer=input("type in new To-Do item.or exit to exit the program") 
      file = open("to_do.txt", "a+", encoding="utf-8")
      input = file.write()
      file.close()
      To_Do_List() 
     elif answer == "n":
      answer=input("do you want to list your To-Do items ? answer 'y' for yes and 'n' for no.or exit to exit the program"  )   
      if answer == "y":
            print("list of the To-Do:\n" )
            file = open("to_do.txt", "r", encoding="utf-8")
            content = file.read()
            file.close()
            To_Do_List() 
     else:
         To_Do_List()   
To_Do_List()
