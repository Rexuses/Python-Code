#Batuhan Beel
#20.08.2020
#Product of two matrix
import time
import random

while True:
    operator = input("Press 'w' for matrix multiplication,press 'e' for random matrix multiplication, press 'q' to finish.") # To determine which operator to use.
    if operator=="w":
        while True:
            try:
                first_matrix_row    = int(input("Please enter how many rows will be in the first matrix")) # The code that determines how many rows the first matrix has.
                first_matrix_column = int(input("Please enter how many columns will be in the first matrix")) # The code that determines how many column the first matrix has.
                first_matrix        = [[0 for x in range(first_matrix_column)] for y in range(first_matrix_row)] # To create the first matrix.

                for row_index in range(first_matrix_row):
                    for column_index in range(first_matrix_column):
                        first_matrix[row_index][column_index] = int(input("Please give value for {}.row {}.column".format(row_index+1,column_index+1))) #The part where we give the values​for the first matrix.

                second_matrix_row    =int(input("Please enter how many rows will be in the second matrix")) # The code that determines how many rows the second matrix has.
                second_matrix_column = int(input("Please enter how many columns will be in the second matrix"))  # The code that determines how many column the second matrix has.
                second_matrix = [[0 for x in range(second_matrix_column)] for y in range(second_matrix_row)] # To create the second matrix.

                for row_index in range(second_matrix_row):
                    for column_index in range(second_matrix_column):
                        second_matrix[row_index][column_index] = int(input("Please give value for {}.row {}.column".format(row_index+1,column_index+1))) # The part where we give the values​for the second matrix.
            except ValueError:
                print("Please enter number.") # Error message.
                continue
            result_matrix = [[0 for x in range(second_matrix_column)] for y in range(first_matrix_row)] # To create the result matrix.

            if first_matrix_column == second_matrix_row: # Determines whether matrix multiplication can be done.
                for row_index in range(len(first_matrix)): # The length of the first matrix (first matrix row) determines the row of the result matrix.
                    for column_index in range(len(second_matrix[0])): # The length of 0. index of the second matrix (column of the second matrix) determines the column of the result matrix.
                        for k in range(len(second_matrix)):
                            result_matrix[row_index][column_index] += first_matrix[row_index][k] *second_matrix[k][column_index] # Calculates the values of the result matrix.
                print("Calculating...")
                time.sleep(1.5)
                print("\n", "First Matrix=", first_matrix, "\n", "Second Matrix=", second_matrix)
                for result in result_matrix:
                    print(result)
            else:
                print("first matrixs column must be equal to the second matrixs row") # Matrix multiplication cannot be done.
                print("try again")
                continue
            break
    if operator=="e":
        while True:
            try:
                first_matrix_row    = random.randint(0,6) # Randomly determines the row of the first matrix.
                first_matrix_column = random.randint(0,6) # Randomly determines the column of the first matrix.
                first_matrix        = [[0 for x in range(first_matrix_column)] for y in range(first_matrix_row)] # To create the first matrix.

                for row_index in range(first_matrix_row):
                    for column_index in range(first_matrix_column):
                        first_matrix[row_index][column_index] = random.randint(0,6) # Give random values to the first matrix.

                second_matrix_row    = random.randint(0,6)
                second_matrix_column = random.randint(0,6)
                second_matrix        = [[0 for x in range(second_matrix_column)] for y in range(second_matrix_row)] # To create the second matrix.

                for row_index in range(second_matrix_row):
                    for column_index in range(second_matrix_column):
                        second_matrix[row_index][column_index] = random.randint(0,6) # Give random values to the second matrix.
            except ValueError:
                print("Please enter number.") # Error message.
                continue
            result_matrix = [[0 for x in range(second_matrix_column)] for y in range(first_matrix_row)]

            if first_matrix_column == second_matrix_row: # Determines whether matrix multiplication can be done.
                for row_index in range(len(first_matrix)): # The length of the first matrix (first matrix row) determines the row of the result matrix.
                    for column_index in range(len(second_matrix[0])): # The length of 0. index of the second matrix (column of the second matrix) determines the column of the result matrix.
                        for k in range(len(second_matrix)):
                            result_matrix[row_index][column_index] += first_matrix[row_index][k] *second_matrix[k][column_index] # Calculates the values of the result matrix.
                print("Calculating...")
                time.sleep(1.5)
                print("\n","First Matrix=",first_matrix,"\n","Second Matrix=",second_matrix)
                for result in result_matrix:
                    print(result)
            else:
                continue
            break
    elif operator=="q":
        print("Logging out")
        break #To exit the program
