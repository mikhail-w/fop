import statistics


class Student:
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade

    def get_grade(self):
        return self._grade


def basic_stats(student_list):
    total_grade = 0
    grade_list = []
    count_obj = {}
    for student in student_list:
        grade_list.append(student.get_grade())

    mean = sum(grade_list) / len(grade_list)
    print(grade_list, mean)

    for grade in grade_list:
        if grade in count_obj:
            count_obj[grade] += 1
        else:
            count_obj[grade] = 1

    print(count_obj)
    max_count = 0
    mode = 0
    for key, value in count_obj.items():
        print(key, value)
        if value > max_count:
            max_count = value
            mode = key
    print(f"Mode: {mode}")

    med = statistics.median(grade_list)
    print(f"Median: {med}")

    result = (mean, med, mode)
    return result


s1 = Student("Kyoungmin", 73)
s2 = Student("Mercedes", 74)
s3 = Student("Avanika", 78)
s4 = Student("Marta", 74)

student_list = [s1, s2, s3, s4]
print(basic_stats(student_list))  # should print a tuple of three values
