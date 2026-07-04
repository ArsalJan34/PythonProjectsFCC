def exam_analyzer(students):
  valid_students = 0
  invalid_students = 0
  A_grades = 0
  failed_students = 0
  grades = []
  for student in students:
    if student == "END":
      break
    if student == "":
      continue
    parts = student.split()

    if len(parts) != 2:
      invalid_students += 1
      continue
    name = parts[0]
    marks = parts[1]
    if not marks.isdigit():
      invalid_students += 1
      continue
    marks = int(marks)
    if marks < 0 or marks > 100:
      invalid_students += 1
      continue
    valid_students += 1
    if marks >= 90:
      grade = "A"
      A_grades += 1
    elif marks >= 80:
      grade = "B"
    elif marks >= 70:
      grade = "C"
    elif marks >= 60:
      grade = "D"
    else:
      grade = "F"
      failed_students += 1

    grades.append(f"{name} : {grade}")
    print(f"\nLetters in {name}: ")
    for letter in name:
      print(letter)

  return [
    valid_students,
    invalid_students,
    A_grades,
    failed_students,
    grades
  ]
students = []
num = int(input("How many student records do you want to enter? : "))
for i in range(num):
  record = input(f"Enter record {i+1} (Name Marks): ")
  students.append(record)
result = exam_analyzer(students)
print("\n============ Report ============ ")
print(f"Valid Students : {result[0]}" )
print(f"Invalid Students : {result[1]}" )
print(f"A Grades : {result[2]}")
print(f"Failed Students  : {result[3]}")

print("\n Grades : ")
for grade in result[4]:
  print(grade)
