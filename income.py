import csv
from datetime import datetime
balance=0
transactions= []

while True :
    print("Welcome To Budget Manager")
    print("1.Add Income or Expenses")
    print("2.Views All Entries")
    print("3.Check Balance")
    print("4.Exit")

    user_click=int(input("Choose Any of One :"))


    if user_click==1 :
        print("You chose to add a transaction.")
        new_transactions={}
        print("A.Is it income or expense")
        value1=input("income or expense :")
        new_transactions["type"]=value1
        print("B.How much is it?")
        value2=int(input("cost :"))
        new_transactions["cost"]=value2
        print("C.What is the category? (like food, salary, etc.")
        value3=input("category :")
        new_transactions["category"]=value3
        print("D.Any note? (like from friend, monthly pay)")
        value4=input("notes :")
        new_transactions["notes"]=value4
        transactions.append(new_transactions)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_transactions["datetime"] = now
        with open("transactions.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([now ,value1, value2, value3, value4])
    elif user_click==2:
        num=0
        print("You chose to view all transactions.")
        if transactions == []:
            print("No transactions found")
        else:
            for trans in transactions:
                num+=1
                print("transactions" ,num )
                print("date $ time :" , trans["datetime"])
                print("type :", trans["type"])
                print("cost :", trans["cost"])
                print("category :", trans["category"])
                print("note :", trans["notes"])
    elif user_click==3:
        print("You chose to show balance.") 
        balance=0
        for total in transactions:
            if total["type"]=="income":
                balance+=total["cost"]
            else:
                balance-=total["cost"]
        print( "your current balance :" , balance)
    elif user_click==4:
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


