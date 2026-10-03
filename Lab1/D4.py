# Даалгавар 4.  Олон оюутантай зэрэг ажиллах
# 3-с доошгүй Student object үүсгэж, list-д хийгээд for давталтаар бүх оюутны 
# мэдээллийг display_info()-оор хэвлэ.
# Жишээ гаралт: 
# Нэр: Болд, Нас: 17, Дүн: 92
# Нэр: Сараа, Нас: 18, Дүн: 85
# Нэр: Түмэн, Нас: 17, Дүн: 76

class Student:
    def __init__(self, name, age, grade):
        self.name= name
        self.age= age
        self.grade= grade
    def display_info(self):
        print(f"Ner: {self.name}, Nas: {self.age}, Onoo: {self.grade}")

students= [
    Student("Bold",21, 97),
    Student("Naraa",20, 98),
    Student("Saraa",21, 87),
]

for s in students:
    s.display_info()