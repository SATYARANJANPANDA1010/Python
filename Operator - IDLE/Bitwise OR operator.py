Python 3.9.11 (tags/v3.9.11:2de452f, Mar 16 2022, 14:33:45) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 12
>>> b = 15
>>> c = a|b
>>> c
15
>>> print(bin(a),bon(b),bin(c))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(bin(a),bon(b),bin(c))
NameError: name 'bon' is not defined
>>> print(bin(a),bin(b),bin(c))
0b1100 0b1111 0b1111
>>> 