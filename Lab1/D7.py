# Даалгавар 7.  Танилцуулгын карт
# 1-р лабораторийн ажилд сурсан ASCII хайрцаг 
# (+---+ хэлбэр) ур чадвараа ашиглан, 
# Student object-ийн нэр, нас, дүнг доорхтой төстэй 
# танилцуулгын карт болгож хэвлэ.
# Жишээ гаралт: 
# +----------------------+
# | Нэр: Болд            |
# | Нас: 17              |
# | Дүн: 92              |
# +----------------------+

class Student:
    def __init__(self, ner, nas, dun):
        self.ner= ner
        self.nas= nas
        self.dun= dun
    def display_info(self):
        print(f"Ner: {self.ner}, Nas: {self.nas}, Dun: {self.dun}")
    def update_dun(self, newOnoo):
        if 0<= newOnoo <=100:
            self.dun= newOnoo
        else:
            print("Aldaa, 0-100-giin hoorond baih ystoi")
    def print_card(self):
        print("+---------------------+")
        print(f"| Ner: {self.ner:<16}|")
        print(f"| Nas: {self.nas:<16}|")
        print(f"| Dun: {self.dun:<16}|")
        print("+---------------------+")
s1= Student("Bold", 17, 92)
s1.print_card()
        
