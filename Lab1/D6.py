# Даалгавар 6.  Алдаа олж засах (Debug)
# Доорх кодыг ажиллуулахад алдаа гардаг. 
# Алдааны шалтгааныг тайлбар (comment) байдлаар бичээд, 
# зассан кодоо шинээр бич.
# Алдаатай код: 
# class Student:
#     def __init__(name, age):
#         self.name = name
#         self.age = age
# Санамж: __init__ method-ийн эхний параметр байнга self байх ёстой — 
# эс тэгвэл эхний бодит аргумент (name) буруугаар self-д орно.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
s1= Student ("Bold", 17)

print(s1.name)
print(s1.age)
    