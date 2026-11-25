"""Lavanya Tripathi: CSV storage and student record CRUD operations."""
import csv
import os
from config import FILE_NAME, SUBJECTS, CSV_HEADERS


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='', encoding='utf-8') as file:
            csv.writer(file).writerow(CSV_HEADERS)


def load_data():
    students = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r', newline='', encoding='utf-8') as file:
            for row in csv.DictReader(file):
                if row.get('Roll_No') and all(row.get(subject) is not None for subject in SUBJECTS):
                    students.append(row)
    return students


def save_student(record):
    initialize_file()
    if os.path.getsize(FILE_NAME) > 0:
        with open(FILE_NAME, 'rb+') as file:
            file.seek(-1, os.SEEK_END)
            if file.read(1) not in (b'\n', b'\r'):
                file.write(b'\n')
    with open(FILE_NAME, 'a', newline='', encoding='utf-8') as file:
        csv.writer(file).writerow(record)


def save_all_students(students):
    with open(FILE_NAME, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(CSV_HEADERS)
        for student in students:
            writer.writerow([student['Roll_No'], student['Name']] + [student[sub] for sub in SUBJECTS])


def _get_marks(prompt_prefix=''):
    labels = ['Python', 'Digital Design', 'Maths', 'Web Dev']
    marks = [float(input(f'{prompt_prefix}Enter {label} Marks (0-100): ')) for label in labels]
    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError('Marks must be between 0 and 100.')
    return marks


def add_new_student():
    print('\n--- ADD NEW STUDENT RECORD ---')
    students = load_data()
    roll_no = input('Enter Roll Number (e.g., S121): ').strip().upper()
    if not roll_no:
        print('[Error] Roll Number cannot be empty.')
        return
    if any(student['Roll_No'].upper() == roll_no for student in students):
        print(f'[Error] Roll Number {roll_no} already exists!')
        return
    name = input('Enter Student Name: ').strip().title()
    if not name:
        print('[Error] Name cannot be empty.')
        return
    try:
        marks = _get_marks()
        save_student([roll_no, name] + marks)
        print(f'[Success] Record for {name} ({roll_no}) saved to {FILE_NAME}!')
    except ValueError as error:
        print(f'[Error] {error}')


def update_student_marks():
    print('\n--- UPDATE STUDENT MARKS ---')
    students = load_data()
    roll_no = input('Enter Roll Number to update: ').strip().upper()
    for student in students:
        if student['Roll_No'].upper() == roll_no:
            try:
                marks = _get_marks('New ')
                for subject, mark in zip(SUBJECTS, marks):
                    student[subject] = mark
                save_all_students(students)
                print(f"[Success] Marks updated for {student['Name']}!")
            except ValueError as error:
                print(f'[Error] {error}')
            return
    print(f'[Error] Roll Number {roll_no} not found.')


def view_all_students():
    from parth_grading import calculate_metrics
    students = load_data()
    if not students:
        print('\n[Info] No records found in the database.')
        return
    print('\n' + '=' * 105)
    print(f"{'Roll':<6} | {'Name':<10} | {'Py':<5} | {'DD':<5} | {'Math':<5} | {'Web':<5} | {'Total':<7} | {'Avg %':<7} | {'Grade':<5} | {'Status':<6} | Remark")
    print('=' * 105)
    for student in students:
        total, avg, grade, status, remark = calculate_metrics(student)
        marks = [float(student[sub]) for sub in SUBJECTS]
        print(f"{student['Roll_No']:<6} | {student['Name']:<10} | {marks[0]:<5.0f} | {marks[1]:<5.0f} | {marks[2]:<5.0f} | {marks[3]:<5.0f} | {total:<7.0f} | {avg:<6.2f}% | {grade:<5} | {status:<6} | {remark}")
    print('=' * 105)


def search_student():
    from parth_grading import calculate_metrics
    students = load_data()
    roll_no = input('\nEnter Roll Number to search (e.g., S101): ').strip().upper()
    for student in students:
        if student['Roll_No'].upper() == roll_no:
            total, avg, grade, status, remark = calculate_metrics(student)
            print('\n--- STUDENT REPORT CARD ---')
            print(f"Roll Number    : {student['Roll_No']}")
            print(f"Name           : {student['Name']}")
            for subject in SUBJECTS:
                print(f'{subject:<15}: {student[subject]}')
            print('-' * 30)
            print(f'Total Marks    : {total:.0f} / 400')
            print(f'Average / %    : {avg:.2f}%')
            print(f'Grade          : {grade}')
            print(f'Final Status   : {status}')
            print(f'Teacher Remark : {remark}')
            print('-' * 30)
            return
    print(f"[Error] Student with Roll Number '{roll_no}' not found.")
