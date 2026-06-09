# # print("Hello world")
# a=12.0
# b=str(a)
# # print(type(b))
# c="uhduhguher"
# print(c[-3:]) #Slishing 
# d="Yujal"
# e="Khulal"
# print("My name is "+d+" "+e)
# print(f"My name is {d} {e}")
# #PMDAS
# a=200
# b=4
# print(a//b)
#Day 2
# a=int(input("Enter a number:"))
# if a%2==0:
#     print("Even")
# else:
#     print("Odd")
# math=int(input("Enter marks of math:"))
# science=int(input("Enter marks of science:"))
# nepali=int(input("enter marks of nepali:"))
# social=int(input("enter marks of social:"))
# computer=int(input("enter marks of computer:"))
# economics=int(input("enter marks of economicss:"))
# Total_Marks=600
# totalobtainmarks= math+ science+ nepali + social + computer+ economics
# percentage=(totalobtainmarks/Total_Marks)*100
# print("total obtained percentage is :", percentage)

# if percentage>90 and percentage<=100:
#     print("A")
# elif percentage>80 and percentage<=90:
#     print("B")
# elif percentage>70 and percentage<=80:
#     print("C")
# elif percentage>60 and percentage<=70:
#     print("D")
# elif percentage>50 and percentage<=60:
#     print("E")
# else:
#     print("Failed")


a= input("Say My Name:")
name= "heisenberg"
while True:
    if a==name:
        print("you are goddam right")
    else:
        print("Deal closed")
    
        

    # euta manxe xaa, manxe ko aagadi 3 ota baato xa, aaba tyo manxe ki ta right ,left  gayo vane game harxa.. 
# ra straight gayo vane pond or river ma pugxa..and then ask boat ma jane kii tairedai janey...
# if he choose to tairena tyo manxe palace ma pugxa, ra palace ma pugera usko aagadi chai 4 ota dhoka hunxa..
# else, boat ma jane vayo vane..boat is never gonna come , and you loose the game....back to palace, 
# uhh 1st  door ma gayo vane tiger le khayo ga,e over, 2nd ma ni bear le khayo , game over, 3rd door ma gayo vane ,
# you won the game vanera aaunu paroo, 4th door ma gayo vane you loose the game vanney

name= input("enter you name:")
ways= input("you have three ways, will'ya tell me, where do you wanna go ? (left, right, straight)")
if ways== "left" or ways== "Left":
    print(f"{name}, you loose the game.")
    again=input("Do you want to try again: Yes/No ? ")
elif ways== "straight" or ways=="Straight":
    print(f"{name}, you've reached a river.")
    survive= input("now, how do you wanna cross the river? by boat or swim?")
    if survive=="boat" or survive=="Boat":
        print(f"{name}, the boat is not comming, you loose the game.")
    elif survive== "swim" or survive== "Swim":
        print(f"{name}, congrats, you have cross the river and reached to the palace.")
        print("now, you've four doors, in front of you:")
        door= input("choose, which door you wanna open: (door 1, door 2, door 3 and door 4)")
        if door=="door 1" or door== "Door 1":
            print(f" soory, {name} you've eaten by tiger, Game Over!!")
        elif door=="door 2" or door=="Door 2":
            print(f"sorry, {name} you've got eaten by anaconda, Game Over!! ")
        elif door=="door 3" or door== "Door 3":
            print(f"congrats, {name}, you have found the hidden treasure. hence, you won the game!!!!!!")
        else:
            print(f"sorry, {name}, Lion got you hammmm, Game Over!!")  
else:
    print(f"{name}, you loose the game.")
