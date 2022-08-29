income = {"rent":0, "laundry":0, "storage":0}
utility = {"water":0, "electric":0, "gas":0, "trash":0, "sewage":0}
expense = {"tax":0, "insurance":0, "HOA":0, "yard":0, "management":0, "repairs":0, "vacancy":0, "CapEx":0, "mortgage":0}
investment = {"downpayment":0, "closingcost":0, "rehab":0}


def int_input(prompt):
    while True:
        try:
            edgecase = int(input(prompt))
            return edgecase
        except ValueError as x:
            print("Please enter a valid number.")
#main flow
while True:
    mainmenu = int_input("""
==================
  ROI Calculator
    Main Menu
==================
1. Income
2. Expenses
3. Investments
4. Summary
5. Exit
==================
  Enter a number
==================
""")
#income menu 
    if mainmenu == 1:
        incomemenu = int_input("""
    ==================
      Income Sources
    ==================
    1. Rent
    2. Laundry
    3. Storage
    4. Misc
    5. View
    6. Main Menu      
    ==================
      Enter a number
    ==================
""")
#each option exists in dictionary
#misc items can be added to respective dictionary on any menu
        if incomemenu == 1:
            cost = int_input("Enter the monthly amount per unit ")
            income["rent"] = cost
        elif incomemenu == 2:
            cost = int_input("Enter the monthly amount per unit ")
            income["laundry"] = cost
        elif incomemenu == 3:
            cost = int_input("Enter the monthly amount per unit ")
            income["storage"] = cost
        elif incomemenu == 4:
            incomeitem = input("What item would you like to add? ")
            if incomeitem in income:
                print("Item is already accounted for.")
            else:
                cost = int_input("Enter the monthly amount per unit ")
                income[incomeitem] = cost
                print(f"{incomeitem} is now accounted for.")
        elif incomemenu == 5:
            for incomeitem in income:
                    print(f'{incomeitem.title()} ${income[incomeitem]}')
            print(f"Total ${sum(income.values())}")
        elif incomemenu != {1,2,3,4,5,6}:
                print("Enter a valid number please. ")     
#expense menu
    elif mainmenu == 2:
        expmenu = int_input("""
    ==================
      Expense Sources
    ==================
     1. Tax
     2. Insurance
     3. Utilities
     4. HOA
     5. Yard
     6. Management
     7. Repairs
     8. Vacancy
     9. CapEx
    10. Mortgage
    11. Misc
    12. View
    13. Main Menu      
    ==================
      Enter a number
    ==================
""")
        if expmenu == 1:
            cost = int_input("Enter the monthly amount per unit ")
            expense["tax"] = cost
        elif expmenu == 2:
            cost = int_input("Enter the monthly amount per unit ")
            expense["insurance"] = cost
#utility submenu            
        elif expmenu == 3:
            utilmenu = int_input("""
        ==================
            Utilities
        ==================
        1. Water
        2. Electric
        3. Gas
        4. Trash
        5. Sewage
        6. Misc
        7. View
        8. Expense Menu     
        ==================
          Enter a number
        ==================
""")
            if utilmenu == 1:
                cost = int_input("Enter the monthly amount per unit ")
                utility["water"] = cost
            elif utilmenu == 2:
                cost = int_input("Enter the monthly amount per unit ")
                utility["electric"] = cost
            elif utilmenu == 3:
                cost = int_input("Enter the monthly amount per unit ")
                utility["gas"] = cost
            elif utilmenu == 4:
                cost = int_input("Enter the monthly amount per unit ")
                utility["trash"] = cost
            elif utilmenu == 5:
                cost = int_input("Enter the monthly amount per unit ")
                utility["sewage"] = cost
            elif utilmenu == 6:
                utilitem = input("What item would you like to add? ")
                if utilitem in utility:
                    print("Item is already accounted for.")
                else:
                    cost = int_input("Enter the monthly amount per unit ")
                    utility[utilitem] = cost
                    print(f"{utilitem} is now accounted for.")
            elif utilmenu == 7:
                for utilitem in utility:
                    print(f'{utilitem} ${utility[utilitem]}')
                print(f"Total ${sum(utility.values())}")
            elif utilmenu != {1,2,3,4,5,6,7,8}:
                print("Enter a valid number please. ")
