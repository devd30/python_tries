#Python program to create dictionary from an obejct of a classs
# class test_class(object):
#     def __init__(self):
#         self.A=1
#         self.B=2
# obj=test_class()

# print obj.__dict__ #this will print dictionary

# print obj.__dict__.keys() , obj.__dict__.values() , obj.__dict__.items() # printing keys, values & dict.items()

# d={'a':122, 'b': 130, 'c': 23}
# print sum(d.values())

# class Dog(object):
#     species="mammal"
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age

# # a=Dog("milo", 6)
# # b=Dog("kiki",5)

# # print "{} and {} are {} and {} is years old".format(a.name, b.name, a.age, b.age)

# # if a.species == "mammal":
# #     print a.name
# # Instantiate the Dog object
# # jake = Dog("Jake", 7)
# # doug = Dog("Doug", 4)
# # william = Dog("William", 5)

# # def get_    biggest_num(*args):
# #     return max(args)

# # print "the oldeest dog is {} years old".format(get_biggest_num(jake.age,doug.age,william.age))

# #instance Method
#     def description(self):
#         return "{} is {} years old".format(self.name, self.age)

# #instance Method
#     def speak(self, sound):
#         return "{} says {}".format(self.name, sound)

# doug=Dog("Doug",9)

# print doug.description()
# print doug.speak("barkbark")

# class Email(object):
#     def __init__(self):
#         self.is_sent = False
#     def send_email(self):
#         self.is_sent = True

# check_email=Email()
# print check_email.is_sent

# check_email.send_email()
# print check_email.is_sent

# class Dog(object):
#     #Class attribute
#     species = "mammals"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     # instance method
#     def description(self):
#         return "{} is {}".format(self.name,self.age)
#     # instance method
#     def speak(self,sound):
#         return "{} speaks {}".format(self.name,sound)

# # Child class (inherits from Dog class)
# class Bull_dog(Dog):
#     def run(self,speed):
#         return "{} runs at {}mph".format(self.name, speed)

# class Pitbull(Dog):
#     def run(self,speed):
#         return "{} runs at {}".format(self.name,speed)

# dog1=Bull_dog("wick",12)
# print dog1.description()
# print dog1.run("slowly")

# dog2=Pitbull("john",14)
# print dog2.run("faster")

# print isinstance(dog1,Dog)
# print isinstance(Pitbull, Bull_dog)

class Mammal(object):
    def __init__(self,mammalName):
        print (mammalName,"is a warm blooded animal")

class Dog(Mammal):
    def __init__(self):
        print "Dog has four Legs"
        super(Mammal,self).__init__()
        print ('cat')

d1=Dog() 

    











