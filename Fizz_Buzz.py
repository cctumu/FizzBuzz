fizzbuzz = []
for n in range(1, 101):
    list_num = list(str(n))
    count_3 = list_num.count('3')
    count_5 = list_num.count('5')
    if count_3 > 1 and count_5 <= 1:
        fizzbuzz.append('Fizz')
    elif count_5 > 1 and count_3 <= 1:
        fizzbuzz.append('Buzz')
    elif count_5 > 1 and count_3 > 1:
        fizzbuzz.append('FizzBuzz')
    else:
        fizzbuzz.append(n)
print(fizzbuzz)

