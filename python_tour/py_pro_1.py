print(" 1.)      Sign up.")
print(" 2.)      Sign in.")
print(" 3.)      Delete Account.")
print(" 4.)      Show User Detail.")
record = [["virenderox", "prince", "viru_1997", "cool_coder"],[12341997, 1231997, 1997123,31101997],[1000,2000,30000,400000]]
def entry(amount, ind):
    print("\nWelcome...")   
    print("\nYou have four options:")
    print("1.) check Amount :")
    print("2.) Amount Widrawal:")
    print("3.) Amount Deposit:")
    print("4.) pin_change:")
    print("5.) Exit")
    op = int(input("Enter your Choice: "))
    if op == 1:
        print("Your current amount is :",amount[ind])
    elif op == 2:
        am = int(input("Enter your Amount"))
        if am < amount[ind]:
            amount[ind] = amount[ind] - am
            print("Your updated Amount is :",amount[ind])
        else:
            print("Does Not have Sufficient balance:")
    elif op == 3 :
        dp =int(input("Enter your Amount to be deposit: "))
        amount[ind] = amount[ind] + dp
        print("Your updated Amount is :",amount[ind])
    elif op == 4 :
        ps = int(input("Enter the New password: "))
        password[ind] = ps
        print("Password changed:")
    elif op == 5:
        quit(None)
    else:
        print("Invalid Choice")
while(1):
    a = int(input("Enter your choice:"))
    if a == 2:
        ur = input(" Username:")
        ps = (input(" Password:"))
        cp = (input(" Confirm Password:"))
        amo = int(input(" Enter Amount:"))
        user_name = record[0]
        password = record[1]
        amount = record[2]
        user_name.append(ur)
        indd = user_name.index(ur)
        if ps == cp:
            record[0].append(ur)
            record[1].append(ps)
            record[2].append(amo)
            entry(amount,indd)
        else:
            print("Somthing went worng in password")
    elif a == 1:
        user_name = record[0]
        password = record[1]
        amount = record[2]
        while(1):
            usr = input("Enter the username: ")
            if usr in user_name:
                pas = int(input("Enter the password: "))
                ind = user_name.index(usr)
                if password[ind] == pas:
                    entry(amount, ind) 
                else:
                    print("Invalid Option")
            else:
                print("\nSomething went worng")
                print("Please try again:\n")
    elif a == 3:
        usr = input("Enter the username: ")
        if usr in user_name:
            pas = int(input("Enter the password: "))
            ind = user_name.index(usr)
            if password[ind] == pas:
                del(record[0][ind])
                del(record[1][ind])
                del(record[2][ind])
            else:
                print("Invalid Password")
        else:
            print("Invalid Information")
    elif a == 4:
        usr = input("Enter the username: ")
        if usr in user_name:
            pas = int(input("Enter the password: "))
            ind = user_name.index(usr)
            if password[ind] == pas:
                print(  "\nRecord:  \n")
                print("Name: ",record[0][ind])
                print("Password: ",record[1][ind])
                print("Amount: ",record[2][ind])
            else:
                print("Invalid Password")
        else:
            print("Invalid Information")
    else:
        print("Invalid Option")
        
                
        
        
        


  
