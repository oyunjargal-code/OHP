# Даалгавар:  Student класст age=18, is_active=True гэсэн 2 default параметр нэм. 
# 3 object үүсгэ: (1) зөвхөн нэрээр, (2) нэр ба насаар, (3) бүх 3 утгыг дамжуулж. 
# Тус бүрийг print()-ээр шалга.

class Student:
    def __init__(self,name, age=18, is_active= True):
        self.name = name
        self.age = age
        self.is_active = is_active
s1= Student("Bat")
s2= Student("Saraa", 20)
s3= Student("Dulmaa", 19, False)

print(s1.name, s1.age, s1.is_active)
print(s2.name, s2.age, s2.is_active)
print(s3.name, s3.age, s3.is_active)