# -*- coding: utf-8 -*-
"""Final Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PVQ2HQDj2rtjObDjZbtJViRkT6alCb93
"""

print("---------Company Management System----------")

#Names     #Ages     #Manager     #Languages
#Can        #30      #Ayse(45)         #Turkish, English, Russian
#Selma      #42      #Ali(46)          #Turkish, English, Japanese, German
#Nadine     #21      #Oliver(40)       #English, German
#Paul       #53      #Selin(30)        #French
#Simone     #27      #Seda(35)         #Spanish, Turkish, Chinese

class Employee():

  def __init__(self, name, age, manager):
    self.name = name
    self.age = age
    self.manager = manager
    self.language = []


  def show_employee_info(self):
    print("Employee name: " + self.name + ", Age: " + str(self.age) + ", Manager: " + self.manager)

  def speak_lang(self, ableLanguage):
    print("Speaks:", ableLanguage)  
    self.language.append(ableLanguage)


employee1 = Employee("Can", "30", "Ayse")
employee2 = Employee("Selma", "42", "Ali")
employee3 = Employee("Nadine", "21", "Oliver")
employee4 = Employee("Paul", "53", "Selin")
employee5 = Employee("Simone", "27", "Seda")

#employee1.show_employee_info()
#employee2.show_employee_info()
#employee3.show_employee_info()
#employee4.show_employee_info()
#employee5.show_employee_info()

employee_name = input("Enter a name: ")
if employee_name == "Can":
  employee1.show_employee_info()
elif employee_name == "Selma": 
  employee2.show_employee_info()
elif employee_name == "Nadine": 
  employee3.show_employee_info()
elif employee_name == "Paul": 
  employee4.show_employee_info()
elif employee_name == "Simone": 
  employee5.show_employee_info()
else:
  print("Not an employee!")

employee1.speak_lang("Turkish")
employee1.speak_lang("English")
employee1.speak_lang("Russian")

print(employee1.language)

employee2.speak_lang("Turkish")
employee2.speak_lang("English")
employee2.speak_lang("Japanese")
employee2.speak_lang("German")

print(employee2.language)

employee3.speak_lang("English")
employee3.speak_lang("German")


print(employee3.language)

employee4.speak_lang("French")

print(employee4.language)

employee5.speak_lang("Turkish")
employee5.speak_lang("Spanish")
employee5.speak_lang("Chinese")

print(employee5.language)

class Manager():

  def __init__(self, name, age, manager):
    self.name = name
    self.age = age
    self.manager = manager
    self.language = []


  def show_manager_info(self):
    print("Manager name: " + self.name + ", Age: " + str(self.age) + ", Sr. Manager: " + self.manager)

  def speak_lang(self, ableLanguage):
    print("Speaks:", ableLanguage)  
    self.language.append(ableLanguage)

manager1 = Manager("Ayse", "45", "Fatma")
manager2 = Manager("Ali", "45", "Melda")
manager3 = Manager("Oliver", "40", "Sebastian")
manager4 = Manager("Selin", "30", "John")
manager5 = Manager("Seda", "35", "Mehmet")

#manager1.show_manager_info()
#manager2.show_manager_info()
#manager3.show_manager_info()
#manager4.show_manager_info()
#manager5.show_manager_info()

manager_name = input("Enter a name: ")
if manager_name == "Ayse":
  manager1.show_manager_info()
elif manager_name == "Ali": 
  manager2.show_manager_info()
elif manager_name == "Oliver": 
  manager3.show_manager_info()
elif manager_name == "Selin": 
  manager4.show_manager_info()
elif manager_name == "Seda": 
  manager5.show_manager_info()
else:
  print("Not a manager!")

manager1.speak_lang("Turkish")
manager1.speak_lang("Chinese")
manager1.speak_lang("Russian")

print(manager1.language)

manager2.speak_lang("English")
manager2.speak_lang("Spanish")
manager2.speak_lang("Russian")
manager2.speak_lang("Italien")

print(manager2.language)

manager3.speak_lang("English")
manager3.speak_lang("Spanish")
manager3.speak_lang("Italien")

print(manager3.language)

manager4.speak_lang("Turkish")
manager4.speak_lang("English")

print(manager4.language)

manager5.speak_lang("Turkish")
manager5.speak_lang("English")
manager5.speak_lang("German")

print(manager5.language)