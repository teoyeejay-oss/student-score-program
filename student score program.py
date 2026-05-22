class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score

    @property
    def score(self):
       return self._score

    @score.setter
    def score(self,value):
        if value <0 or value > 100 :
            raise ValueError("Your score must be between 0 and 100.")
        self._score = value

    @property
    def grade(self):
        if 40 > self._score :
            return "Your grade is G"
        elif  self._score <50:
            return "Your grade is D"
        elif  self._score < 60 :
            return "Your grade is C"
        elif  self._score < 70 :
            return "Your grade is B"
        else:
            return "Your grade is A"
try:
    student1 = Student("kuma", 150)
    print(student1.score)
    print(student1.grade)
except ValueError as e :
    print(e)
