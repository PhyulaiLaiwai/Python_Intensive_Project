# ==============================
# 📚 Python Intensive Course
# ==============================

# ==============================
# 🧩 Project 1: Personal Budget Tracker
# ==============================


# ****************************************
# start you code her ..........💪
import csv
import os

FILE_Name="budget_dat.csv"
CATEGORIES =["Food","Transport","Rent","Utilities","Entertainment","Other","Work"]
#creating csv file
def initialize_csv():
    if not os.path.isfile(FILE_Name):
        with open(FILE_Name,mode='w',newline='')as file:
            writer= csv.writer(file)
            writer.writerow(["Category","Amount","Type"])
initialize_csv()



def get_transaction(trans_type):
     print(f"\n--Add{trans_type}--")
     print(f"Avaliable Category: {','.join(CATEGORIES)}")

    #Category validation 
     while True:
       category = input("Enter category :").strip().capitalize()
       if category in CATEGORIES:
            break
       else: 
           print(f"Invalid category ! Please choose from the list{','.join(CATEGORIES)}")

     #AMOUNT VALADATION
     while True:
         try:
             amount=float( input("Enter Amount:  "))
             if amount <= 0:
                 print("Amount must be positive number")
                 continue
             break
         except ValueError:
             print("Invalid input .Please  enter numeric for amount")
     return category,amount,trans_type
def save_trans(category,amount,trans_type):
    with open (FILE_Name,mode="a",newline='')as file:
        writer= csv.writer(file)
        writer.writerow([category,amount,trans_type])
    print("✅Transition save successfully!")

def calculat_bal():
    if not os.path.exists(FILE_Name):
        return 0.0,0.0,0.0
    else:
        income= 0.0
        expense=0.0
        with open (FILE_Name,mode="r")as file:
           reader=  csv.DictReader(file)
           for row in reader:
               #data conversion with error handling
               try:
                   amount=float( row["Amount"])
                   if row["Type"] == "Income":
                        income += amount
                   else:  expense += amount
               except ValueError:
                   continue
    return income,expense,income-expense
def display_report():
    print("\n" +"="*30)
    print("       Budget Report")
    print("="*30)
    income,expense,balance= calculat_bal()
    print(f"Total Income:  💲{income:>10.2f}")
    print(f"Total Expense: 💲{expense:>10.2f}")
    print("_"*30)
    print(f"Current Balance: 💲{balance:>10.2f}")


def main():
    initialize_csv()
    menu ={
        "1": ("Add Income","Income"),
        "2":("Add Expense","Expense"),
        "3":("View Report",None),
        "4":("Exit",None)
    }
    #menu = (1,(Add income,income))
    while True:
        print("\n --------Personal Budget Trucker--------")
        for k,v in menu.items():
            print (f"{k} {v[0]}")
        choice = input("Select an option (1-4) :").strip()
        if choice in ['1','2']:
            data = get_transaction(menu[choice][1])
            save_trans(*data)
        elif choice == '3':
                display_report()
        elif choice== '4':
             print("Good Bye !💗")
             break
        else:
                print("Invalid choice !")
if __name__ =="__main__":
    main()


                
            


                

            




