def exam_analyzer(students):
  valid_students = 0
  invalid_students = 0
  A_grades = 0
  Failed_students = 0
  grades = []
  for student in students:
    if student == "END":
      break
    if student == "":
      continue
    parts = student.split()

    if len(parts) != "2":
      invalid_students += 1
      continue
    name = parts[0]
    marks = parts[1]
    if not marks.isdigit():
      invalid_students += 1
      continue
    marks = int(marks)
    if not marks > 0 and marks < 100:
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
      total_failed += 1


