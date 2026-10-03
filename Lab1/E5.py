# [ХЯЛБАР]  Дасгал 5.  Утас (Phone)
# Юуг дадлагажуулах вэ?  Method дотор нөхцөлт логик (if) анх удаа ашиглах дадлага.
# Даалгавар:  brand, battery гэсэн 2 attribute-тай Phone класс зарла. 
# is_charged() method нэмж, battery 50-аас их бол True, эс тэгвэл False буцаадаг болго.
# Жишээ гаралт:
# True
class Phone:
    def __init__(self,brand, battery):
        self.brand= brand
        self.battery= battery
    def is_charged(self):
        if 50<= self.battery <=100:
            print("True")
        else:
            print("False")
p1=Phone("Samsung", 99)
p1.is_charged()