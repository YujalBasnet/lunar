# customer=input("Enter the name of the customer: ")
# shopkeeper=input("We have Chomwein on our menu: (Veg/ Egg) ").upper().lower()
# if shopkeeper=="veg":
#     fullvegprice=100
#     halfvegprice=50
#     veg=input(f"{customer}, Do you want half plate or full plate: ").upper().lower()
#     if veg=="half".upper().lower():
#         print(f"{customer}, The total price will be: {halfvegprice}")
#     if veg=="full".upper().lower():
#         print(f"{customer}, The total price will be: {fullvegprice}")

# elif shopkeeper=="egg":
#     fulleggprice=120
#     halfeggprice=60
#     egg=input(f"{customer}, Do you want half or full plate: ").upper().lower()
#     if egg=="half".upper().lower():
#         print(f"{customer}, The total price will be: {halfeggprice}")
#     if egg=="full".upper().lower():
#         print(f"{customer}, The total price will be: {fulleggprice}")
# else:
#     print(f"Sorry, we dont have {shopkeeper}.")

# fullveg=100
# halfveg=50
# fullegg=120
# halfegg=60
# shopkeeper=input("We have chowmein on our menu: (Veg/ Egg)").upper().lower()
# if shopkeeper=="veg":
#     veg=input("You want full or half: ").upper().lower()
#     if veg=="full":
#         print(f"total price will be: {fullveg}")
#     elif veg=="half":
#         print(f"total price will be: {halfveg}")
# elif shopkeeper=="veg":
#     egg=input("you want half or full: ")
#     if egg=="half":
#         print(f"total price will be: {halfegg}")
#     elif egg=="full":
#         print(f"total price will be: {fullegg}")

plate=input("Half or Full ")
if plate=="half":
    price=50
elif plate=="full":
    price=100
item=input("chowmein or Momo ? ").upper().lower()
if item=="chowmein":
    kun=(input("Want veg or Chicken:? ")).upper().lower()
    if kun=="veg":
        price+=20
        print(f"your total bill is : {price}") 
    elif kun=="chicken":
        price+=40
        print(f"your bill is: {price}")
if item=="momo":
    type=(input("want veg or chicken ? "))
    if type=="veg":
        price+=30
        print(f"your total bill is: {price}")
    elif type=="chicken":
        price+=60
        print(f"your total bill is: {price}")