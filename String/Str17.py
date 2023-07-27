names = ['naresh rao','Satya ranjan','Krishna jain']
for word in names:
    print(word.title())
# comprehension
Title_name = [word.title() for word in names]
print(Title_name)