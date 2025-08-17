# #new.py is related to this inheritance example.
# Create a new file named new.py and add the following code to it:
# class Studnet():
#     name = "John"
#     age = 20
#     gender = "Male"
# from new import Student 

# class Person(Student):
#     pass

# p1 = Person()
# print(p1.name) 

# ----------------------------------------------------------------------------

# class Parent:
#     def __init__(self):
#         print("I am the parent class")

#     def greet(self):
#         print("Hello from Parent")

# class Child(Parent): 
#     def __init__(self): 
#         super().__init__()  # Calls parent constructor
#         print("I am the child class")

#     def greet(self):  # Method overriding
#         print("Hello from Child") 

# c = Child() # Creates an instance of Child
# c.greet()  # Calls the overridden method

# --------------------------------------------------------------



# # "Pehle neeche se input lega → Student class me jaayega → waha se parent class ko call karega → waha name and age set honge → fir grade set hoga → fir show_info() se sab print hoga."
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show_info(self):
#         print("Name:", self.name, ", Age:", self.age)

# class Student(Person):
#     def __init__(self, name, age, grade):
#         super().__init__(name, age)
#         self.grade = grade

#     def show_info(self):
#         super().show_info()
#         print("Grade:", self.grade)

# #Taking input from the user

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# grade = input("Enter your grade: ")

# student = Student(name, age, grade)
# student.show_info() # This will call the overridden method in Student class
# # This will print the name, age, and grade of the student

## -------------------------------------------------------------

# class CompanyData:
#     def __init__(self, emp_id, name):
#         self.emp_id = emp_id
#         self.name = name

#     def display_basic_info(self):
#         print(f"\nEmployee ID: {self.emp_id}")
#         print(f"Name: {self.name}")


# class Employee(CompanyData):
#     def __init__(self, emp_id, name, position):
#         super().__init__(emp_id, name)
#         self.position = position.lower()
#         self.salary, self.shift_hours = self.get_salary_and_shift()

#     def get_salary_and_shift(self):
#         position_data = {
#             "manager": (90000, "9am - 6pm"),
#             "senior developer": (70000, "10am - 6pm"),
#             "junior developer": (40000, "10am - 5pm")
#         }
#         return position_data.get(self.position, (0, "N/A"))

#     def display(self):
#         self.display_basic_info()
#         print(f"Position: {self.position.title()}")
#         print(f"Salary: ₹{self.salary}")
#         print(f"Shift Hours: {self.shift_hours}")


# class Intern(CompanyData):
#     def __init__(self, emp_id, name, months):
#         super().__init__(emp_id, name)
#         self.months = months
#         self.stipend = self.calculate_stipend()

#     def calculate_stipend(self):
#         # Simple logic: ₹5000/month
#         return self.months * 5000

#     def display(self):
#         self.display_basic_info()
#         print(f"Internship Duration: {self.months} month(s)")
#         print(f"Stipend: ₹{self.stipend}")


# # --------- User Interaction Logic ---------
# def main():
#     print("📋 Welcome to Company Database System")
#     emp_id = input("Enter Employee ID: ")
#     name = input("Enter Name: ")
#     emp_type = input("Is this person an Employee or Intern? ").strip().lower()

#     if emp_type == "employee":
#         position = input("Enter Position (Manager / Senior Developer / Junior Developer): ").strip().lower()
#         emp = Employee(emp_id, name, position)
#         emp.display()
#     elif emp_type == "intern":
#         try:
#             months = int(input("Enter Duration of Internship (in months): "))
#             intern = Intern(emp_id, name, months)
#             intern.display()
#         except ValueError:
#             print("❌ Invalid input for months. Please enter a number.")
#     else:
#         print("❌ Invalid type entered. Please enter 'Employee' or 'Intern'.")

# # Run the program
# main()
   

































