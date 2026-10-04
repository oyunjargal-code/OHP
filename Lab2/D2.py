# Даалгавар:  is_passing() method нэм — grade >= 60 бол True, эс тэгвэл 
# False БУЦААНА (print хийхгүй). Дараа нь if s1.is_passing(): ашиглан 
# "Тэнцсэн" эсвэл "Тэнцээгүй" гэж хэвлэ.

class Student:
    def __init__(self,name, age=18, is_active= True, grade=0):
        self.name = name
        self.age = age
        self.is_active = is_active
        self.grade= grade
    def is_passing(self):
        return self.grade >= 60
        
s1= Student("Bat", grade=75)

if s1.is_passing():
    print("Tentssen")
else:
    print("Tentseegui")
