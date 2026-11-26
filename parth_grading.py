"""Parth Chauhan: marks calculation, grading, and pass/fail engine."""
from config import SUBJECTS


def calculate_metrics(student):
    """Return (total, average, grade, status, remark) for a student record."""
    marks = [float(student[subject]) for subject in SUBJECTS]
    total = sum(marks)
    average = total / len(SUBJECTS)

    # A student fails if any one subject is below 40.
    status = 'Fail' if any(mark < 40 for mark in marks) else 'Pass'
    if status == 'Fail':
        return total, average, 'F', status, 'Better luck next time'

    if average >= 90:
        grade = 'A+'
    elif average >= 80:
        grade = 'A'
    elif average >= 70:
        grade = 'B'
    elif average >= 60:
        grade = 'C'
    elif average >= 50:
        grade = 'D'
    else:
        grade = 'E'
    return total, average, grade, status, 'Good'
