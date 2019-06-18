BJB = 0
Cong = 0
AAP = 0
others = 0
Admin_usr = "Virenderox"
pas = "evm1997"
l = []
while(1):
    print("     \nWelcome")
    print("\n1.) Admin")
    print("2.) User")
    print("3.) Exit")
    inp = int(input("\nEnter your Choice:"))
    if inp == 2:
        print("\n1.) BJB")
        print("2.) Congress")
        print("3.) AAP")
        print("4.) Others")
        h = int(input("\nEnter your Choice:"))
        if h == 1:
            BJB += 1
        elif h == 2:
            Cong += 1
        elif h == 3:
            AAP += 1
        elif h == 4:
            others += 1
        else:
            print("\nInvalid Option")
    elif inp == 1:
        i = input("\nEnter your AdminName:")
        if i == Admin_usr:
            j = input("Password:")
            if j == pas:
                print("\nWelcome")
                l.append(BJB)
                l.append(Cong)
                l.append(AAP)
                l.append(others)
                m = max(l)
                ind = l.index(m)
                print("\nBJB Vote Count:",l[0])
                print("Congress Vote Count:",l[1])
                print("APP Vote Count:",l[2])
                print("Others Vote Count:",l[3])
                print("\nwinner:")
                if ind == 0:
                    print("BJB:",l[0])
                elif ind == 1:
                    print("Congress:",l[1])
                elif ind == 2:
                    print("AAP:",l[2])
                else:
                    print("Others:",l[3])
                break
            else:
                print("\nInvalid Password")
                continue
        else:
            print("\nInvalid AdminName")
            continue
    elif inp == 3:
        break
    else:
        print("\nInvalid Option")
