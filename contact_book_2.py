contacts = {}

try:
    with open("contacts.txt","r") as file:
         for line in file:
             line = line.strip()
             if not line:
                 continue
             name, phone = line.split("," ,1)
             contacts[name] = phone
except FileNotFoundError:
    pass

def add_contacts():
    name = input("Please enter your name")
    phone = input("please Enter your phone number")
    if name in contacts:
        print("Nmae is already exit")
    else:
        contacts[name] = phone
        with open("contacts.txt","w") as file:
            for name, phone in contacts.items():
                file.write(f'{name},{phone}\n')
        print("your number is successfully saved")
        
def view_contacts():
    print("Your contacts")
    for name, phone in contacts.items():
        print( name, ":", phone)
        
def search_contacts():
    name = input("Please enter any name for search")
    if name in contacts:
        print("Contact found", contacts[name])
    else:
        print("Contact is not founded")
        
def Delete_contacts():
    name = input("please enter any name for deletion")
    if name in contacts:
        del contacts[name]
        with open("contacts.txt","w") as file:
            for name , phone in contacts.items():
                file.write(f'{name},{phone}\n')
            print("contact is successfully deleted")
    else:
        print("contact is not found")
        
def Exit_contacts():
    print("Have a Good Day!")
    
    
def main():
    while True:
            print("====== contacts Book ======")
            print( "1. Add contact ")
            print("2. view contacts ")
            print("3. search ")
            print("4. Delete the contact ")
            print("5. Exit")
            choice = input("please Enter your choice")
            print(choice)
            if choice =="1":
                 add_contacts()
            
            elif choice =='2':
                view_contacts()
                
            elif choice =='3':
                search_contacts()
                
            elif choice =='4':
                Delete_contacts()
                
            elif choice == '5':
                Exit_contacts()
                break
            
            else:
                print("Invalid choice")

main()              