# class hello:
#     def __init__(self,name,age,friend):
#         self.name=name
#         self.age=age
#         self.friend=friend
#     def haha(self):
#         print(f"My name is {self.name} and age is {self.age}") 
#         return  (f"mr {self.friend} is our friend")
    
# # yujal=hello("yujal",16,"ujwal")
# # print(yujal.name)
# # print(yujal.age)
# # print(yujal.haha())

#     def __str__(self):
#         return self.name

# a=hello("yujal",16,"ujwal is gay")
# print(a)

class ujwal:
    def __init__(self,name,age,occupation):
        self.name=name
        self.age=age
        self.occupation=occupation
    def detail(self):
        print(f"My name is {self.name}, and i am {self.age} years old, and i'm the owner of {self.occupation}")
aryan=ujwal("yujal",16,"Tesla")
aryan.name="ujwaaal" #to change the object's name
aryan.detail()