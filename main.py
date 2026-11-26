"""Lavanya: integrated command-line menu for the team project."""
from lavanya_records import (
    initialize_file, view_all_students, add_new_student,
    update_student_marks, search_student,
)
from diksha_analytics import high_low_performers, subject_wise_analysis


def main_menu():
    initialize_file()
    while True:
        print('\n==============================================')
        print('   STUDENT PERFORMANCE ANALYSIS SYSTEM')
        print('==============================================')
        print('1. View All Student Records (Table View)')
        print('2. Add New Student Record')
        print('3. Update Existing Student Marks')
        print('4. Search Individual Student Report Card')
        print('5. Class Ranking & High/Low Performers')
        print('6. Subject-Wise Performance Statistics')
        print('7. Exit')
        print('==============================================')
        choice = input('Select an option (1-7): ').strip()
        actions = {
            '1': view_all_students,
            '2': add_new_student,
            '3': update_student_marks,
            '4': search_student,
            '5': high_low_performers,
            '6': subject_wise_analysis,
        }
        if choice == '7':
            print('Saving data and exiting system. Goodbye!')
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print('[Error] Invalid option! Please enter a number between 1 and 7.')


if __name__ == '__main__':
    main_menu()
