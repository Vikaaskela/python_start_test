#Task 7
#Напишіть скрипт для очищення тексту від HTML-тегів.
#Також необхідно врахувати кілька особливостей:
#- крім одинарних тегів є парні теги, наприклад <div> </div>, тобто. перший тег відкриває, 
#а другий закриває.
#- тег у собі може містити купу додаткової інформації. Наприклад <div id="rcnt" style="clear:both;
#position:relative;zoom:1">

text = """<p>Приклад використання атрибуту `text`</p>
<body id="b" onload="func(this.vling)">
  <p>Атрибут `text` визначає колір тексту в документі. Кольори окремих елементів можна легко змінювати за допомогою стилів.</p>
  <input type="color" name="" id="a1"><br><br>
<input type="button" onclick="func()" value="Змінити колір">
</body>
"""
while '<' in text:
    tag_start = text.find('<')
    tag_end = text.find('>')

    temp = text[tag_start:tag_end + 1]
    text = text.replace(temp, '')
text = text.replace('\n\n', '')
print(text)