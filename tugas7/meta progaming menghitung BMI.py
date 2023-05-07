#Nama   : Muhamad Nairul Ramandhika
#Kelas  : R1
#NIM    : 210511040

class MenghitungBMIMeta(type):
    def _init_(cls, name, bases, attrs):
        super()._init_(name, bases, attrs)
        def pria(cls, tinggi):
            return (tinggi - 100) - (tinggi - 100) * 10/100
        cls.pria = classmethod(pria)

        def wanita(cls, tinggi):
            return (tinggi - 100) - (tinggi - 100) * 15/100
        cls.wanita = classmethod(wanita)
class Ideal(metaclass=MenghitungBMIMeta):
    pass
A = Ideal()
B = A.pria(173)
C = A.wanita(155)
print('BMI Pria:',B)
print('BMI Wanita:',C)