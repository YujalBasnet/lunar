# a=int(input("Enter a number: "))
# while a !=0:
#     b=input("Try again: ")
#     if b=="yes":
#         a=int(input("Enter a number: "))    
# print("good")
# a=int(input("kun ko table chaiyo: "))
# b=int(input("kati samma ko table chaiyo: "))
# i=1
# while i<=b:
#     print(a*i)
#     i+=1
#List-->
# a=["yujal","ujwal","aaryan"]
# a[1]="Hari"#it update , in the postion of ujwal it updated as Hari
# print(a)

# a=["yujal","aryan","ujwal"]
# for i in a:
#     if "aryan" in i:
    
#         print(i)

# a=[]
# b=int(input("how many names you want to enter: "))
# for i in range(b):
#     c=input(f"enter {i+ 1} name:")
#     a.append(c)
# print(a)

#Tupel----------------------------------------------------------------------------------------------->

# a=("binayak","ujwal","yujal","aaryan")
# b=list(a)
# b.append("aayush")
# c=tuple(b)
# print(c)

#DICTIONERY--------------------------->
disc={"nameee":"yujal", "age":16}
disc.pop("nameee")# yesle chai name ko value ra key lai delete handinxa (.popitems) le chai last ko delete handinxa
print(disc.values())
print(disc["age"]) #to print specific value
disc.clear()  #yesle chai disctinoney lai khali banai dinxa
print(disc)