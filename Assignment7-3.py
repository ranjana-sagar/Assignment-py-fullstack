print("a. Check whether a given set of three numbers are lengths of an isosceles triangle or not","b. Check whether a given set of three numbers are lengths of an right angle or not","c. Check whether a given set of three numbers are equilateral or not","d. Exit",sep='\n')
match input("Enter your choice"):
    case 'a':
        print("Enter three numbers:")
        a,b,c=int(input()),int(input()),int(input())
        if a==b or b==c or a==c:
            print("Isosceles Triangle")
        else:
            print("Isosceles not")
    case 'b':
        print("Enter three numbers:")
        a,b,c=int(input("Enter hypoteneous length")),int(input("Enter base length")),int(input("Enter hight length"))
        if a*a==b*b+c*c:
            print('right angle triangle')
        else:
            print("not right angle triangle")
    case 'c':
        print("Enter three numbers:")
        a,b,c=int(input()),int(input()),int(input())
        if a==b==c:
            print("Equilateral triangle")
        else:
            print("not equilateral triangle")
    case 'd':
        exit()
    case _:
        print("Invalid choice")
            
        
