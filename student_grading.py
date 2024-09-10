student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for student_name in student_scores:
    if student_scores[student_name] <= 70:
      student_grades[student_name]="Fail"
    elif student_scores[student_name] >= 91:
        student_grades[student_name]="Outstanding"
    elif student_scores[student_name] >= 81:
      student_grades[student_name]="Exceeds Expectations"
    elif student_scores[student_name] >= 71:
      student_grades[student_name]="Acceptable"
    
for student_finish in student_grades:
    print(f"{student_finish} : {student_grades[student_finish]}")
    