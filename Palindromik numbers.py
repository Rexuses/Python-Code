#Batuhan Beel
#30.08.2020
#Find the palindromik numbers

list=list() # Blank list to add palindromic numbers
for i in range(1000):
    i=str(i) # We convert it to string to get the inverse of the variable
    if i==i[::-1]:
        list.append(i)
print(list)

