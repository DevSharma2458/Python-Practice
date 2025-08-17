# try:
#     x = int(input('Input a integer: '))
#     print(x)
# except ValueError:
#     print('Value not an integer')
# finally:
#     print('Execution completed')




# try:
#     age = int(input("Enter Your Age: "))
#     print("Your age  is: ", age)
# except ValueError:
#     print("Please Enter a valid Age")
# finally:
#     print("Thank you for using the program")    



while True:
    try:
        age = int(input("Enter your age: "))
        if age <= 0:
            print("❌ Age must be a positive number.")
        else:
            print("✅ Your age is:", age)
            break
    except ValueError:
        print("❌ Please enter a valid number.")
    except KeyboardInterrupt:
        print("\n⚠️ Input cancelled by user.")
        break
    finally:
        print("📌 This message runs after each attempt.\n")

print("✅ Program Ended. Thank you!")


























































































