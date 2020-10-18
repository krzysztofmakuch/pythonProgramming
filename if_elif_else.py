a_str = input('podaj jakas liczbe ')
a = float(a_str)
if a > 0:
    print('%f jest dodatnia' %(a))
elif a < 0:
    print('%f jest ujemna' %(a))
else:
    print('%f nie jest ani dodatnia, ani ujemna' %(a))
