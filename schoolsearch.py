'''
Jake Huey
Professor Migler
CSC 365
January 15th, 2025

This program simulates a simple DBMS with python. Given a text-file, with data format:

    StLastName, StFirstName, Grade, Classroom, Bus, GPA, TLastName, TFirstName

We want to be able to query the database for these types of data

The types of commands are:
    • S[tudent]: <lastname> [B[us]]   - Search for a student by last name. Optionally, show bus route instead of other details
    • T[eacher]: <lastname>           - Search for all students taught by a teacher
    • B[us]: <number>                 - Search for all students riding a numbered bus route
    • G[rade]: <number> [H[igh]|L[ow]]- Search for all students in a grade or find the student with highest/lowest GPA
    • A[verage]: <number>             - Calculate the average GPA for a specific grade
    • I[nfo]                          - Display the number of students in each grade
    • Q[uit]                          - Quit the program
**Key:**
- Square brackets [] indicate optional components.
- Angle brackets <> indicate required inputs.

**Examples of Valid Commands:**
    S
    Student COOKUS
    T MIGLER
    G 2 H
    Quit
'''
class SchoolSearch:
    def __init__(self, filename):
        self.filename = filename
        self.students = self.load_students()
    
    def load_students(self):
        students = []
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    row = line.strip().split(',')
                    if len(row) != 8:
                        print("Error: Incorrect data format in students.txt")
                        exit(1)
                    try:
                        student = {
                            'StLastName': row[0],
                            'StFirstName': row[1],
                            'Grade': int(row[2]),
                            'Classroom': int(row[3]),
                            'Bus': int(row[4]),
                            'GPA': float(row[5]),
                            'TLastName': row[6],
                            'TFirstName': row[7]
                        }
                        students.append(student)
                    except ValueError:
                        print("Error: Invalid data type in students.txt")
                        exit(1)
        except FileNotFoundError:
            print("Error: students.txt file not found")
            exit(1)
        #print(students)
        return students

    def search_student(self, lastname, bus_info=False):
        results = []

        # Collect all students with the specified last name
        for student in self.students:
            if student['StLastName'] == lastname:
                results.append(student)

        # Display results based on whether the 'B' flag was used
        if len(results) == 0:
            print(f"No student found with last name '{lastname}'.")
        else:
            for student in results:
                if bus_info:  # R5: Print only bus route
                    print(f"{student['StLastName']}, {student['StFirstName']}: Bus Route {student['Bus']}")
                else:  # R4: Print full student information
                    print(f"{student['StLastName']}, {student['StFirstName']}: Grade {student['Grade']}, Classroom {student['Classroom']}, Teacher: {student['TFirstName']} {student['TLastName']}")


    def search_teacher(self, lastname):
        results = []
        for student in self.students:
            if student['TLastName'] == lastname:
                results.append(student)

        if len(results) == 0:
            print(f"No teacher found with last name '{lastname}'.")
        else:
            for student in results:
                print(student['StLastName'] + ", " + student['StFirstName'])

    def search_bus(self, bus_number):
        results = []
        for student in self.students:
            if student['Bus'] == bus_number:
                results.append(student)

        if len(results) == 0:
            print("No students found on bus route:", bus_number)
        else:
            for student in results:
                print(student['StLastName'] + ", " + student['StFirstName'] + ", Grade " + str(student['Grade']) + ", Classroom " + str(student['Classroom']))

    def search_grade(self, grade, high_low=None):
        results = []
        for student in self.students:
            if student['Grade'] == grade:
                results.append(student)

        if len(results) == 0:
            print("No students found in Grade:", grade)
        else:
            if high_low in ['H', 'High']:
                top_student = results[0]
                for student in results:
                    if student['GPA'] > top_student['GPA']:
                        top_student = student
                print("Highest GPA: " + top_student['StLastName'] + ", " + top_student['StFirstName'] + " with GPA " + str(top_student['GPA']) + ", Teacher: " + top_student['TFirstName'] + " " + top_student['TLastName'] + ", Bus Route: " + str(top_student['Bus']))
            elif high_low in ['L', 'Low']:
                lowest_student = results[0]
                for student in results:
                    if student['GPA'] < lowest_student['GPA']:
                        lowest_student = student
                print("Lowest GPA: " + lowest_student['StLastName'] + ", " + lowest_student['StFirstName'] + " with GPA " + str(lowest_student['GPA']) + ", Teacher: " + lowest_student['TFirstName'] + " " + lowest_student['TLastName'] + ", Bus Route: " + str(lowest_student['Bus']))
            else:
                for student in results:
                    print(student['StLastName'] + ", " + student['StFirstName'] + ", Classroom " + str(student['Classroom']) + ", Teacher " + student['TFirstName'] + " " + student['TLastName'])

    def average_gpa(self, grade):
        #results = []
        total_gpa = 0
        count = 0

        for student in self.students:
            if student['Grade'] == grade:
                total_gpa += student['GPA']
                count += 1

        if count == 0:
            print("No students found in Grade:", grade)
        else:
            avg_gpa = total_gpa / count
            print("Average GPA for Grade " + str(grade) + ": " + format(avg_gpa, ".2f"))

    def info(self):
        grade_count = {}
        for i in range(7):
            grade_count[i] = 0

        for student in self.students:
            grade_count[student['Grade']] += 1

        for grade in sorted(grade_count):
            print("Grade " + str(grade) + ": " + str(grade_count[grade]) + " Students")

    def print_invalid(self):
        print("Invalid command. Try again.")

    def run(self):
        while True:
            command = input("Enter command: ")
            parts = command.split()
            if not parts:
                continue
            if len(parts) == 1 and parts[0] not in ['Q', 'Quit', 'I', 'Info']:
                self.print_invalid()
                continue
            if parts[0] in ['Q', 'Quit']:
                break
            elif parts[0] in ['S', 'Student']:
                if len(parts) > 2 and parts[2] in ['B', 'Bus']:
                    self.search_student(parts[1], bus_info=True)
                else:
                    if len(parts) <= 2:
                        self.search_student(parts[1])
                    else:
                        self.print_invalid()
            elif parts[0] in ['T', 'Teacher']:
                if len(parts) < 3:
                    self.search_teacher(parts[1])
                else:
                    self.print_invalid()
            elif parts[0] in ['B', 'Bus']:
                if len(parts) < 3:
                    self.search_bus(int(parts[1]))
                else:
                    self.print_invalid()
            elif parts[0] in ['G', 'Grade']:
                if len(parts) > 2 and len(parts) <= 3:
                    #self.search_grade(int(parts[1]), parts[2])
                    if parts[2] in ['H', 'L', 'High', 'Low']:
                        self.search_grade(int(parts[1]), parts[2])
                    else:
                        self.print_invalid()
                else:
                    if len(parts) <= 2:
                        self.search_grade(int(parts[1]))
                    else:
                        self.print_invalid()
            elif parts[0] in ['A', 'Average']:
                if len(parts) <= 2:
                    self.average_gpa(int(parts[1]))
                else:
                    self.print_invalid()
            elif parts[0] in ['I', 'Info']:
                if len(parts) == 1:
                    self.info()
                else: 
                    self.print_invalid()
            else:
                self.print_invalid()

if __name__ == "__main__":
    school_search = SchoolSearch('students.txt')
    #school_search = SchoolSearch('fakestudents.txt')
    school_search.run()
