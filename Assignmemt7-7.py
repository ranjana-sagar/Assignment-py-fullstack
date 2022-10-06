x=float(input("Enter a number:"))
match x:
    case x if x>0:
        print("positive number")
    case x if x==0:
        print("Zero")
    case x if x<0:
        print("Negative number")
    case _:
        print("Invalid number")
