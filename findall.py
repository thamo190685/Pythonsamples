import re

str = 'This is really short & sweat, is not it?'

x = re.findall("\Bis",str)

print(x)

print(len(x))