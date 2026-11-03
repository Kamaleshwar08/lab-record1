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
