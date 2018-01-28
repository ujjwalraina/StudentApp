class Student:
    def __init__(self):
        self.sname = ''
        self.grade = ''
        self.math = 0
        self.english = 0
        self.science = 0

    def calc(self):
        avg = (self.math + self.english +self.science)/3
        if avg < 30:
            self.grade = 'E'
        elif avg>=30 and avg<50:
            self.grade = 'D'
        elif avg>=50 and avg<65:
            self.grade = 'C'
        elif avg>=65 and avg<85:
            self.grade = 'B'
        else:
            self.grade = 'A'
        return self.grade


    def add(self):
        self.sname = input('enter sname: ')
        self.math = int(input('enter math: '))
        self.english = int(input('enter english: '))
        self.science = int(input('enter science: '))
        self.grade = self.calc()