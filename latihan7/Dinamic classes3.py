class CelciusMeta(type):
    def _init_(cls, name, bases, attrs):
        super()._init_(name, bases, attrs)
        cls.suhu_standar = ""
    def to_fahrenheit(cls, suhu):
            return (suhu * 9/5) + 32
    def to_reamur(cls, suhu):
            return suhu * 4/5
    def to_kelvin(cls, suhu):
            return suhu + 273.15
class Celcius(metaclass=CelciusMeta):
    def _init_(self, suhu):
        self.suhu = suhu

    def ke_unit(self, unit):
        if unit == "Fahrenheit":
            self.suhu = self._class_.to_fahrenheit(self.suhu)
            self._class_.suhu_standar = "Fahrenheit"
        elif unit == "Reamur":
            self.suhu = self._class_.to_reamur(self.suhu)
            self._class_.suhu_standar = "Reamur"
        elif unit == "Kelvin":
            self.suhu = self._class_.to_kelvin(self.suhu)
            self._class_.suhu_standar = "Kelvin"
        elif unit == "Celcius":
            pass # do nothing
        else:
            raise ValueError(f"Unit {unit} tidak dikenal.")
    def _repr_(self):
        return f"{self.suhu:.2f} {self._class_.suhu_standar}"
# Membuat objek suhu dengan nilai 100 Celcius
c = Celcius(100)
# Mengubah objek suhu menjadi Fahrenheit
c.ke_unit("Fahrenheit")
print(c)