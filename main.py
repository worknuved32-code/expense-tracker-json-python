import json
try:
    with open("expense.json","r") as f:
        expenses = json.load(f)
except:
    expenses = []

def add_expenses(expenses):
    item = input("Enter Expense:")
    price = int(input("Enter price:"))

    expense = {
        "item":item,
        "price":price
    }
    expenses.append(expense)
    with open("expense.json","w") as f:
        json.dump(expenses,f)
    print("Item added successfully")

def view_expenses(expenses):
    for expense in expenses:
        print("Item :",expense["item"])
        print("Price :",expense["price"])
        print("-"*17)

def total_expenses(expenses):
    total=0
    for expense in expenses:
        total=total+expense["price"]
    print("Total expenses :",total)

def highest_expenses(expenses):
    highest_expense = max(expenses,key=lambda x: x["price"])
    print("Highest expenses")
    print("Item :",highest_expense["item"])
    print("Price :",highest_expense["price"])
    print("-"*17)

def delete_expense(expenses):
    name = input("Enter the expense name :")
    flag = False
    for expense in expenses:
        if name == expense["item"]:
            expenses.remove(expense)
            with open("expense.json","w") as f:
                json.dump(expenses,f)
            print("Expense deleted")
            flag=True
            break
    if not flag:
        print("Expense does not exist")


    
while True:
    print("\n1.Add Expenses",
          "\n2.View Expenses"
          "\n3.Total Expenses"
          "\n4.Highest Expenses"
          "\n5.Delete Expenses"
          "\n6.Exit")
    
    choice = int(input("Enter the choice :"))

    if choice == 1:
        add_expenses(expenses)
    elif choice == 2:
        view_expenses(expenses)
    elif choice == 3:
        total_expenses(expenses)
    elif choice == 4:
        highest_expenses(expenses)
    elif choice == 5:
        delete_expense(expenses)
    else:
        break
