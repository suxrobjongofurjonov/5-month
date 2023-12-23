#garbage collection
#   C dasturlash tilida строго-типизированный bo'ladi o'zgaruvchi yozilishidan type ni yozish kerak va bitta nomli o'zgaruvchi yaratilsa eski o'zga
# ruvchini hotirasi o'chmaydi chunki type o'zgarmaydi
#  Python tilida dynamic bo'ladi va bitta nomli o'zgarubchi yaratilsa eski o'zgaruchi hotirasi o'chib ketadi chunki python dynamic shuning uchun yangi 
# boshqa typeda yaratilishi mumkin
import re

# text="""Both patterns and strings to be searched can be Unicode strings (str) as well as 8-bit strings (bytes). However, Unicode strings and 8-bit strings cannot be mixed: that is, you cannot match a Unicode string with a byte pattern or vice-versa; similarly, when asking for a substitution, The replacement string must be of thesame type as both thE pattern and the search string."""

# javob= re.findall('the',text)
# print(len(javob))
## alxodililani olish uchun
# javob= re.findall('\\bthe\\b',text)
# print(len(javob))
## kattadami yoki kichkinami olish uchun
# javob= re.findall('[Tt][Hh][Ee]',text)
# print(javob)
## sonlarni topish uchun
# javob= re.findall('[0-9]',text)
# print(javob)

matn="""Regular expressions can be concatenated to form new regular expressions; if A and B are both regular expressions, then AB is also a regular expression. In general, if a string p matches A and another string q matches B, the string pq will match AB. This holds unless A or B contain low precedence operations; boundary conditions between A and B; or have numbered group references. Thus, complex expressions can easily be constructed from simpler primitive expressions like 88 the ones described 43 here. For details of the theory and implementation of 65 regular expressions, consult the Friedl book [Frie09], or almost any textbook about compiler construction."""

# j=re.findall('[A-Z]',matn)
# print(len(j))
# j=re.findall('.',matn)
# print(j)hammasini olib beradi faqat \n tashqari
# j=re.findall('\d',matn)
# print(j)
