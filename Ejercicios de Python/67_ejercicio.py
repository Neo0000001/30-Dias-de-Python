# Ejercicio 67: Convertir kilopascales (kPa) en presión psi, mmHg, y atm.

def conversor(kpa):
    psi = kpa / 6.89475729
    mmhg = kpa *  760 / 101.325
    atm = kpa / 101.325
    return (f'{kpa} KPa equivale a {psi} psi, {mmhg} mmHg y {atm} atmosferas.')
    
kpa = float(input('Introduce la presion en KPa: '))
print(conversor(kpa))