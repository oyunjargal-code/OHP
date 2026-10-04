# Даалгавар:  Student object-ийг зөвхөн keyword аргумент ашиглан 
# (жишээ нь grade=90, name="...", age=17) 2-3 өөр дарааллаар үүсгэж, 
# бүгд адилхан зөв ажиллаж байгааг батал.
class Student:
    def __init__(self, name, age=18, is_active=True, grade=0):
        self.name = name
        self.age = age
        self.is_active = is_active
        self.grade = grade
s1=Student("Dulguun",grade=90,age=17)
s2=Student(grade=92, name="Sanchir", age=18)
s3=Student (age=17, name="Dolgor", grade=90)

print(s1.name, s1.age, s1.grade)
print(s2.name, s2.age, s2.grade)
print(s3.name, s3.age, s3.grade)
