y=int(input("Enter an year:"))
match y:
    case y if y%100!=0 and y%4==0:
        print("Non century leap year")
    case y if y%100==0 and y%400==0:
        print("Century leap year")
    case y if y%100!=0 and y%4!=0:
        print("Non century non leap year")
    case y if y%100==0 and y%4!=0:
        print("Century non leap year")
    case _:
        print("Invalid year")
