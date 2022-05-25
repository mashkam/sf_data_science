import pandas as pd

student_data = pd.read_csv('data/students_performance.csv', sep=',')
print(student_data.loc[155, 'writing score'])

print(student_data.info())

print(round(student_data['math score'].mean()))

print(student_data['race/ethnicity'].mode())

print(round(student_data[student_data['test preparation course'] == 'completed'
                         ]['reading score'].mean()))

print(student_data[student_data['math score'] == 0].shape[0])

print(student_data[student_data['lunch'] == 'standart']['math score'].mean())

print(round(student_data['parental level of education'].
            value_counts(normalize=True)*100))

a = student_data[student_data['race/ethnicity'] ==
                 'group A']['writing score'].median()
b = student_data[student_data['race/ethnicity'] ==
                 'group C']['writing score'].mean()
print(abs(round(a - b)))
