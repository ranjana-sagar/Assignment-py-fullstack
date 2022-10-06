print("Enter two string:")
s1,s2=input(),input()
match(s1,s2):
    case(s1,s2)if s1==s2:
        print("identical string")
    case(s1,s2)if s1>s2:
        print("{} comes after {}".format(s1,s2))
    case(s1,s2)if s1<s2:
        print("{} comes before {}".format(s1,s2))
