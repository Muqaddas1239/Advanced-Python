#Exception Handling in Python

#Exception handling is a way to handle runtime errors in a program so that the program does not suddenly stop

number = int(input("Enter a number: "))
print(10 / number)    #If our input is 0, ZeroDivisionError: division by zero

#so, to avoide this termination of program we use try and except 

try:
    number = int(input("Enter a number: "))
    print(10 / number)

except:
    print("Something went wrong!")   #Now if our input is not integer or 0 it prints except part and program doesnt stop


#   If we want to know the error we use a base class for built in exceptions Exception as:

try:
    number = int(input("Enter a number: "))
    print(10 / number)

except Exception as e:
    print("An error occurred:", e)

# else : only runs when there is no exception

try:
    number = int(input("Enter a number: "))
    result = 10 / number

except ZeroDivisionError:          #we can also use only subclasses of Exception class
    print("Cannot divide by zero.")

else:
    print("Answer is:", result)

#finally: finally runs whether an error happens or not

try:
    number = int(input("Enter a number: "))
    print(10 / number)

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Program finished.")

