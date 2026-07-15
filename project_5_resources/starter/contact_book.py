import csv
import os

class Contact:
    def __init__(self, name, ph, email):
        self.name = name
        self.ph = ph
        self.email = email
        
    def display(self):
        print(f"Name: {self.name}")
        print(f"Phone: {self.ph}")
        print(f"Email: {self.email}")
        print("-" * 20)

class ContactBook:
    def __init__(self, filename="contact.csv"):
        self.contacts = [] # temp contact place list
        self.filename = filename # initialize filename to contactbook
        self.ensure_csv_exist() # is there contactbook.csv ? checking 
 
    def ensure_csv_exist(self):
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='', encoding='utf-8') as file: # check if file exist
                writer = csv.writer(file)
                writer.writerow(["Name", "Phone", "Email"]) # header row creating

    def add_contact(self, name, ph, email):
        new_cont = Contact(name, ph, email)
        self.contacts.append(new_cont) # list[] format append
        self.save_cont_to_csv(new_cont) # save contacts

    def save_cont_to_csv(self, contact):
        try:
            with open(self.filename, mode='a', newline='', encoding='utf-8') as file: # a is append mode
                writer = csv.writer(file)
                writer.writerow([contact.name, contact.ph, contact.email])
            print("Contact saved to csv")
        except Exception as e:
            print(f"Error in Saving contact to CSV: {e}")
    
    def view_contact(self):
        if not self.contacts: # check is there contact or not in contact list[]
            print("\n No contact to display")
        else:
            print("\n All contacts:")
            for i in self.contacts:
                i.display()
    
    def search_contact(self, search_name):
        print(f" \n Searching for: {search_name}")
        found = False
        for contact in self.contacts:
            if contact.name.lower() == search_name.lower():
                contact.display()
                found = True
        
        # FIX: Shifted left outside the loop so it evaluates once after checking all contacts
        if not found:
            print(f"contact not found for: {search_name}")

    def delete_contact(self, delete_name):
        removed = False
        for contact in self.contacts[:]: # need to make shallow copy cuz delete in list can cuz error
            if contact.name.lower() == delete_name.lower():
                self.contacts.remove(contact)
                removed = True
                break # if found the program break
        if removed:
            try:
                with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Name", "Phone", "Email"])
                    for contact in self.contacts:
                        writer.writerow([contact.name, contact.ph, contact.email])
                print(f"{delete_name} is deleted")
            except Exception as e:
                print(f"error in updating contact.csv file {e}")
        else:
            print("contact not found")

    def load_from_csv(self): # FIX: Removed the unused 'file' parameter
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file) # read data from dictionary
                self.contacts.clear() # clear table 
                for row in reader:
                    name = row['Name']
                    phone = row['Phone']
                    email = row['Email']
                    self.contacts.append(Contact(name, phone, email))
            print(f"\n Contacts loaded from {self.filename}")
        except Exception as e:
            print(f"error found in file loading: {e}")


# FIX: Fully unindented the main function loop and runner so they sit at root level
def main():
    book = ContactBook()
    book.load_from_csv()
    print(f"\n Welcome to contact book manager\n")
    while True:
        print("\n1.Add➕\n2. View All Contacts🪟\n3. Search Contact 🔎\n4. Delete Contact🗑️ \n5. Exit Program👋🏻")
        
        # Added a try/except shell so entering an accidental string letter won't crash your menu!
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid format. Please pick a number between 1 and 5.")
            continue
            
        if choice == 1:
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            book.add_contact(name, phone, email)
        elif choice == 2:
            book.view_contact()
        elif choice == 3:
            name = input("Enter name to search: ")
            book.search_contact(name)
        elif choice == 4:
            name = input("Enter name to delete: ")
            book.delete_contact(name)
        elif choice == 5:
            print("Goodbye")
            break
        else:
            print("Invalid entry. Try again.")

if __name__ == "__main__":
    main()