
#    Число делится на 3 тогда, когда сумма его цифр делится на 3.
#    Проверить этот признак на примере заданного трехзначного числа.
#

x = int(input())

if (x//100 + x%100//10 + x%10)%3==0:
    print('True')
else:
    print('False')