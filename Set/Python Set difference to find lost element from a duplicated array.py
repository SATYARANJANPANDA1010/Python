A = [1, 4, 5, 7, 9]
B = [4, 5, 7, 9]
S1 = set(A)
S2 = set(B)
print(f'First Array {A}')
print(f'Second Array {B}')
if len(S1) > len(S2):
    print(f'{S1-S2} is missing in second array')
else:
    print(f'{S2-S1} is missing in first array')

