contacts = {}

                      
                                  
try:
    with open("contacts.txt", "r") as file:
     for line in file:
      name,phone = line.strip().split(",")
      contacts[name] = phone
except FileNotFoundError:
                pass
            
def main():          
    while True:
            
            
            print("====== contacts Book ======")
            print( "1. Add contact")
            print("2. view contacts")
            print("3. search")
            print("4. Delete the contact")
            print("5. Exit")

            choice = input("Enter your chooice : ")
            print(choice)

            if choice == "1":
                name = input("please enter your name : ")
                phone = input("please enter your phone number : ")
                if name in contacts:
                    print("Name is already exits")
                else:    
                    contacts[name] = phone
                    with open("contacts.txt","w") as file:
                       for name, phone in contacts.items():
                        file.write(f"{name}, {phone} \n")
                    print("your number is saved.")

            elif choice == "2":
                print("your contacts")
                for name, phone in contacts.items():
                        print(name, ": ", phone)


            elif choice == '3':
                name = input("Enter any name for search : ")
                if name in contacts:
                    print("contact found", contacts[name])
                else:
                    print("contact not founded")
                
            elif choice == "4":
                name = input("Enter the name for delete : ")
                if name  in contacts:
                    del contacts[name]
                    with open("contacts.txt","w") as file:
                        for name, phone in contacts.items():
                            file.write(f"{name} : {phone} \n")
                    print("Name has been successfully deleted")
                else:
                    print("contact is not found")
                    
                
            elif choice == "5":
                print("Good Bye !")
                break


            else:
                print("invalid choice sweet Heart :) ")
            
main()