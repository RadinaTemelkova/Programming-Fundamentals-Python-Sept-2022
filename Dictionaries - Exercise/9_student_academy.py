number_of_rows = int(input())
students_and_avg_grades = {}
not_very_good_avg_grade = True
for x in range(number_of_rows):
    student_name = input()
    grade = float(input())
    if student_name not in students_and_avg_grades.keys():
        students_and_avg_grades[student_name] = []
    students_and_avg_grades[student_name].append(grade)

for key, value in students_and_avg_grades.items():
    current_student_avg_grade = sum(value) / len(value)

    if current_student_avg_grade < 4.50:
        students_and_avg_grades[key] = not_very_good_avg_grade
    else:
        students_and_avg_grades[key] = current_student_avg_grade

for key, value in students_and_avg_grades.items():
    if value != not_very_good_avg_grade:
        print(f"{key} -> {value:.2f}")

