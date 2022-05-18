file=open('todo.txt','w',encoding='utf-8')
print("Hello ! you are in ToDo list program please chose y for yes and n for no ,or exit for Exit from program ")

while True:
    user_input = input("do you want to add a new To-Do item? ")
    if user_input == 'y':
        user_input2=input("please type your new to do list ")
        file.write(user_input2+'\n')
    elif user_input=='n':
        file=open('todo.txt','r+')
        user_input3=input("do you want to list your To-Do items ? ")
        if user_input3=='y':
            item_l=file.readlines()
            print(item_l)
    elif user_input=='exit': 
        file.close()
        print("thank you for using the To-Do program, come back again soon ")
        break


        