"""
Scenario
Your task is to write a function able to input integer values and to check if they are within a specified range.

The function should:

accept three arguments: a prompt, a low acceptable limit, and a high acceptable limit;
if the user enters a string that is not an integer value, the function should emit the message Error: wrong input, and ask the user to input the value again;
if the user enters a number which falls outside the specified range, the function should emit the message Error: the value is not within permitted range (min..max) and ask the user to input the value again;
if the input value is valid, return it as a result.
Test data
Test your code carefully.

This is how the function should react to the user's input:

Enter a number from -10 to 10: 100
Error: the value is not within permitted range (-10..10)
Enter a number from -10 to 10: asd
Error: wrong input
Enter number from -10 to 10: 1
The number is: 1
"""

# functions prompts user for input then checks if the input is an integer and between the min and max values provided
# in the function call
def read_int(prompt, min, max):
    userInput = input(prompt)
    isUserInputValid = False
    while isUserInputValid == False:
        try:
# try to cast string to int
            userInput = int(userInput)
            assert userInput > min and userInput < max
            isUserInputValid = True
# except branch for when casting to int raises and exception
        except ValueError:
            print("Error: wrong input")
            userInput = input(prompt)
# except branch for when asset statement raises and exception
        except AssertionError:
            print("Error: the value is not within permitted range")
            userInput = input(prompt)

    return str(userInput)

v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
