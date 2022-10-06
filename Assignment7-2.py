print("1.Addition","2.Subtraction","3.Multiplication","4.Division",sep='\n')
x=int(input("Enter your choice:"))
match x:
    case 1:
        print("Enter two number:")
        a,b=int(input()),int(input())
        print(a+b,":Sum of two numbers")
    case 2:
        print("Enter two number:")
        a,b=int(input()),int(input())
        print(a-b,":subtrac of two numbers")
    case 3:
        print("Enter two number:")
        a,b=int(input()),int(input())
        print(a*b,":multiplication of two numbers")
    case 4:
        print("Enter two number:")
        a,b=int(input()),int(input())
        print(a/b,":division of two numbers")
    case _:
        print("Invalid choice")
        
        
        
