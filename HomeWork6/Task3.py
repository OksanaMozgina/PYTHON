# Написать функцию, аргументы имена сотрудников, возвращает словарь, 
# ключи — первые буквы имён,
# значения — списки, содержащие имена, начинающиеся с соответствующей буквы.


words = "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

def collection(words):
    new_list = []
    dict_list = {}
    for word in sorted(words):
        key = word[0]
        if key in dict_list:
            dict_list[key].append(word)
        else:
            dict_list[key] = [word]
    return dict_list
print()
print(words)
print()
a = collection (words)
print(a)
print()
