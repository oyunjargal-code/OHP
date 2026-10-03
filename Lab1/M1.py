# [ДУНД]  Дасгал 6.  Машин (Car)
# Юуг дадлагажуулах вэ?  Object-ийн төлөвийг (state) method-оор өөрчлөх дадлага.
# Даалгавар:  brand attribute, speed=0 гэсэн эхний утгатай Car класс зарла. 
# accelerate(amount) method нэмж, дуудах бүрд speed-ийг amount-аар нэмэгдүүлж, 
# шинэ хурдыг хэвлэдэг болго.
# Жишээ гаралт:
# Одоогийн хурд: 20
# Одоогийн хурд: 45
class Car:
    def __init__(self,brand, attribute="Standart", speed=0):
        self.brand= brand
        self.attribute= attribute
        self.speed = speed
    def accelerate(self, amount):
        self.speed = self.speed + amount
        print(self.brand,"-iin hurd odoo:", self.speed, "km/ts")

car1= Car("Toyota")
car1.accelerate(20)
car1.accelerate(15)