#back to expense menu
        elif expmenu == 4:
            cost = int_input("Enter the monthly amount per unit ")
            expense["HOA"] = cost
        elif expmenu == 5:
            cost = int_input("Enter the monthly amount per unit ")
            expense["yard"] = cost
        elif expmenu == 6:
            cost = int_input("Enter the monthly amount per unit ")
            expense["management"] = cost
        elif expmenu == 7:
            cost = int_input("Enter the monthly amount per unit ")
            expense["repairs"] = cost
        elif expmenu == 8:
            cost = int_input("Enter the monthly amount per unit ")
            expense["vacancy"] = cost
        elif expmenu == 9:
            cost = int_input("Enter the monthly amount per unit ")
            expense["CapEx"] = cost
        elif expmenu == 10:
            cost = int_input("Enter the monthly amount per unit ")
            expense["mortgage"] = cost
        elif expmenu == 11:
            expenseitem = input("What item would you like to add? ")
            if expenseitem in expense:
                print("Item is already accounted for.")
            else:
                cost = int_input("Enter the monthly amount per unit ")
                expense[expenseitem] = cost
                print(f"{expenseitem} is now accounted for.")
        elif expmenu == 12:
            for expenseitem in expense:
                    print(f'{expenseitem.title()} ${expense[expenseitem]}')
            print(f"Total ${sum(expense.values())}")
        elif expmenu != {1,2,3,4,5,6,7,8,9,10,11,12}:
                print("Enter a valid number please. ")
#investment menu        
    elif mainmenu == 3:
        invmenu = int_input("""
    ==================
       Investments
    ==================
    1. Down Payment
    2. Closing Costs
    3. Rehab Budget
    4. Misc
    5. View
    6. Main Menu      
    ==================
      Enter a number
    ==================
""")
        if invmenu == 1:
            cost = int_input("Enter the amount per unit ")
            investment["downpayment"] = cost
        elif invmenu == 2:
            cost = int_input("Enter the amount per unit ")
            investment["closingcost"] = cost
        elif invmenu == 3:
            cost = int_input("Enter the amount per unit ")
            investment["rehab"] = cost
        elif invmenu == 4:
            investitem = input("What item would you like to add? ")
            if investitem in investment:
                print("Item is already accounted for.")
            else:
                cost = int_input("Enter the amount per unit ")
                investment[investitem] = cost
                print(f"{investitem} is now accounted for.")
        elif invmenu == 5:
            for investitem in investment:
                    print(f'{investitem.title()} ${investment[investitem]}')
            print(f"Total ${sum(investment.values())}")
        elif invmenu != {1,2,3,4,5}:
                print("Enter a valid number please. ")
#summary menu
    elif mainmenu == 4:
        summarymenu = int_input("""
    ==================
       Summaries
    ==================
    1. Total Income
    2. Total Expense
    3. Total Investment
    4. Cash Flow
    5. RoI
    6. Main Menu      
    ==================
      Enter a number
    ==================      
""")
        if summarymenu == 1:
            totalincome = 0 + sum(income.values())
            print(f"Total Income ${totalincome}")
        elif summarymenu == 2:
            totalexpense = 0 + sum(expense.values()) + sum(utility.values())
            print(f"Total Expenses ${totalexpense}")
        elif summarymenu == 3:
            totalinvest = 0 + sum(investment.values())
            print(f"Total Investment ${totalinvest}")
        elif summarymenu == 4:
            cashflow = 0 + totalincome - totalexpense
            print(f"Cash Flow ${cashflow}")
        elif summarymenu == 5:
            RetInv = cashflow / totalinvest
            RetInvAnn = cashflow * 12 / totalinvest
            print(f"Monthly Return on Investment is {RetInv * 100}%")
            print(f"Annual Return on Investment is {RetInvAnn * 100}%")
        elif summarymenu != {1,2,3,4,5,6}:
            print("Enter a valid number please. ")
#quit
    else:
        print("""
        Thank you for playing elaborate shopping cart
        """)
        break