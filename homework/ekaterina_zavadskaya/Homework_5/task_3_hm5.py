"""Даны такие списки:

1) students = ['Ivanov', 'Petrov', 'Sidorov']
2) subjects = ['math', 'biology', 'geography']

Распечатайте текст, который будет использовать данные из этих списков.
Текст в итоге должен выглядеть так:

Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geography

"""


STUDENTS = ['Ivanov', 'Petrov', 'Sidorov']
SUBJECTS = ['math', 'biology', 'geography']

print("Students", ", ".join(STUDENTS),
      "study these subjects:", ", ".join(SUBJECTS))
