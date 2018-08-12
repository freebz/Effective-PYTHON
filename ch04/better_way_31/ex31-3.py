class Grade(object):
    def __get__(*args, **kwargs):
        # ...

    def __set__(*args, **kwargs):
        # ...

class Exam(object):
    # 클래스 속성
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


exam = Exam()
exam.writing_grade = 40


Exam.__dict__['writing_grade'].__set__(exam, 40)


print(exam.writing_grade)

print(Exam.__dict__['writing_grade'].__get__(exam, Exam))
