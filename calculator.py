# Hello from the file!

# 1. Take in user input
# 2. Decide what operation to perform based on the input
# 3. Perform the operation
# 4. Give the answer to the operation
# 5. Ask if they want to perform another calculation
# If yes:
# 6. a. Repeat 1-5
# 6. b. Shut off the application



### PART ONE - Imports and Helper Functions ###
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Cannot divide by zero!"



### PART TWO - main() Definition ###
def main():
    appOn = True

    operations = {"+": add,
                  "-": subtract,
                  "*": multiply,
                  "/": divide}

    while appOn:
        print("Would you like to perform (another) operation? (y/n)")
        keepGoing = input("  --> ").lower()

        if keepGoing == "n" or keepGoing == "no":
            appOn = False
        else:
            print("Enter an equation")
            eqIn = input("  --> ").split(" ")
            
            result = float(eqIn[0])
            num = 0

            for i in range(len(eqIn)):
                if eqIn[i] in operations.keys():
                    num = float(eqIn[i+1])
                    result = operations[eqIn[i]](result, num)
                    if result == "Cannot divide by zero!":
                        break
                else:
                    continue

            print(result)



### PART THREE - main() Call ###
if __name__ == "__main__":
    main()
