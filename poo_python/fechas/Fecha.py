class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.año}'

    def __gt__(self, otro):
        cadena_self = f"{self.año:04}{self.mes:02}{self.dia:02}"
        cadena_otro = f"{otro.año:04}{otro.mes:02}{otro.dia:02}"
        return int(cadena_self) > int(cadena_otro)
    
#%% test
fecha1 = Fecha(10,3,2024)
fecha2 = Fecha(11,3,2022)

print("pruebo __str__")
print(fecha1)

print("pruebo __gt__")
print(fecha1>fecha2)
print(fecha2>fecha1)