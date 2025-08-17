# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person ('John', 87)
# print(p1.name)
# print(p1.age)

# # -------------------------------------------------------------

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# name  = str(input("Enter your name: "))
# age = int(input("Enter your age: "))
# p1 = Person (name, age)
# print(p1.name)
# print(p1.age)


# # -------------------------------------------------------------
# class Car:
#     def __init__(self, brand):
#         self.brand = brand

#     def display_brand(self):
#         print("The car brand is", self.brand)

# my_car = Car(str(input("Enter the car brand: ")))
# my_car.display_brand()

# # -------------------------------------------------------------
# # Car with Features
# class CarFeature:
#     def __init__(self, brand, features):
#         self.brand = brand # Store car brand
#         self.features = features # Store list of features

    
# # Method to display brand of the car
#     def display_brand(self):
#         print("The car brand is", self.brand)


# # Method to display features of the car
#     def display_feature(self):
#         if len(self.features) <= 0:
#             print("No features available for this car ")
#         else:
#             print("Features: ")
#             for feature in self.features: # Loop through the list and print each feature
#                 print("-", feature)    


# # Input Section

# brand = input("Enter the car brand: ")

# # ASk user how many features they want to add

# num = int(input("How many features do you want to add? "))
# features = [] # Initialize an empty list to store features

# # if user wants to add features
# if  num > 0:
#     for i in range(num):
#         feat = input(f"Enter feature {i+1}: ") # Take input one by one 
#         features.append(feat) # Add to list


# my_car = CarFeature(brand, features) # Create an instance of CarFeature
# my_car.display_brand()
# my_car.display_feature()

# # -------------------------------------------------------------

# # Target:
# # Multiple car inputs lene hain (brand + features).
# # Jab tak user kahe "nahi", tab tak input continue chale.
# # Sabhi data list of objects ke form mein store ho.
# # End mein saare cars ka brand aur unke features print ho.

# # Car with Features
# class CarFeature:
#     def __init__(self, brand, features):
#         self.brand = brand # Store car brand
#         self.features = features # Store list of features

    
# # Method to display brand of the car
#     def display_brand(self):
#         print("The car brand is", self.brand)


# # Method to display features of the car
#     def display_feature(self):
#         if len(self.features) <= 0:
#             print("No features available for this car ")
#         else:
#             print("Features: ")
#             for feature in self.features: # Loop through the list and print each feature
#                 print("-", feature)    

# # List to store all car objects
# all_cars = []

# while True:
#    # Input Section
#     brand = input("Enter the car brand: ")

#     # ASk user how many features they want to add

#     num = int(input("How many features do you want to add? "))
#     features = [] # Initialize an empty list to store features

#     # if user wants to add features
#     if  num > 0:
#         for i in range(num):
#             feat = input(f"Enter feature {i+1}: ") # Take input one by one 
#             features.append(feat) # Add to list

#     car = CarFeature(brand, features)
#     all_cars.append(car) # Add the car object to the list


#     more = input("Do you want to add another car? (yes/no): ").strip().lower()
#     if more != 'yes':
#         break


# # Display all car info after loop ends
# print("\n---Summary of Entered Cars---")
# for i, car in enumerate(all_cars, start=1):
#     print(f"\nCar {i}:")
#     car.display_brand()
#     car.display_feature()

# # -------------------------------------------------------------


# # Basic ATM Class

# class ATM:
#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew ₹{amount}. Remaining balance: ₹{self.balance}")
#         else:
#             print("Insufficient balance!")

#     def check_balance(self):
#         print(f"Current balance: ₹{self.balance}")

# # ✅ Testing the class
# my_atm = ATM(1000)
# my_atm.deposit(500)
# my_atm.withdraw(700)
# my_atm.withdraw(1000)   # edge case
# my_atm.check_balance()




