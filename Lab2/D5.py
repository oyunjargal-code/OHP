# Даалгавар:  increase_grade(self, amount=5) method бич — 
# дуудахад аргумент өгөхгүй бол 5-аар, өгвөл өгсөн тоогоор дүнг нэмэгдүүлдэг болго. 
# Дүн 100-аас хэтрэхгүй байхаар хязгаарла (min() ашиглаж болно).

class Student:
    def __init__(self, name, grade=0):
        self.name = name
        self.grade = grade
    def increase_grade(self, amount= 5):
        self.grade= min(100, self.grade + amount)

s1= Student("Bat",75)
before1=s1.grade
s1.increase_grade()
print("Dun:,", before1,"-> increase-iin daraa", s1.grade)

s2= Student("Saraa",47)
before2=s2.grade
s2.increase_grade(13)
print("Dun:,", before2,"-> increase-iin daraa", s2.grade)