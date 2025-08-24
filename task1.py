#Taking input from the user
num = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#Performing operations
additional = num + num2
subtraction = num - num2
multiplication = num * num2
division = num / num2 if num2 != 0 else 0
"Undifined (Division by zero)"

#Displaying Results
print("addition:", additional)
print("subtraction:", subtraction)
print("multiplication:", multiplication)
print("division:", division)