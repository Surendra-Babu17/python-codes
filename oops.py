'''INHERITNACE'''
'''
Inheritance means it is the fundamental concept in oops.
-> it is the process where on class acquries the attribute and method of another class.

USE OF INHERITANCE:
1.code reusebility 
2.reduces redundancy
3.herrarical relationship between classes

TYPES OF INHERITANCE:

1.SINGLE INHERITANCE
2.MULTIPLE INHERITANCE
3.MULTILEVEL INHERITANCE
4.HIERARCHICAL INHERITANCE

'''
#  1.Single Inheritance 
#  ----> single inheritance means one parent class one child class denotes single inheritance.

'''first create class just i was create basic class and object to understand every one''' 
class mythri_theater:       # crating class
    adress="nijampet"  #class attribute 
    state="HYB"
    capacity=1200
a=mythri_theater()    # create an object
print(a.adress) 
print(a.state)
print(a.capacity) 
print("adrees of the mythri theater is",a.adress,"and this thater present in ",a.state,"state and capacity in thos theater is:",a.capacity)  

'''single level inheritance'''
'''one parent class and one child class is denotes SINGLE INHERITANCE'''
'''FIRST CREATTING CLASS IN INHERITANCE METHOD'''  

class parent():         # creating parent class
    def output(self):    # constructor
        print("i am the parent") 
class child(parent):             #creating child class
    def outputc(self):
        print("i am the child")  
a=child()
a.output()
a.outputc() 


'''Multilevel inheritance'''
'''two parent classes one child class is known as multilevel inheritance''' 
class father():    # creating parent1 class
    def outputf(self):
        print("i am the father of the family") 
class mother(father):   # creating parent2 class
    def outputm(self):
        print("i am the mother of the family")  
class son_daughter(mother):
    def output_sd(self):
        print("i am the child of this family")
acess=son_daughter()
acess.outputm()
acess.outputf()
acess.output_sd()  
    
'''MULTIPLE INHERITANCE''' 
'''two parent classes one child class is known as multilevel inheritance''' 
class father():    # creating parent1 class
    def outputf(self):
        print("i am the father of the family") 
class mother(father):   # creating parent2 class
    def outputm(self):
        print("i am the mother of the family")  
class son_daughter(father,mother):
    def output_sd(self):
        print("i am the child of this family")
acess=son_daughter()
acess.outputm()
acess.outputf()
acess.output_sd()   



'''Herarical Inheritance''' 
'''one parent class multiple child classes''' 
class father_mother():
    def father_mother(self):
        print("we both are wife and husbands")
class child1(father_mother):
    def output(self):
        print("i am the older child and first perosn in my family")
class child2(father_mother):
    def child2(self):
        print("i am the older child and first perosn in my family")
class child3(father_mother):
    def child3(self):
        print("i am the older child and first perosn in my family")

class child4(father_mother):
    def child4(self):
        print("i am the older child and first perosn in my family") 
acess1=child1()
acess2=child2()
acess3=child3()
acess4=child4()
acess1.output()
acess1.father_mother()
acess2.child2() 


'''IN depth of the exaples in Inheritance'''
'''SINGLE LEVEL INHERITANCE''' 

class hero(): #one parent class
    def __init__(self,name,age,rating):
        self.name=name
        self.age=age 
        self.rating=rating 
        
    def hero_details(self):  
        print(f"Hero name is{self.name} and {self.age} years age.He is popular in worldwide his rating is{self.rating} out of 10")
class top_cinema(hero):                      #ond=e child class (single_level-inheritance) or  second parent class
    def top_movie(self):
        print(f"{self.name} top movie is Bhahubali")
#MULTILevel INHERITANCE  
class hero_language(top_cinema):
    def language(self):
        print(f"{self.name} is NO.1 tollywood hero he is world wide popular hero")

acess=hero_language("Prabhas",45,9.8)
acess.hero_details()
acess.top_movie()
acess.language()


# Parent class
class Animal:
    def speak(self):
        print("Animal speaks")

# Child class inherits from Animal
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Create object of Dog
d = Dog()
d.speak()  # Inherited method
d.bark()   # Own method







