
math=int(input("Enter marks of math:"))
science=int(input("Enter marks of science:"))
nepali=int(input("enter marks of nepali:"))
social=int(input("enter marks of social:"))
computer=int(input("enter marks of computer:"))
economics=int(input("enter marks of economicss:"))
Total_Marks=600
if 100>=math>=0 and 100>=science>=0 and 100>=nepali>=0 and 100>=social>=0 and 100>=computer>=0 and 100>=economics>=0: 
    totalobtainmarks= math+ science+ nepali + social + computer+ economics
    percentage=(totalobtainmarks/Total_Marks)*100
    print("total obtained percentage is :", percentage)
    if (math or science or nepali or social or computer or economics) <50:
        print("You have failed")
    elif percentage>90 and percentage<=100:
            print("A")
    elif percentage>80 and percentage<=90:
            print("B")
    elif percentage>70 and percentage<=80:
            print("C")
    elif percentage>60 and percentage<=70:
            print("D")
    elif percentage>50 and percentage<=60:
            print("E")
    else:
            print("Failed")
else:
    print("Invalid number")