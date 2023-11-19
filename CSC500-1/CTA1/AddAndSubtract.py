def my_function(tempNum, text, method): #Function to Check if a given value is an integer or not
  if not tempNum.isnumeric():
	 	tempNum = input('Enter a valid integer - '+ text+' to '+ method+' : ')
  if not tempNum.isnumeric(): #recursive call to check given number is an integer or not
    tempNum=my_function(tempNum, text, method) 
  return int(tempNum)

print('Enter number 1 to add/subtract : ', end=' ') #Ask User to enter value 1
text = "Number 1" #set text - input Values for function
method = "add/subtract" #set method - input Values for function
num1 = my_function(input(), text, method) #Call function to check entered value is an integer
print('Enter number 2 to add/subtract : ', end=' ') #Ask User to enter value 2
text = "Number 2" #reset text - input Values for function
num2 = my_function(input(), text, method) #Call function to check entered value is an integer
_total = num1+ num2 #Add
print('Sum of', end=' ') # Print total
print(num1, end=' and ')
print(num2, end=' = ')
print(_total)
_difference = num1- num2 #Subtract
print('Difference of', end=' ') #Print Difference
print(num1, end=' and ')
print(num2, end=' = ')
print(_difference)
#End

