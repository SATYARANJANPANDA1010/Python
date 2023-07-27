# pop() method
# s.pop() or s.pop(i)
# retrieves the item at i and also removes it from s
# s.pop() --> read and remove last element
# s.pop(i) --> read and remove, element at given i (index)

stack = []
stack.append("java")
stack.append("c++")
stack.append("python")
print(stack)
course1 = stack.pop()
print(course1)

course2 = stack.pop()
print(course2)

print(stack)
