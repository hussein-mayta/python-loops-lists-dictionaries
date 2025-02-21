
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

