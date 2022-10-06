x=input("What is your favourite color?")
match x:
    case x if 'yello' in x:
        print("yellow-Monday")
    case x if 'Blue' in x:
        print("Blue-Tuesday")
    case x if 'orange' in x:
        print("Orange-Wednesday")
    case x if 'white' in x:
        print("white-thursday")
    case x if 'black' in x:
        print("Black-Friday")
    case x if 'red' in x:
        print("Red-Saturday")
    case _:
        print("Sunday")
