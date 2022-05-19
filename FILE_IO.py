exit_u='exit'
exit_p=True            

ask1=input("do you want to add a new To-Do item")
while exit_u:
    if ask1 =='y':
        ans_u=input("what type? ")
        file=open("to_do.txt","a",encoding="utf-8")
        file.write(f'{ans_u}\n')
        file.close()

    elif ask1 =='n':
        v_l=input("Do you want to viwe your To-Do list")
        if v_l =='y':
            file_read=open("to_do_txt")
            t_d_l=file_read.readline()
            for i in t_d_l:
                print(i)

        elif ask1 == exit_u:
            exit_p=False            
