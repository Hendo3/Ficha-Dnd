import time, math

dark = '18 metros na penumbra como se fosse luz plena e no escuro como se fosse penumbra, \nnão pode discernir cores, apenas tons de cinza'

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
raca = int(inputer('1 para Anão \n2 para Elfo \n3 para Halfling \n4 para Humano \n5 para Draconato \n6 para Gnomo \n7 para Meio-Elfo \n8 para Meio-Orc \n9 para Tiefling \n- '))
ca = int(inputer('Digite sua C.A: '))
hp = inputer('Quantidade de HP: ')

forca = int(inputer('Força: '))
mod_for = mod(int(forca))

dest = int(inputer('Destreza: '))
mod_des = mod(int(dest))
    
const = int(inputer('Constituição: '))
mod_con = mod(int(const))

inte = int(inputer('Inteligência: '))
mod_int = mod(int(inte))

sab = int(inputer('Sabedoria: '))
mod_sab = mod(int(sab))

car = int(inputer('Carisma: '))
mod_car = mod(int(car))

lvl = int(inputer('Nível: '))

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
    print(f'Nome do personagem: [{nome}]')
    print(f'Classe: [{classe}]', ' '*5, f'Raça: [{raca}]', ' '*5, f'Pontos de vida: [{hp}]')
    print(f'C.A: [{ca}]')
    print('_'*10)
    print('')
    print('Atributos')
    print('_'*10)
    print(f'Força: {forca} \n{mod_for}')
    print(f'Destreza: {dest} \n{mod_des}')
    print(f'Constituição: {const} \n{mod_con}')
    print(f'Inteligência: {inte} \n{mod_int}')
    print(f'Sabedoria: {sab} \n{mod_sab}')
    print(f'Carisma: {car} \n{mod_car}')
    print('_'*10)
    print('')
    print('Testes de resistência')
    print('_'*10)
    print(f'Força: {res_for}')
    print(f'Destreza: {res_des}')
    print(f'Constituição: {res_con}')
    print(f'Inteligência: {res_int}')
    print(f'Sabedoria: {res_sab}')
    print(f'Carisma: {res_car}')
    print('')
    print('_'*10)
    print('')
    print('Perícias')
    print('_'*10)
    print(f'Acrobacia {acrobacia}')
    print(f'Adestrar Animais: {adestrar}')
    print(f'Arcanismo: {arcanismo}')
    print(f'Atletismo: {atletismo}')
    print(f'Atuação: {atuacao}')
    print(f'Enganação: {enganacao}')
    print(f'Furtividade: {furtividade}')
    print(f'História: {historia}')
    print(f'Intimidação: {intimidacao}')
    print(f'Intuição: {intuicao}')
    print(f'Invtigação: {investigacao}')
    print(f'Medicina: {medicina}')
    print(f'Natureza: {natureza}')
    print(f'Percepção: {percepcao}')
    print(f'Persuasão: {persuasao}')
    print(f'Prestidigitação {prestidigitacao}')
    print(f'Religião: {religiao}')
    print(f'Sobrevivência: {sobrevivencia}')

def anao():
    global const
    const= int(const)
    const += 2
    desloc = float(7.5)
    sub_raca = int(inputer(f'Digite sua sub-raça: \n1 para Anão da Colina \n2 para Anão da Montanha \n- '))
    cab()
    #if sub_raca == 1:
    #    global raca_sab
    #    raca_sab = int(sab)
    #    raca_sab += 1
    #    cab()
    #    print(f'Anão da colina \nHabilidades: \n{dark} \nVantagens: \nPossui vantagem em testes de resistência a veneno e resistência contra danos de envenenamento \nIdiomas: \nComum e Anão')
    #elif sub_raca == 2:
    #    global raca_for
    #    raca_for = int(forca)
    #    raca_for += 2
    #    cab()
    #    print(f'Anão da montanha \nHabilidades: \n{dark} \nVantagens: \nPossui vantagem em testes de resistência a veneno e resistência contra danos de envenenamento \nIdiomas: \nComum e Anão')
    #else:
    #    print('Sub-Raça não encontrada')

def main():
    if raca == 1:
        anao()
    elif raca == 2:
        elfo()
    else:
        print('later')


main()
