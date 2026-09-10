# 2. словари. создать словарь студентов (имя- строка, оценки (массив)).
# написать функцию которая считает средний бал, доставая значения по ключу.

def main():
    student = {'name': "alex", 'grades': [4, 5, 4, 5, 4, 3, 4, 3]}
    print(count_everage_grades(student))


def count_everage_grades(student):
    averege_grade = 0.0
    arr_grades = student.get('grades', [])
    if not arr_grades:
        return 0.0
    for grade in arr_grades:
        averege_grade += grade
    averege_grade = averege_grade / len(arr_grades)
    return averege_grade


main()
