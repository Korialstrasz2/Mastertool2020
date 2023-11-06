class Arma():
    def __init__(self):
        self.danno = []
        self.resistenza = 100

    pa_per_attacco = 5

class na(Arma):
    danno = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    pa_per_attacco = 3
    nome = "Mani Nude"

class ManiNude(Arma):
    danno = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 6, 7, 8, 8]
    pa_per_attacco = 3
    nome = "Mani Nude"


class SpadaCorta(Arma):
    danno = [0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 8, 8, 10]
    pa_per_attacco = 4
    nome = "Spada Corta"


class SpadaLunga(Arma):
    danno = [0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 10, 10, 10, 12, 15]
    pa_per_attacco = 5
    nome = "Spada Lunga"

class Mazza(Arma):
    danno = [0, 0, 0, 0, 0, 0, 4, 4, 4, 8, 8, 8, 12, 12, 12, 14, 14, 14, 16, 20]
    pa_per_attacco = 6
    nome = "Mazza"

class Ascia(Arma):
    danno = [0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 8, 8, 8, 8, 12, 12, 15, 15, 19]
    pa_per_attacco = 5
    nome = "Ascia"

class Lancia(Arma):
    danno = [0, 0, 0, 0, 0, 0, 5, 5, 5, 9, 9, 9, 15, 15, 15, 20, 20, 20, 21, 24]
    pa_per_attacco = 6
    nome = "Lancia"

class Alabarda(Arma):
    danno = [0, 0, 0, 0, 0, 0, 0, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19, 24]
    pa_per_attacco = 6
    nome = "Alabarda"

class Bastone(Arma):
    danno = [0, 0, 4, 4, 4, 6, 6, 6, 8, 8, 8, 10, 10, 10, 10, 13, 13, 13, 13, 14]
    pa_per_attacco = 5
    nome = "Bastone"

class Spada2Mani(Arma):
    danno = [0, 0, 0, 0, 0, 0, 6, 6, 6, 10, 10, 10, 14, 14, 14, 18, 18, 18, 22, 26]
    pa_per_attacco = 6
    nome = "Spada a 2 Mani"

class Ascia2Mani(Arma):
    danno = [0, 0, 0, 0, 0, 0, 0, 11, 11, 13, 13, 15, 15, 17, 18, 19, 22, 22, 22, 26]
    pa_per_attacco = 7
    nome = "Ascia a 2 Mani"

class Martello2Mani(Arma):
    danno = [0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 18, 18, 25, 25, 26, 26, 26, 31, 34]
    pa_per_attacco = 8
    nome = "Martello a 2 Mani"

class Arco(Arma):
    danno = [0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 10, 10, 10, 12, 15]
    pa_per_attacco = 5
    nome = "Arco"

class Balestra(Arma):
    danno = [0, 4, 4, 5, 5, 6, 6, 8, 8, 8, 10, 10, 10, 10, 10, 11, 11, 11, 11, 12]
    pa_per_attacco = 2
    nome = "Balestra"

class Natura1(Arma):
    danno = [0, 4, 4, 5, 5, 6, 6, 8, 8, 8, 10, 10, 10, 10, 10, 11, 11, 11, 11, 12]
    pa_per_attacco = 6
    nome = "Natura 1"

class Natura2(Arma):
    danno = [0, 0, 5, 5, 6, 7, 7, 8, 9, 9, 10, 11, 11, 12, 13, 13, 14, 15, 15, 16]
    pa_per_attacco = 6
    nome = "Natura 2"

class Natura3(Arma):
    danno = [0, 0, 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    pa_per_attacco = 7
    nome = "Natura 3"