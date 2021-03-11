#Batuhan Beel 180403031
#06.00.2020
#Fibonacci

def Fibonacci():
    while True:
            operator    = input("Press 'q' to finish.\nPlease enter the place of fibonacci number you want : ")  # To determine which operator to use.
            if operator == "q":
                print("Logging out")
                break  # To exit the program
            else:
                try:
                    operator=int(operator) # To convert integer if is possible.
                    if operator<1 : # To prevent minus and zero.
                        print("Please enter a value greater than 0") # Warning message.
                    else:
                        new_term        = 0
                        first_term      = 1
                        second_term     = 1
                        fibonacci_list  = [first_term, second_term]
                        desired_list    = []
                        i               = 0
                        while i <operator:
                            new_term    = first_term+second_term
                            first_term  = second_term # Converts 1st term to 2nd term.
                            second_term = new_term # Converts 2nd term into new term.
                            fibonacci_list.append(new_term) # To add Fibonacci values into fibonacci list.
                            i+=1
                        for i in range(operator):
                            desired_list.append(fibonacci_list[i]) # To show Fibonacci values in the Fibonacci list we want.
                        print(desired_list)
                except ValueError:
                    print("Please press 'q' or enter integer number.")  # Error message.
                    print("*****************************************")
                    continue
                except IndexError:
                    print("Please enter integer number between(0-51).")  # Error message.
                    print("*****************************************")
                    continue
print(Fibonacci())
