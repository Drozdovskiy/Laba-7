text = input(' Ведите строку ')
vse_gls = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
gls = 0
sgl = 0
for i in text:
    if i in vse_gls:
        gls += 1
    else:
        sgl += 1

print('Гласные:', gls)
print('Согласные:', sgl)