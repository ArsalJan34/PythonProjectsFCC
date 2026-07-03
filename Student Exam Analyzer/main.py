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



