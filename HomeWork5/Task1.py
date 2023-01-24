# Напишите программу, удаляющую из текста все слова, содержащие "абв".
#  В тексте используется разделитель пробел.

from random import sample

def rand_list(count: int, alp: str = 'abc'):
    new_list = []
    for i in range(count):
        letters = sample(alp, k=3)
        new_list.append("".join(letters))
    return " ".join(new_list)

def simple_sentence(words: str) -> str:
    return " ".join(i for i in words.split() if i != "abc")

all_list = rand_list(int(input("Number of words : ")))
print(all_list)
print(simple_sentence(all_list))
