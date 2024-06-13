import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    student_subject = students.merge(subjects, how='cross')
    count = examinations.groupby(['student_id', 'subject_name']).agg(attended_exams=('subject_name', 'count'))
    result = student_subject.merge(count, on=['student_id', 'subject_name'], how='left').sort_values(by=['student_id', 'subject_name']).fillna({'attended_exams': 0})
    return result[['student_id', 'student_name', 'subject_name', 'attended_exams']]