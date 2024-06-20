slovo1 = str(input(' Введите слово '))

count = ''

for c in slovo1:
    count = c + count
    
if slovo1 == count:
    print ('Да')
else:
    print ('Нет')
