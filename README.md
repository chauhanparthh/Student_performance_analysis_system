# Student Performance Analysis System — Milestone 1

A CSV-based Python CLI project for student record management, marks calculation, grading, class ranking, performer segmentation, and subject-wise statistics.

## Team contribution and files

| Team member | Assigned work | File(s) |
|---|---|---|
| Lavanya Tripathi | Main structure, CSV and student records | `main.py`, `lavanya_records.py`, `config.py` |
| Parth Chauhan | Marks, grading and pass/fail | `parth_grading.py` |
| Diksha Mudgil | Ranking, high/low performers, subject analysis | `diksha_analytics.py` |
| Deepika | Documentation and presentation | `README.md` / project report |

## Run the complete project

Keep all `.py` files and `students.csv` in the same folder. From that folder run:

```bash
python main.py
```

No third-party packages are required. The program uses Python's standard library.

## Menu

1. View all student records
2. Add a student
3. Update marks
4. Search a report card
5. Top 5 ranking and high/low performers
6. Subject-wise statistics
7. Exit

## Grading rules

- Marks are on a 0–100 scale.
- Any subject score below 40 means Fail and grade F.
- Otherwise grades are A+ (90+), A (80+), B (70+), C (60+), D (50+), E (below 50).
- High performer: average at least 85% and Pass.
- Low performer: average below 50% or Fail.

## Individual GitHub contribution

Each member can upload their assigned module file(s) to their own repository. For a runnable full project, upload the **entire folder contents** together; modules import one another and `main.py` is the entry point. Add `students.csv` as the sample dataset.
