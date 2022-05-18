
f = open("to_do.txt","a+", encoding="utf-8") 

if f:
    print("To-Do List:")
    while True:
        f = open("to_do.txt", "a+")
        userInput = input("\nDo you want to add a new To-Do item? ").lower()

        
        if userInput == "exit":
            print("\nThank you for using the To-Do program, come back again soon")
            break
        elif userInput == "y":
            item = input("Type the new To-Do item: ")
            
            f.write("\n")
            f.write(item)
            f.close()

        elif userInput == "n":
            c = input("Do you want to list your To-Do items? ").lower()


            if c == "y":
                print("\nFile Contents")
                with open("to_do.txt") as file:
                    for line in file:
                        print(line.strip())


        else:
            print("\nInvalid input ! Please try again ")

else:
    print("Can't open the file")


f.close()