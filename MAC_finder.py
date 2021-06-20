#A valid MAC address must satisfy the following conditions:
'''
It must contain 12 hexadecimal digits.
One way to represent them is to form six pairs of the characters separated with a hyphen (-) or colon(:).
For example, 01-23-45-67-89-AB is a valid MAC address.
Another way to represent them is to form three groups of four hexadecimal digits separated by dots(.).
For example, 0123.4567.89AB is a valid MAC address.
'''

import re
fhand = open("characters.txt","r")
filecontent = fhand.read()

#def validadress(str):
#    if (fhand == None):
#        return False

regex = re.compile(r'(?:[0-9a-fA-F]:?){12}')
print(re.findall(regex,filecontent))
