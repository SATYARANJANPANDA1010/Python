# WAP to count vowels in given string

str1 = input("Enter any string: ")
a, e, i, o, u = 0, 0, 0, 0, 0
a = str1.count("a")
e = str1.count("e")
i = str1.count("i")
o = str1.count("o")
u = str1.count("u")

print(f" 'a' count is {a} 'e' count is {e} 'i' count is {i} 'o' count is {o} 'u' count is {u} total number vowels {a+e+i+o+u}"
     )