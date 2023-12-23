import re 
def vowel(text):
    res=max(text, key=lambda word: len(re.findall('r[aeiouAEIOU]', word)))
    res1=str(res)
    return res1

print(vowel(['suxrob', 'hello', 'world', 'google']))