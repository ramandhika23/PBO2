class PersegiPanjangMeta(type):
    def _init_(cls, name, bases, attrs):
        super()._init_(name, bases, attrs)
        def luas(cls, panjang, lebar):
            return panjang * lebar
        cls.luas = classmethod(luas)
        def keliling(cls, panjang, lebar):
            return 2 * (panjang + lebar)
        cls.keliling = classmethod(keliling)
class PersegiPanjang(metaclass=PersegiPanjangMeta):
    pass
A = PersegiPanjang()
B = A.luas(4,5)
C = A.keliling(4,5)
print('Luas Persegi Panjang:',B)
print('Keliling Persegi panjang:',C)