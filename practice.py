from typing import List


def grade(average_score: int):
    if average_score >= 90:
        grade_letter = "A"
    elif average_score >= 90:
        grade_letter = "B"
    elif average_score >= 80:
        grade_letter = "C"
    elif average_score >= 60:
        grade_letter = "D"
    else:
        grade_letter = "F"
    return grade_letter


def average(exam_scores: List[int]):
    total = sum(exam_scores)
    avg = total / len(exam_scores)
    return avg


def pass_student(exam_scores: List[int]):
    passed = True
    # check if student had a pass mark of 60 and above
    for score in exam_scores:
        if score < 60:
            passed = False
    return passed


def process_student_grades(exam_scores: List[int]):
    avg = average(exam_scores)
    grade_letter = grade(int(avg))
    passed = pass_student(exam_scores)
    student_grades_data = {
        "average_grade": avg,
        "grade_letter": grade_letter,
        "all_grade_pass": passed
    }
    return student_grades_data


print(process_student_grades([80]))
