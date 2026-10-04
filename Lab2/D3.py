# Даалгавар:  display_info(self, verbose=False) method бич. 
# verbose=False үед зөвхөн нэр, дүнг; verbose=True үед нас, идэвхтэй эсэхийг 
# нэмж хэвлэдэг болго.
class Student:
    def __init__(self,name, age=18, is_active= True, grade=0):
        self.name = name
        self.age = age
        self.is_active = is_active
        self.grade= grade
    def display_info(self, verbose= False):
        print("Ner:", self.name, ", Dun:", self.grade)
        if verbose:
            print("age:", self.age, self.is_active)
s1=Student("Bat",grade=75)
s1.display_info()
s1.display_info(verbose=True)