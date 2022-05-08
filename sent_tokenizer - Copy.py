import re

s = 'A! Bsss. C D A'
pattern = r'\W'

l = re.split(pattern, s, 2)
print(l)