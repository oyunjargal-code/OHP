# [ХЯЛБАР]  Дасгал 1.  Нохой (Dog)
# Юуг дадлагажуулах вэ?  Анхны энгийн class бичиж, attribute болон method 
# хэрхэн ажилладгийг мэдрэх дадлага.
# Даалгавар:  name, breed гэсэн 2 attribute-тай 
# Dog класс зарла. bark() method нэмж, "Хау хау!" гэж хэвлэдэг болго.
# Жишээ гаралт:
# Хау хау!
class Dog:
    def __init__(self, name, breed):
        self.name= name
        self.breed= breed
    def bark(self):
        print("Hau hau!")
d1=Dog("Bobik", "Aylchin")
d1.bark()