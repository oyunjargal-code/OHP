# [ХЯЛБАР]  Дасгал 4.  Кино (Movie)
# Юуг дадлагажуулах вэ?  Олон attribute-ийг нэг мессежинд эмхэтгэх дадлага.
# Даалгавар:  title, year гэсэн 2 attribute-тай Movie класс зарла. 
# info() method нэмж мэдээллийг нэгтгэж хэвлэ.
# Жишээ гаралт:
# Кино: Interstellar (2014)
class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year
    def info(self):
        print(f"{self.title} ({self.year})")
m1= Movie("Interstellar", 2014)
m1.info()