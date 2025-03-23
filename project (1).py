print("Hello, user!")  # Say hi to the user

students_names = []
number_of_students = input("Enter the number of students: ")  # Ask the user to input the number of students

name = input("Enter the student's name: ")  # Ask the user to input the student's name
name = name.lower()  # Convert name to lowercase for case-insensitive comparison

subjects = ["Math", "Science", "English"]  # Subjects
school = input("Enter the school name: ")  # Name of the school

try:
    degree1 = int(input("Enter the degree for Math: "))  # Degree for Math
    degree2 = int(input("Enter the degree for Science: "))  # Degree for Science
    degree3 = int(input("Enter the degree for English: "))  # Degree for English
except ValueError:  # Handle non-numeric input
    print("Invalid input! Please enter numbers only.")
    exit()  # Exit the program if invalid input is given

def calc_average():  # Function to calculate the average
    average = (degree1 + degree2 + degree3) / 3  # Calculate the average of the three degrees
    print(f"Average: {average:.2f}")  # Print the average with 2 decimal places
    if average > 50:
        print("This student has passed.")
    else:
        print("This student has not passed.") 

calc_average()  # Call the function

def find_student():  # Function to find the student
    name1 = input("Enter the student's name to search: ")  
    name1 = name1.lower()  # Convert to lowercase for case-insensitive comparison
    
    if name1 == name:  
        calc_average()  # Call the function to show the student's result
    else:
        print("This name is not in the system.")  # This name is not found

find_student()  # Call the function








