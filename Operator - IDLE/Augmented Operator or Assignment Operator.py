
b = 5
a/=b+5
a

>>> n1 = 4
>>> n2 = 2
>>> n1 *=n2-2
>>> n1
0
>>> A = 0b101
>>> B = 0b111
>>> A&=B
>>> print(bin(A),bin(B))
0b101 0b111
>>> A
5
>>> A=0b101
>>> B=0b111
>>> A|=B

>>> Print(bin(A),bin(B))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    Print(bin(A),bin(B))
NameError: name 'Print' is not defined
>>>  print(bin(A),bin(B))
 
SyntaxError: unexpected indent
>>> print(bin(A),bin(B))
0b111 0b111
>>> a = 0b111
>>> b = 0b110
>>> a^=b
>>> print(bin(a),bin(b))
0b1 0b110
>>> 