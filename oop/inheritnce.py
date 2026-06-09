# class parents:
#     def __init__(self,name):
#         self.name=name
        
        
# class son(parents):
#     pass
# s=son("Aryan")
# print(s.name)

class dog:
    def __init__(self,name):
        self.name=name
        
        
class cat:
    def __init__(self,behaviour):
        self.behaviour=behaviour
        
class people(dog,cat):
    def __init__(self,age,behaviour,name):
        dog.__init__(self,name)
        cat.__init__(self,behaviour)
        self.age=age
        self.name=name
        self.behaviour=behaviour

a=people("dance","aryan",18)
print(a.age)
print(a.name)
print(a.behaviour)
        