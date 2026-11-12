# Student Marks, Percentage and Grade
name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))
total = 0
for i in range(1, n + 1):
    mark = float(input(f"Enter mark for Subject {i}: "))
    total += mark
    percentage = total / n
    if percentage >= 90:
        grade = "A+"
        performance = "Outstanding"
    elif percentage >= 80:
        grade = "A"
        performance = "Excellent"
    elif percentage >= 70:
        grade = "B"
        performance = "Very Good"
    elif percentage >= 60:
        grade = "C"
        performance = "Good"
    elif percentage >= 50:
        grade = "D"
        performance = "Average"
    else:
        grade = "F"
        performance = "Needs Improvement"
print("\n--- Academic Performance ---")
print("Student Name :", name)
print("Total Marks :", total)
print("Percentage :", round(percentage, 2), "%")
print("Grade :", grade)
print("Performance :", performance)

#electricity billig system
def calculate_bill(units):
    if units <= 100:
        return units * 1.50
    elif units <= 200:
        return (100 * 1.50) + ((units - 100) * 2.50)
    elif units <= 500:
        return (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)
    else:
        return (100 * 1.50) + (100 * 2.50) + (300 * 4.00) + ((units - 500) * 6.00)


def process_billing_system():
    while True:
        try:
            n = int(input("Enter number of customers: "))
            if n > 0:
                break
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    for i in range(1, n + 1):
        print(f"\nCustomer {i}")
        name = input("Enter customer name: ").strip()

        while True:
            try:
                units = float(input("Enter units consumed: "))
                if units >= 0:
                    break
                print("Units consumed cannot be negative.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        bill = calculate_bill(units)

        print("\n" + "=" * 30)
        print("      ELECTRICITY BILL        ")
        print("=" * 30)
        print(f"Customer Name : {name}")
        print(f"Units         : {units:.2f}")
        print(f"Bill Amount   : Rs. {bill:.2f}")
        print("=" * 30)


if __name__ == "__main__":
    process_billing_system()

# Menu-Driven Student Information System
students = {}
def add_student():
     roll = input("Enter Roll No: ")
     name = input("Enter Name: ")
     dept = input("Enter Department: ")
     students[roll] = {"Name": name, "Department": dept}
     print("Student added successfully.")
    
def view_students():
     if not students:
         print("No student records found.")
         return
     print("\n--- Student Records ---")
    for roll, data in students.items():
         print("Roll No:", roll,"| Name:", data["Name"],"| Department:", data["Department"])
        
def search_student():
     roll = input("Enter Roll No to search: ")
     if roll in students:
         print(students[roll])
     else:
         print("Student not found.")
         
def delete_student():
     roll = input("Enter Roll No to delete: ")
     if roll in students:
         del students[roll]
         print("Student deleted successfully.")
    else:
         print("Student not found.")
while True:
     print("\n1. Add Student")
     print("2. View Students")
     print("3. Search Student")
     print("4. Delete Student")
     print("5. Exit")
     choice = input("Enter your choice: ")
     if choice == "1":
         add_student()
     elif choice == "2":
         view_students()
     elif choice == "3":
         search_student()
     elif choice == "4":
        delete_student()
     elif choice == "5":
         print("Exiting...")
         break
     else:
         print("Invalid choice.")
         
# Student Record Management with List, Tuple, Dictionary and CSV
import csv
students = [
 {"RollNo": "101", "Name": "Anitha", "Department": "CSE", "Mark": 86},
 {"RollNo": "102", "Name": "Bala", "Department": "CSE", "Mark": 91},
 {"RollNo": "103", "Name": "Chitra", "Department": "ECE", "Mark": 78}
]

# Tuple example: fixed course details
course = ("Python", 4)
print("Course Tuple:", course)

# Write text file
with open("students.txt", "w") as file:
     for student in students:
        file.write(str(student) + "\n")
         
# Write CSV file
with open("students.csv", "w", newline="") as file:
     fields = ["RollNo", "Name", "Department", "Mark"]
     writer = csv.DictWriter(file, fieldnames=fields)
     writer.writeheader()
     writer.writerows(students)

# Read CSV file
print("\n--- Records from CSV ---")
with open("students.csv", "r") as file:
     reader = csv.DictReader(file)
     for row in reader:
         print(row["RollNo"], row["Name"], row["Department"], row["Mark"])
