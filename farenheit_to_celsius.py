farenheit = int(input('Input F: '))

def converter(c):
    return (farenheit - 32) / 1.8


celsius = converter(farenheit)
print(f'It is {celsius} C')
