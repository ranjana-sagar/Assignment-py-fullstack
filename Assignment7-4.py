match int(input("Enter your age:")):
    case x if 0<x<=10:
        print("kid")
    case x if 10<x<=20:
        print("Teenager")
    case x if 20<x<=40:
        print("Young")
    case x if 40<x<60:
        print("Experienced")
    case x if 60<=x:
        print("Senior citizen")
    case _:
        print("Invalid choice")
