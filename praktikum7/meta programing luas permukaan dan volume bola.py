#Nama   : Muhamad Nairul Ramandhika
#Kelas  : R1
#NIM    : 210511040

class BolaMeta(type):
    def _init_(cls, name, bases, attrs):
        super()._init_(name, bases, attrs)
        def luaspermukaan(cls, jari):
            return 4 * 3.14 * jari * jari
        cls.luaspermukaan = classmethod(luaspermukaan)

        def volume(cls, jari):
            return 4/3 * 3.14 * jari * jari * jari
        cls.volume = classmethod(volume)
class Luaspermukaandanvolume(metaclass=BolaMeta):
    pass
A = Luaspermukaandanvolume()
B = A.luaspermukaan(21)
C = A.volume(21)
print('Luas Permukaan Bola:',B)
print('Volume Bola:',C)