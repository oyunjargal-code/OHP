# # АЛДААТАЙ код:
# class Recipe:
#     def __init__(self, name, ingredients=[]):
#         # АЛДАА: [] нь mutable, зөвхөн НЭГ УДАА үүсээд бүх object хуваалцана
#         self.name = name
#         self.ingredients = ingredients
 
 
# recipe1 = Recipe("Бууз")
# recipe1.ingredients.append("мах")
 
# recipe2 = Recipe("Салат")
# print(recipe2.ingredients)  # хоосон байх ёстой байтал "мах" гарч ирнэ!

# ЗАССАН хувилбар:
class Recipe:
    def __init__(self, name, ingredients=None):
        self.name = name
        self.ingredients = ingredients if ingredients is not None else []
 
 
recipe1 = Recipe("Бууз")
recipe1.ingredients.append("мах")
 
recipe2 = Recipe("Салат")
print(recipe2.ingredients)  # одоо зөв хоосон list гарна

