import locale
# locale.setlocale(locale.LC_COLLATE,'pt_RB.UTF-8')
fruits = ['caju','atemoia','cajá','açaí','acerola']
sorted_fruits = sorted(fruits,key=locale.strxfrm)
print(sorted_fruits)
