
def to_do_list():
    file = open('To-Do.txt','w',encoding="utf-8")
    print ("\n welcom in your To-Do list ! \nIf you want to exit, type ""exit")
    print("_________________________________")


    while True:
        ask_user=input(" - Do you want to add a new To-Do item?\t")
        if ask_user == 'y':
            ask_user_type = input(" - Please what you want in your list :\t")
            file.write(ask_user_type + '\n')

        
            #save
        elif ask_user == 'n':
            
            file= open('To-Do.txt','r+')
            ask_user_want = input("- Do you want to list your To-Do items ?\t")
            if ask_user_want == 'y':
               print_items_list=file.readlines()
               print("you should do :",print_items_list )
              

        elif ask_user == "exit":
            file.close()
            print("\n thank you for using the To-Do program, come back again soon")
            break
to_do_list()
        
         

