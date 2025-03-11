class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.año}'

    def __gt__(self, otro):
        cadena_self = str(self.año) + str(self.mes) + str(self.dia)
        cadena_otro = str(otro.año) + str(otro.mes) + str(otro.dia)
        return int(cadena_self) > int(cadena_otro)
    
#%% test
fecha1 = Fecha(10,3,2024)
fecha2 = Fecha(11,3,2022)

print("pruebo __str__")
print(fecha1)

print("pruebo __gt__")
print(fecha1>fecha2)
print(fecha2>fecha1)