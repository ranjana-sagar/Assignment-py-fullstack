match int(input("Enter a number:")):
    case x if x%2==0:
        print("Saurabh Shukla")
    case x if x<0 and x%2:
        print("Prateek Jain")
    case x if x%2!=0:
        print("Aditya Choudhary")
    case _:
        print("Invalid Choice")
