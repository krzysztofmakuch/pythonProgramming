##################
##### petle ######
##################
#1. 
def liczby_3_do_33():
    '''
    wypisuje wszystkie liczby
    '''
    print('nie chce mi sie tego pisac')


#2. 
def dodatnie_podzielne():
    '''
    Funkcja wypisuje liczby dodatenie, podzielne przez 7, mniejsze od 777
    '''
    a = 0
    while a < 777:
        if podzielne_przez_7(a):
            print('%3i jest podzielne przez 7' %(a))
        a += 1

def podzielne_przez_7(liczba):
    ''' (int) -> (boolean)
    funkcja sprawdza czy liczba podzielna przez 7
    '''
    return liczba % 7 == 0

#3.
def elementy_wieksze():
    '''
    wypisuje elementy z listy wieksze niz 3
    '''
    print('nie chce mi sie tego pisac')

#4.
def elementy_z_litera_a():
    '''
    wypisuje z listy elementy zawierajace litere 'a'
    '''
    lista = ['ala', 'pies', 'slon', 'rzeka']
    for ele in lista:
        if 'a' in ele: print(ele)

#5.
def od_ostatniego():
    '''
    wypisuje wszystkie elementy listy w odwrotnej kolejnosci
    '''
    lista = [2,3,51,521,1,5]
    for ele in lista[::-1]:
        print(ele)

#6.
def bin_dec(binarna):
    '''(str)
    Funkcja zamienia liczbe z systemu binarnego(string 0 i 1) na dwojkowy
    '''
    i = 0
    suma = 0
    
    while i < len(binarna):
        suma = 2*suma + int(binarna[i])
        i += 1
    print(suma)
        

##################
#### stringi #####
##################

#1. tego nie bede pisal, macie wypisane jakich metod uzyc

#2. zrobmy to petla
def zlicz_litery_a():
    '''
    zlicza litery 'a' w slowie
    '''
    slowo = 'Pan Marcin poszedl do Ali'
    i = 0
    for w in slowo:
        if w == 'a':
            i += 1
    print('w slowie \'%s\' jest %i liter \'a\'' %(slowo, i))

#3.
def zamiana_pierwszej_ostatniej(slowo):
    '''(str)
    funkcja zamienia ostatnia i pierwsza litere
    '''
    #utrudnijmy zycie i zrobmy to dookola, przez zmienna tymczasowa i liste:
    lista = list(slowo)
    temp = slowo[0]
    lista[0] = lista[len(slowo)-1]
    lista[len(slowo)-1] = temp
    nowe_slowo = ''.join(lista)
    print('%s to stare slowo, a po zamianie liter otrzymujemy %s' %(slowo,\
                                                                    nowe_slowo))

    #a znacznie prosciej:
    nowe_slowo_2 = slowo[-1] + slowo[1:len(slowo)-1] + slowo[0]
    print('z prostszego sposobu tez dostaniemy %s' %(nowe_slowo_2))

#4.
def zlicz_dowolne_litery(slowo, litera):
    '''(str, str)
    Funkcja zlicza liczbe liter w slowie
    '''
    i = 0
    for w in slowo:
        if w == litera:
            i += 1
    print('w slowie \'%s\'  jest %i liter \'%s\'' %(slowo, i, litera))
    
#5.
def usun_litere(slowo, n):
    '''(str)
    Usuwa n-ta litere ze slowa
    '''
    nowe_slowo = slowo[:n-1] + slowo[n:]
    print('Stare slowo to \'%s\', a po usunieciu %i-ej litery uzyskujemy \
slowo \'%s\'' %(slowo, n, nowe_slowo))

##################
##### listy ######
##################

#1. tego mi sie nie chce, wszystko jest w instrukcji

#2.
def skrajne_z_listy(lista):
    '''(list) -> (list)
    zwraca dwuelementowa liste z neipustej listy danej. Pierwszy i ostatni
    element odpowiadaja pierwszemu i ostatniemu elementowi
    '''
    #prosze zwrocic uwage, ze co innego oznacza 'zwraca', a co innego 'wypisuje'
    return [lista[0],lista[-1]]
    
#3.
def dlugosc_elementow(lista):
    '''(list)
    wypisuje dlugosc wszystkich elementow listy
    '''
    i = 0
    for ele in lista:
        #zalozylem, ze zaden element nie jest dluzszy niz 10:
        print('Dlugosc elementu %i:%10s wynosi %i' %(i, ele, len(ele)))
        i += 1

#4. To zadania mozna zrobic na wiele sposobow
def dlugosc_najdluzszego_ele(lista):
    '''(list)
    podaje dlugosc najdluzszego elementu w liscie
    '''
    #sposob 1. - przez zmienne tymczasowe, wasz poziom
    max_len = 0
    for ele in lista:
        temp = len(ele)
        if temp > max_len:
            max_len = temp
            
    print('Najdluzszy element ma dlugosc', max_len)
    
    #sposob 2. - tez wasz poziom, ale juz trzeba wiedziec, ze tak sie da
    print('Korzystajac z funckji wbudwanej:', len(max(lista, key = len)))

    #sposob 3. - mniej wiecej cwiczenie 5
    print('Korzystajac z list skladanych:', max([len(ele) for ele in lista]))





    
