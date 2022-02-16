y = [1, 2, 3, 4, 5, 6, 7, 8]
x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0:
            print(f'{y[i]}{x[j]} is a black bar')
        elif i % 2 != 0 and j % 2 != 0:
            print(f'{y[i]}{x[j]} is a black bar')
        elif i % 2 == 0 and j % 2 != 0:
            print(f'{y[i]}{x[j]} is a white bar')
        elif i % 2 != 0 and j % 2 == 0:
            print(f'{y[i]}{x[j]} is a white bar')



