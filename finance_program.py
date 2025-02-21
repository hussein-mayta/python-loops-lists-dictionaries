
print("Hello Nabiha ;")
print("  **Menu** ")
print(" 1: Enter data to manage your finances.")
print(" 2: Print data history.")
print(" 3: Exit.")

option = int(input("Enter your option :"))

data=[]
months=[]

while option != 3 :
    
    if option == 1:
        sm=float(input("Enter your monthly salary :"))  # sm: for salary of the month
        nm=input("Enter name of month :")  # nm: for name of month

        if nm not in months:
            months.append(nm)

            ps=float(input("Enter percentage of savings :"))     # ps: percentage saving
        
            pr=float(input("Enter percentage of rent :"))        # pr: percentage rent
        
            pe=float(input("Enter percentage of electricity :")) # pe: percentage electricity

            savingAmount = (sm * ps)/100
            
            rentAmount = (sm * pr)/100
            
            electricityAmount= (sm * pe)/100

            total= savingAmount + rentAmount + electricityAmount

            remainder = sm - total

            yearlyRent= rentAmount * 12
            yearlyElect= electricityAmount * 12

            poweredSalary= sm ** 2

            additional = float(input("Enter additional savings : "))
            left =round(additional / savingAmount,2)

            dic={
                "Month ": nm,
                "Salary ": sm,
                "Saving amount ": savingAmount,
                "Rent amount ": rentAmount,
                "Electricity amount ":electricityAmount,
                "Total spend " : total,
                "Salary remainder ": remainder,
                "yearly cost of rent  ":yearlyRent,
                "yearly cost of electricity ":yearlyElect,
                "Salary power 2 ":poweredSalary,
                "Left ": left,
            }

            data.append(dic)

        else :
            print("You already entered this month !!!")

    elif option ==2 :
        if len(data) == 0:
            print("You haven't entered any data yet")

        else:
            print("\nFinance History: ")
            for i in data :
                print("\n----------------------------------")
                for key, value in i.items():
                    print(f"{key}: {value}")  
                    
    option = int(input("Enter your option :"))      

print("EXIT")
  






