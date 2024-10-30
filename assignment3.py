#!/usr/bin/env python
# coding: utf-8

# Q1.Explain Class and Object with respect to Object-Oriented Programming. Give a suitable example.

# Class is a blueprint where in it provides the attributes and methods to design a object
# 
# Object is an specific instance created for the class each object can have its own attributes and values 

# In[3]:


class movies:
    def __init__(self,actor,actress):
        self.actor = actor
        self.actress  = actress
    


# In[4]:


DDLJ = movies('sharukh','kajol')


# Q2.Name the four pillars of OOPs.

# 1.Encapsulation
# 2.polymorphism
# 3.Abstraction
# 4.Inheritance

# Q3. Explain why the __init__() function is used. Give a suitable example.

# ini() functon is called intializer or instructor it is basically gives attributes to the class in the intialstage.

# In[5]:


class college:
    def __init__(self,students,teachers,helpers):
        self.students = students
        self.teachers = teachers
        self.helpers = helpers


# Q4. Why self is used in OOPs?

# self in the oops is like call the class itself like when we create a method or a function we use it to bind it to the class .self is a reference to the current instance of the class.It is used to access variables and methods associated with that instance

# Q5.What is inheritance? Give an example for each type of inheritance.

# Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows a new class to inherit attributes and methods from an existing class. This promotes code reusability and establishes a relationship between classes.

# In[19]:


##single inheritance

class parent:
    def love(self):
        return "i love people"
        
class child(parent):
    def play(self):
        return "i love to play"


# In[21]:


vinay = child()
print(vinay.love())
print(vinay.play())


# In[22]:


#multiple inheritance

class father:
    def read(self):
        return "i love reading"
    
class mother:
    def cook(self):
        return "i love cooking"
    
class child(father,mother):
    def play(self):
        return "i love playing"
    
vinay = child()
print(vinay.read())
print(vinay.cook())
print(vinay.play())


# In[23]:


#Multilevel inheritance

class grandpa:
    def knowledge(self):
        return " i have knowledge"

class father(grandpa):
    def wealth(self):
        return "i have wealth"

class son(father):
    def play(self):
        return "i love to play"
    
vinay = son()
print(vinay.knowledge())
print(vinay.wealth())
print(vinay.play())


# In[25]:


#Hierarchical Inheritance
class parent:
    def love(self):
        return " i have love"

class child1(parent):
    def music(self):
        return "i love music"
    
class child2(parent):
    def racing(self):
        return "i love racing"

vinay  = child1()
vijay = child2()

print(vinay.love())
print(vinay.music())
print(vijay.love())
print(vijay.racing())


# In[27]:


class father:  
    def cooking(self):
        return "I can cook delicious meals."

class mother:  
    def teaching(self):
        return "I can teach well."

class Child(father,mother):  
    def sports(self):
        return "I excel in sports!"

my_child = Child()
print(my_child.cooking()) 
print(my_child.teaching())  
print(my_child.sports())    


# In[ ]:




