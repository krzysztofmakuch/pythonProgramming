#przyklad na dziedziczenie, niekoniecznie poprawny matematycznie

class prostokaty:
    def __init__(self, podstawa, wysokosc):
        self.h = wysokosc
        self.a = podstawa

    def pole(self):
        return(self.a * self.h)

    def obwod(self):
        return(2*self.a + 2*self.h)

    #przeladowanie operatora, wroc dopiero po zrozumieniu dziedzicznosci
    def __add__(self, o):
        return self.obwod() + o.obwod()

    #wiedziec, ze w ten sposob mozna spowodowac automatyczne wywolanie metody
    #i przypisanie wyniku do zmiennej
    k = property(obwod)

    #podobno dobra praktyka:
    def __str__(self):
        return('Obiekt jest prostokatem o wysokosc %s i podstawie %s' %(self.h, self.a))

class romby(prostokaty):
    def __init__(self, podstawa, wysokosc, bok):
        prostokaty.__init__(self, podstawa, wysokosc)
        self.b = bok

    #obwod rombu jest liczony inaczej, wiec trzeba nadpisac metode:
    def obwod(self):
        return(2*self.b + 2*self.a)    


#dziedziczyc mozna rowniez za pomoca funkcji super()
class trapezy(prostokaty):
    def __init__(self, podstawa, wysokosc, bok1, bok2, podstawa2):
        super().__init__(podstawa, wysokosc)
        self.b1 = bok1
        self.b2 = bok2
        self.p2 = podstawa2

    def obwod(self):
        return(self.a + self.b1 + self.p2 + self.b2)
       
