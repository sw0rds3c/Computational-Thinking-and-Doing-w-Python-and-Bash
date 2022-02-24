''' SIMPLE CALCULATOR by Mike S. -- 02/11/2022'''

# adding two numbers
def add(x, y):
    return x + y

# subtracting two numbers
def subtract(x, y):
    return x - y

# multiplying two numbers
def multiply(x, y):
    return x * y

# dividing two numbers
def divide(x, y):
    return x / y

# starts loop
while True:

    # display the choice of operations available
    print("Select Operation.\n")
    print("1.Add\n")
    print("2.Subtract\n")
    print("3.Multiply\n")
    print("4.Divide\n")

    # take input from the user
    userChoice = input("Please enter your choice of mathematical operations \n--> [1 , 2 , 3 , or 4]: ")

    # check if the users choice is one of the four options
    if userChoice in ('1', '2', '3', '4'):
        num1 = float(input("Please enter the first number to work with: "))
        num2 = float(input("Please enter the second number to work with: "))

        if userChoice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif userChoice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif userChoice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif userChoice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if the user would like to exit the menu
        # break the while loop if the response is Y or y
        userExit = input("To exit the program, please enter the 'Y' key: ")
        if userExit.upper() == "Y":
          break
    
    else:
        print("Something went wrong (Invalid Input?)")