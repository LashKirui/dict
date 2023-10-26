student_scores = {
    "Hillary": 89,
    "Joseph": 57,
    "Harry": 98,
    "Jane": 87,
    "Rony": 74,
}

student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectation"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(f"Students grades: {student_grades}")
