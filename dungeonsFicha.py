import time, math
from racesdd import Races

def alt_for(n):
    global forca, mod_for
    forca = int(forca) + int(n)
    mod_for = non(int(forca))

def alt_des(n):
    global dest, mod_des
    dest = int(dest) + int(n)
    mod_des = non(int(dest))

def alt_con(n):
    global const, mod_con
    const = int(const) + int(n)
    mod_con = non(int(const))

def alt_int(n):
    global inte, mod_int
    inte = int(inte) + int(n)
    mod_int = non(int(inte))

def alt_sab(n):
    global sab, mod_sab
    sab = int(sab) + int(n)
    mod_sab = non(int(sab))

def alt_car(n):
    global car, mod_car
    car = int(car) + int(n)
    mod_car = non(int(car))
    
def alt_all(n):
    global forca, mod_for, dest, mod_des, const, mod_con, inte, mod_int, sab, mod_sab, car, mod_car
    forca = int(forca) + int(n)
    dest = int(dest) + int(n)
    const = int(const) + int(n)
    inte = int(inte) + int(n)
    sab = int(sab) + int(n)
    car = int(car) + int(n)
    mod_for = non(forca)
    mod_des = non(dest)
    mod_con = non(const)
    mod_int = non(inte)
    mod_sab = non(sab)
    mod_car = non(car)

def alt_choose(number):
    e1 = int(inputer(f'Escolha +{number} em 1 atributo: \n1 para Força \n2 para Destreza \n3 para Constituição \n4 para Inteligência \n5 para Sabedoria \n6 para Carisma \n: '))
    n = 1 
    
    if e1 == 1:
        alt_for(n)
    elif e1 == 2:
        alt_des(n)
    elif e1 == 3:
        alt_con(n)
    elif e1 == 4:
        alt_int(n)
    elif e1 == 5:
        alt_sab(n)
    elif e1 == 6:
        alt_car(n)
    else:
        print('Atributo Inválido...')
        return e1

    e2 = int(inputer('Escolha outro atributo: '))

    if e2 == 1:
        alt_for(n)
    elif e2 == 2:
        alt_des(n)
    elif e2 == 3:
        alt_con(n)
    elif e2 == 4:
        alt_int(n)
    elif e2 == 5:
        alt_sab(n)
    elif e2 == 6:
        alt_car(n)
    else:
        print('Atributo Inválido...')
        return e2

def main():
    from racesdd import raca
    if raca == 1:
        raca.anao()
    elif raca == 2:
        raca.elfo()
    elif raca == 3:
        raca.halfling()
    elif raca == 4:
        raca.humano()
    elif raca == 5:
        raca.draconato()
    elif raca == 6:
        raca.gnomo()
    elif raca == 7:
        raca.meio_elfo()
    elif raca == 8:
        raca.meio_orc()
    elif raca == 9:
        raca.tiefling()
    else:
        print('Raça não encontrada')
        return raca

main()