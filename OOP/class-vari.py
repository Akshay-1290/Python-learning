class Student:
   #variable and value that are defined under the class are called ...
   class_year = 2025
   num_students = 0

   def __init__(self, name, age):
       self.name = name
       self.age = age
       Student.num_students += 1

student1 = Student("Akshay", 18)
student2 = Student("Atharv", 19)
student3 = Student("Chaggan", 20)
student4 = Student("Atigy", 30)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
print(f"{student4.name} is {student4.age} years old ")