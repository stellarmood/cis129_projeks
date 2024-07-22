#jp feddick cis129
def write_grades_to_file(filename):
    with open(filename, 'w') as file:
        print("Enter grades (enter -1 to stop):")
        while True:
            grade_str = input("Enter grade (-1 to stop): ")
            if grade_str == '-1':
                break
            try:
                grade = float(grade_str)
                file.write(f"{grade}\n")
            except ValueError:
                print("Invalid input. Please enter a valid grade.")

    print(f"Grades have been written to {filename}.")

# Example usage
filename = 'grades.txt'
write_grades_to_file(filename)

#9.2
# Read grades from grades.txt file and calculate total, count, and average

filename = 'grades.txt'

# Read grades from file
grades = []
with open(filename, 'r') as file:
    for line in file:
        try:
            grade = float(line.strip())  # Convert line to float
            grades.append(grade)
        except ValueError:
            print(f"Skipping invalid entry: {line.strip()}")

# Display individual grades
print("Individual Grades:")
for grade in grades:
    print(grade)

# Calculate total, count, and average
total = sum(grades)
count = len(grades)
average = total / count if count > 0 else 0

# Display total, count, and average
print("\nTotal:", total)
print("Count:", count)
print("Average:", average)

#9.3
import csv

def write_grades_to_csv(filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])  # Write header row
        while True:
            first_name = input("Enter student's first name (or type 'quit' to exit): ")
            if first_name.lower() == 'quit':
                break
            last_name = input("Enter student's last name: ")
            try:
                exam1 = int(input("Enter exam 1 grade: "))
                exam2 = int(input("Enter exam 2 grade: "))
                exam3 = int(input("Enter exam 3 grade: "))
                writer.writerow([first_name, last_name, exam1, exam2, exam3])
            except ValueError:
                print("Invalid input. Please enter integer grades.")

    print(f"Student grades have been written to {filename}.")

# Example usage
filename = 'grades.csv'
write_grades_to_csv(filename)

