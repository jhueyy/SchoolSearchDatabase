# School Search DBMS
Description: This program simulates a simple DBMS with Python. Given a text-file, with data format:

`<StLastName, StFirstName, Grade, Classroom, Bus, GPA, TLastName, TFirstName>`

Goal: we want to be able to query the database for these types of data.

## Commands Supported:

- **S[tudent]: `<lastname>` [B[us]]** - Search for a student by last name. Optionally, show the bus route instead of other details.
- **T[eacher]: `<lastname>`** - Search for all students taught by a teacher.
- **B[us]: `<number>`** - Search for all students riding a numbered bus route.
- **G[rade]: `<number>` [H[igh]|L[ow]]** - Search for all students in a grade or find the student with the highest/lowest GPA.
- **A[verage]: `<number>`** - Calculate the average GPA for a specific grade.
- **I[nfo]** - Display the number of students in each grade.
- **Q[uit]** - Quit the program.

## Key:

- Square brackets `[]` indicate optional components.
- Angle brackets `<>` indicate required inputs.

## Examples of Valid Commands:

- `S`
- `Student COOKUS`
- `T MIGLER`
- `G 2 H`
- `Quit`

## How to Run the Program

1. Ensure you have **Python 3.x** installed on your machine.
2. Place the `students.txt` file in the same directory as the `schoolsearch.py` script if it is not already present.
3. Open a terminal and navigate to the directory containing the program files.
4. Run the program using the following command:
   ```bash
   python3 schoolsearch.py


