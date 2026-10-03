# Даалгавар 2.  Мэдээллээ нэгтгэн харуулах
# Даалгавар 1-ийн Student класст display_info() method нэмж, нэр, нас, дүнг нэг мөрөнд эмхэтгэн хэвлэ.
# Жишээ гаралт: 
# Нэр: Болд, Нас: 17, Дүн: 92

class Student:
    def __init__(self, name, age, grade):
        self.name= name
        self.age= age
        self.grade= grade
    def display_info(self):
        print(f"Ner: {self.name}, Nas: {self.age}, Onoo: {self.grade}")
s1= Student("Bat", 18, 99)
s1.display_info()