month=int(input("Enter the month number:"))
match month:
    case month if month in (1,3,5,7,8,10,12):
        print("31 dayas in this month")
    case month if month in (4,6,9,11):
        print("30 dayas in this month")
    case 2:
        print("28 or 29 dayas in this month")
    case _:
        print("invalid month number")
