"""Напишите программу, которая добавляет ‘ing’ в конец слов (к каждому слову)
 в тексте:

 “Etiam tincidunt neque erat, quis molestie enim
 imperdiet vel. Integer urna nisl, facilisis vitae semper
 at, dignissim vitae libero”

 и после этого выводит получившийся текст на экран.

 Знаки препинания:
  - не должны оказаться внутри слова.
  - Если после слова идет запятая или точка, этот знак препинания
  должен идти после того же слова, но уже преобразованного.

  """


ORIGIN_TEXT = ("Etiam tincidunt neque erat, "
               "quis molestie enim imperdiet vel. "
               "Integer urna nisl, facilisis vitae semper at, "
               "dignissim vitae libero")

NEW_TEXT = []

for word in ORIGIN_TEXT.split():
    if "," in word:
        word = word.replace(",", "ing,")
        NEW_TEXT.append(word)
    elif "." in word:
        word = word.replace(".", "ing.")
        NEW_TEXT.append(word)
    else:
        word += "ing"
        NEW_TEXT.append(word)

print(" ".join(NEW_TEXT))
