# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings
# s1 = "Hello how are you"
# s2 = "Hello how is"

s1 = "Hello how are you"
s2 = "Hello how is"

s1 = s1.split(" ")
s2 = s2.split(" ")

for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    f val not in s1:
        print(val)

# 3.)Wrire a code print the 8th fibanochi number
# 0,1,2,3,5,8,
num=5
n1=0
n2=1
for val in range 
# object =c1()
#object.display ()
#? Eg :6
class class1:
    def__int__(self):
        name="mansoor"
        email="mansoorbaasha2003@gmail.com"
        #return name,email#error---->cant use return with constructor
        def display (self):
   # ? Eg:6
# ? To use the variable inside the constructor in another methods 
class class1:
    def _init_(self):
        self.name = "hari"
        self.email = "hareeshpeetla4046@gmail.com"
        # return name,email #error ---> cannot use return with constructor

    def display (self):
         print(self.name, self.email)

c1 = class1()
c1.display()


            
#!------>Inheritance
#5 types of inheritence
#single inheritence
#multilevel inheritence
#multiple inheritence
#hybrid inheritence
#heirarichal inheritence

#*single inheritence
#? it has only one parent class and only one child class

 # ! Eg:1
 class parent:
     def m2 (self):
         print ("Iam  child class ")
obj=child ()
obj.m1()

 # ! Eg:2


class c1:
    def _init_(self):
        print(" I am constructor from parent class")

class child1(c1):
    pass

obj= child1()

class child (parent):
    def display (self):
        print (self . name)
d=child()
d. display()

all=parrot ()
all.dog_voice()
#all.sound()
#all.parrot_voice()
class honda_city:
    def honda_city_engine_speces(self, cc, hp, torque, fuel_type, num_of_pistin):
        print(cc, hp, torqu, fuel_type, num_of_piston)
        
    def honda_city__engine_speces(self, cc, hp, torque, fuel_type, num_of_pistin):
        print(cc, hp, torqu, fuel_type, num_of_piston)

class amaze(honda_city):
    def amaze_engine_speces(self, cc, hp, torque, fuel_type, num_of_pistin):
        print(cc, hp, torqu, fuel_type, num_of_piston)


    def amaze_body_speces(self, cc, hp, torque, fuel_type, num_of_pistin):
         print(cc, hp, torqu, fuel_type, num_of_piston)

class civic(amaze):
    def civic_engine_speces(self, cc, hp, torque, fuel_type, num_of_pistin):
         print(cc, hp, torqu, fuel_type, num_of_piston)

    def civic_engine_speces(self, cc, hp, torque, fuel_type, num_of_pistin):
         print(cc, hp, torqu, fuel_type, num_of_piston)


class Honda(civic):
    pass

honda = Honda()
honda.honda_city_engin_specs(1500, 230, 2979, "petrol" 4)
honda.civic_body_specs("white", 2000, 5.5, 8, "Hatchback")

# ! multiple inheritance
# ? it has multiple parent and 1 child


p=petrol()
p.defanition()
# Eg:2
# MRO---> Method resolution Order
class addition:
    def add(self, a, b):
        print(a+b)
    def mul(self,a,b):
        print(a%b)
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)
calc=division()
calc.add(3,4)
calc.mul(5,2)

clclass c6(


#Hybrid Inheritance
# The combination of above 4 inheritance is called Hybrid inheritance
class c1:
    def m1(self):
        print("Class1")
class c2:
    def m2(self):
        print("class2")
class c3:
    def m3(self):
        print("Class 3")
class c4:
    def m4(self):
        print("Class 4")
class c5:
    def m5(self):
        print("Class 5")
class c6:
    def m6(self):
        print("Class 6")

obj= c6()
obj.m3()

# ! ------------>polymorphism
# poly - many ,morph --->form
# A function which has the ability to perform more than 1 functionality
#then it is considered to be as polymorphism

# * polymorphism in builtin functions
#ken() --> Which is used to find the length of list,tuple,dict etc...
#Index()
#Max()
#Min()
#Count()
#pop()

# *
print(6*7)
l1 = {12,3,4,5,6}
print(*l1)
def f1(*args)
l1 = [1,2,3,4]
print(l1*10)


polymorphism in classes
we can achieve polymorphism in 2 ways
1.) method overloading --> it is not possible in python
2.) method overriding

tasks
write the code for the below tasks using function
1.)d1 = {"shirt": 1000, "pant":1500, "shoes": "900", "handkey": 30}
a.) find the min ans max priced product
b.) find the product starts with 's' and 's'

2.) find the n = 67, is strong number or not

3.) l1 = [1,2,3,4,5,6]
n=2 --> [5, 6, 1,2,3,4]
n=3 --> [4,5,6, 1,2,3]










     
