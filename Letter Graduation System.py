#Batuhan Beel 180403031
#14.08.2020
#Letter Graduation System

print("*****************************\n\nWelcome To Letter Graduation System\n\n*****************************")
while True:
    try:
        print("Press 'q' to Log Out of the System.")
        operator = input("Enter Your Midterm Grade") # To determine which operator to use.
        if operator == "q":
            print("You Have Logged Out of the System.")
            break # To exit the program.
        elif float(operator) >= 0 and float(operator) <= 100:
            operator = float(operator) # To convert string to float
            final    = float(input("Enter Your Final Grade:"))
            if final >= 0 and final <= 100:
                GPA = (operator * 0.4) + (final * 0.6)
                if GPA <= 100 and GPA >= 90:
                    print("Your Letter Grade:AA")
                elif GPA < 90 and GPA >= 85:
                    print("Your Letter Grade:BA")
                elif GPA < 85 and GPA >= 75:
                    print("Your Letter Grade:BB")
                elif GPA < 75 and GPA >= 70:
                    print("Your Letter Grade:CB")
                elif GPA < 70 and GPA >= 60:
                    print("Your Letter Grade:CC")
                elif GPA < 60 and GPA >= 55:
                    print("Your Letter Grade:DC")
                elif GPA < 55 and GPA >= 50:
                    print("Your Letter Grade:DD")
                elif GPA < 40 and GPA >= 50:
                    print("Your Letter Grade:FD")
                else:
                    print("Your Letter Grade:FF")
            else:
                print("Please Enter Correctly.") # To warn you when wrongly entered.
        else:
            print("Please Enter Correctly.") # To warn you when wrongly entered.
    except ValueError:
        print("Please Enter Correctly.") # Error message.
