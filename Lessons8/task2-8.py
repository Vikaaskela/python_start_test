#Task 2
#Напишіть функцію, яка поверне кількість слів у текстовому рядку.

def func(text):
    """ Write a function that returns the number of words in a text string.
    Args:
        text (str):

    Returns:
        number: will return the number of words in a text string
    """
    return f'{len(text.split())}'
print(func('Hello people!'))