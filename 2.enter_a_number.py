count_ = 0
sum_ = 0
a = None
while a != 'done':
    a = input('Enter a number: ')
    if a == 'done':
        break
    else:
        try:
            sum_ += int(a)
            count_ += 1
        except:
            print('Invalid input')


print(sum_, count_, sum_/count_)
