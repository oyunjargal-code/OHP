# [ХЯЛБАР]  Дасгал 2.  Тойрог (Circle)
# Юуг дадлагажуулах вэ?  __init__ дотор attribute зөв онооход анхаарах дадлага.
# Даалгавар:  radius гэсэн 1 attribute-тай Circle класс зарлаж, 
# object үүсгээд radius-аа print() ашиглан шууд хэвл (method шаардлагагүй).
class Circle:
    def __init__(self, radius):
        self.radius= radius
c1= Circle(5)
print(c1.radius)