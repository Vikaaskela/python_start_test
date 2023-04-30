'''
text = input('text=').lower().split()
result =[]
for word in text:
    if word not in result:
        result.append(word)
print('\n'.join(result))
'''
'''
text = input('text=').lower().split()
result = set(text)
print('\n'.join(result))
'''
'''
import string
text = input('text=').lower()
tmp = set(text) - set(string.punctuation)
res = {}
for item in tmp:
    res[item] = text.count(item)
print(res)
'''
text = input('text=').lower().split()
bad_words = {'aaa', 'bbb'}
if set(text) & bad_words:
    print('Error')
else:
    print(text)
