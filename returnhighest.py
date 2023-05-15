user_string = input('Please enter five numbers separated by spaces:') #collect user numbers

array = user_string.split()  #get rid of white space forming string
array_integers = []
array_integers = [int(i) for i in array] #convert string items to integers
max_number = max(array_integers) #print the max number in list of integers




print(user_string)
print(array)
print(array_integers)
print(max_number)
