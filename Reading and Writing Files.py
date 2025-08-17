# coun_file = open('Countries.txt', 'r')
# print(coun_file.readable())
# print(coun_file.readlines()[3])
# coun_file.seek(0)  # Reset file pointer to the beginning
# print(coun_file.read())
# coun_file.seek(0)

# for lines in coun_file:
#     print(lines)
# coun_file.close()



# agar mai yaha file name kuch aur dalunga to dusri file create ho jayegi
# coun_file = open('Countries.txt', 'w') # w use karoge to purani file se data delete ho jayega
# coun_file = open('Countries.txt', 'a') # a use karoge to purani file se data delete nahi hoga
# coun_file.write('\nNew Zealand')  # Write a new line to the file
# coun_file.close()  # Close the file to save changes



# #Creating new python file and printing something in that file
# new_file = open('NewFile.py', 'w')
# new_file.write('print("Hello, this is a new file!")\n')
# new_file.close()

 
# Sports_file = open('Sports.txt', 'r')
# print(Sports_file.read()) 

# Sports_file.seek(0)  # Reset file pointer to the beginning

# for Sports in Sports_file:
#     print(Sports.strip())



# # With Statement automatically closes the file after the block of code is executed
# # This is a better practice than manually closing the file
# with open('Sports.txt', 'r') as Sports_file:
#     print(Sports_file.read())

#     Sports_file.seek(0)

#     for sport in Sports_file:
#         print(sport.strip())


# #File create kari
# with open('example.txt', 'w') as file:
#     file.write("Hello, World!\n")
#     file.write("This is line 2. \n")

# # Append to the file
# with open('example.txt', 'a') as file:
#     file.write("\n This is a new append line.")

# # Writing the list of countries to a file deleting old data
# # Writing multiple lines using writelines()
# lines = ["India\n", "Australia\n", "Brazil\n"]
# with open('countries.txt', 'w') as file:
#     file.writelines(lines)


# # Reading the file line by line with error handling
# try:
#     with open('countries.txt', 'r') as file:
#         for line in file:
#             print(line.strip())
# except FileNotFoundError:
#     print("File not found. Please check the filename")



# #If File Doesn't Exist - Create and Write
# filename = 'newfile.txt'
# try:
#     with open(filename, 'r') as f:
#         print(f.read())
# except FileNotFoundError:
#     with open(filename, 'w') as f:
#         f.write("File Created automatically\n")
#     print(f"{filename} created and written to. ")


# #Combined Input plus file writing practice
# with open('user_input.txt', 'w') as file:
#     name = input("Enter your name: ")
#     age = input("Enter your age: ")
#     file.write(f"Name: {name}\n")
#     file.write(f"Age: {age}\n")














































































