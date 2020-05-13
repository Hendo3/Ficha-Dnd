import time, math

def inputer(message):
    inputer = input(message)
    return inputer

def mod(atributo):
    mod = int(atributo) - 10
    fm = mod / 2
    j = round(fm)
    if fm == float():
        j
    else:
        return j
nome = inputer('Nome do personagem: ')
classe = inputer('Classe: ')
raca = inputer('Digite sua raça: ')
ca = int(inputer('Digite sua C.A: '))

forca = inputer('Digite o valor da Força: ')
mod_for = mod(int(forca))

dest = inputer('Digite o valor da Destreza: ')
mod_des = mod(int(dest))
    
const = inputer('Digite o valor da Constituição: ')
mod_con = mod(int(const))

inte = inputer('Digite o valor da Inteligência: ')
mod_int = mod(int(inte))

sab = inputer('Digite o valor da Sabedoria: ')
mod_sab = mod(int(sab))

car = inputer('Digite  valor do Carisma: ')
mod_car = mod(int(car))

lvl = int(inputer('Digite o seu Nível: '))
if lvl >= 1 <=4 :
    proe = 2
elif lvl >= 5 <= 8:
    proe = 3
elif lvl >= 9 <= 12:
    proe = 4
elif lvl >= 13 <= 16 :
    proe = 5
else:
    proe = 6

res_for = mod_for + proe
res_des = mod_des + proe
res_con = mod_con + proe
res_int = mod_int + proe
res_sab = mod_sab + proe
res_car = mod_car + proe

atletismo = res_for

acrobacia = res_des
furtividade = res_des
prestidigitacao = res_des

arcanismo = res_int
investigacao = res_int
natureza = res_int
religiao = res_int
historia = res_int

adestrar = res_sab
intuicao = res_sab
medicina = res_sab
percepcao = res_sab
sobrevivencia = res_sab

atuacao = res_car
enganacao = res_car
intimidacao = res_car
persuasao = res_car

def cab():
    print('Nome do personagem: [', nome, ']')
    print('Classe: [', classe ,']', ' '*5, 'Raça: [', raca, ']')
    print('C.A: [', ca, ']')
    print('_'*10)
    print('')
    print('Atributos')
    print('_'*10)
    print('Força:', forca, '[', mod_for, ']')
    print('Destreza:', dest, '[', mod_des, ']')
    print('Constituição:', const, '[', mod_con, ']')
    print('Inteligência:', inte, '[', mod_int, ']')
    print('Sabedoria:', sab, '[', mod_sab, ']')
    print('Carisma:', car, '[', mod_car, ']')
    print('_'*10)
    print('')
    print('Testes de resistência')
    print('_'*10)
    print('Força:', res_for)
    print('Destreza:', res_des)
    print('Constituição:', res_con)
    print('Inteligência:', res_int)
    print('Sabedoria:', res_sab)
    print('Carisma:', res_car)
    print('')
    print('_'*10)
    print('')
    print('Perícias')
    print('_'*10)
    print('Acrobacia:', acrobacia)
    print('Adestrar Animais:', adestrar)
    print('Arcanismo:', arcanismo)
    print('Atletismo:', atletismo)
    print('Atuação:', atuacao)
    print('Enganação:', enganacao)
    print('Furtividade:', furtividade)
    print('História:', historia)
    print('Intimidação:', intimidacao)
    print('Intuição:', intuicao)
    print('Invtigação:', investigacao)
    print('Medicina:', medicina)
    print('Natureza:', natureza)
    print('Percepção:', percepcao)
    print('Persuasão:', persuasao)
    print('Prestidigitação:', prestidigitacao)
    print('Religião:', religiao)
    print('Sobrevivência:', sobrevivencia
