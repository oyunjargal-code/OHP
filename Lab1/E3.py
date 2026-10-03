# [ХЯЛБАР]  Дасгал 3.  Бараа (Product)
# Юуг дадлагажуулах вэ?  Attribute-уудыг method дотор нэгтгэн ашиглах дадлага.
# Даалгавар:  name, price гэсэн 2 attribute-тай Product класс зарла. 
# show_price() method нэмж, "нэр — үнэ₮" хэлбэрээр хэвлэдэг болго.
# Жишээ гаралт:
# Цамц — 45000₮
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def show_price(self):
        print(f"Ner: {self.name}- {self.price}₮")
p1= Product("Цамц", 45000)
p1.show_price()