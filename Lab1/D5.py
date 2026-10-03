# Даалгавар 5.  Ангийн дундаж дүнг тооцоолох
# students жагсаалтад байгаа бүх Student object-ийн grade attribute-ийг 
# ашиглан дундаж дүнг тооцоолж хэвлэдэг class_average(students) функц бич.
# Жишээ гаралт: 
# Ангийн дундаж дүн: 84.3
# Санамж: Дундаж = дүнгүүдийн нийлбэр ÷ оюутны тоо.

class Student:
    def __init__(self, name, age, grade):
        self.name= name
        self.age= age
        self.grade= grade
    def display_info(self):
        print(f"Name: {self.name}, Nas: {self.age}, Dun: {self.grade}")
    def update_grade(self, newgrade):
        if 0<= newgrade <=100:
            self.grade=newgrade
        else:
            print("Aldaa: Dun 0-100-giin hoorond bh ystoi")
def class_avarge(students):
        total= 0
        for s in students:
            total= total + s.grade
        avarge = total / len(students)
        print("Angiin dundaj dun:", avarge)
students = [
        Student("Bold", 17, 92),
        Student("Saraa", 18, 85),
        Student("Tumen", 17, 76),
    ]

for s in students:
        s.display_info()
class_avarge(students)
        