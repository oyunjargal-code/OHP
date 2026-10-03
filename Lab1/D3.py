# Даалгавар 3.  Дүнгээ шинэчлэх
# update_grade(new_grade) method нэмж, шинэ дүнг зөвхөн 0–100 хооронд байвал шинэчил, 
# эс тэгвэл алдааны мессеж хэвлэ.
# Жишээ гаралт: 
# Дүн амжилттай шинэчлэгдлээ.
# Алдаа: дүн 0-100 хооронд байх ёстой.

class Student:
    def __init__(self, name, age, grade):
        self.name= name
        self.age= age
        self.grade= grade
    def update_grade(self, new_grade):
        if 0 <= new_grade <=100:
            self.grade= new_grade
            print("Dun amjilttai shinechlegdlee")
        else:
            print("Aldaa: Dun 0-100-giin hoorond baih ystoi")
s1= Student("Saraa", 15, 85)
s1.update_grade(105)