# Даалгавар 1.  Анхны класснаа зарла
# Student класс үүсгэж, __init__ ашиглан оюутны нэр (name), нас (age), дүн (grade) гэсэн 3 attribute-тай болго. Нэг object үүсгэж, 3 attribute-ийг тус тусад нь print()-ээр хэвлэ.
# Жишээ гаралт: 
# Болд
# 17
# 92

class Student:
    def __init__(self, name, age, grade):
        self.name= name
        self.age= age
        self.grade= grade
s1= Student("Bold", 17, 97)

print(s1.name)
print(s1.age)
print(s1.grade)