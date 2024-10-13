namber = [3, 4, 5, 6, 7, 8 , 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
def password(number):
    pass_ = ''
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                print(number)
                pass_ += str(i) + str(j)
    return pass_

print('Введите число: ')
print(password(int(input())))