"""Diksha Mudgil: ranking, performer segmentation, and subject analytics."""
from config import SUBJECTS
from lavanya_records import load_data
from parth_grading import calculate_metrics


def high_low_performers():
    students = load_data()
    if not students:
        print('\n[Info] No records available for analysis.')
        return
    high_list, low_list, ranked_list = [], [], []
    for student in students:
        _, average, _, status, _ = calculate_metrics(student)
        ranked_list.append((average, student['Roll_No'], student['Name'], status))
        if average >= 85 and status == 'Pass':
            high_list.append(f"{student['Name']} ({average:.2f}%)")
        elif average < 50 or status == 'Fail':
            low_list.append(f"{student['Name']} ({average:.2f}% - {status})")

    # Sort passing students above failing students, then by highest average
    ranked_list.sort(key=lambda item: (item[3] == 'Pass', item[0]), reverse=True)

    print('\n--- CLASS RANKING (TOP 5) ---')
    for rank, item in enumerate(ranked_list[:5], start=1):
        print(f'Rank {rank}: {item[2]} ({item[1]}) - {item[0]:.2f}% [{item[3]}]')
    print('\n--- HIGH PERFORMERS (Avg >= 85% & Pass) ---')
    print(', '.join(high_list) if high_list else 'None')
    print('\n--- LOW PERFORMERS (Avg < 50% or Fail) ---')
    print(', '.join(low_list) if low_list else 'None')


def subject_wise_analysis():
    students = load_data()
    if not students:
        print('\n[Info] No records available for subject analysis.')
        return
    print('\n--- SUBJECT-WISE PERFORMANCE ANALYSIS ---')
    print('-' * 75)
    print(f"{'Subject':<16} | {'Class Avg':<10} | {'Highest':<20} | {'Lowest':<20}")
    print('-' * 75)
    for subject in SUBJECTS:
        marks = [(float(student[subject]), student['Name']) for student in students]
        subject_average = sum(mark for mark, _ in marks) / len(marks)
        highest, lowest = max(marks), min(marks)
        high_str = f"{highest[0]:.0f} ({highest[1]})"
        low_str = f"{lowest[0]:.0f} ({lowest[1]})"
        print(f"{subject:<16} | {subject_average:<9.2f}% | {high_str:<20} | {low_str:<20}")
    print('-' * 75)
    
