#Task 2
#Напишіть функцію, яка поверне кількість слів у текстовому рядку.
'''
def func(text):
    """ Write a function that returns the number of words in a text string.
    Args:
        text (str):

    Returns:
        number: will return the number of words in a text string
    """
    return f'{len(text.split())}'
print(func('Hello people!'))
'''
'''
def words_count(text: str) -> int:
    return len(text.split())
print(words_count('Hello world'))
'''
import string


def words_count(text:str) -> int:
    for item in string.punctuation:
        text = text.replace(item, ' ')
         
    return len(text.split())


print(words_count('Hello, world'))
