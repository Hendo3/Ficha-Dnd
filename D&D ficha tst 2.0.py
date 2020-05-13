import time, math

anao = ['Anão', 'anão', 'anao', 'Anao']
elfo = ['Elfo', 'elfo']
half = ['Halfling', 'halfling']
huma = ['Humano', 'humano']
drac = ['Draconato', 'draconato']
gnom = ['Gnomo', 'gnomo']
miel = ['Meio-Elfo', 'meio-elfo', 'Meio-elfo', 'meio-Elfo', 'Meio Elfo', 'meio elfo', 'Meio elfo', 'meio Elfo']
morc = ['Meio-Orc', 'Meio-orc', 'meio-Orc', 'meio-orc', 'Meio Orc', 'Meio orc', 'meio Orc', 'meio orc', 'Orc', 'orc']
tief = ['Tiefling', 'tiefling']
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
raca = inputer('Digite sua raça: ')
ca = int(inputer('Digite sua C.A: '))
hp = inputer('Quantidade de HP: ')

raca_for = 0
raca_des = 0
raca_con = 0
raca_int = 0
raca_sab = 0
raca_car = 0

forca = inputer('Digite o valor da Força: ')
re_forca = int(forca) + raca_for
mod_for = mod(int(re_forca))

dest = inputer('Digite o valor da Destreza: ')
re_dest = int(dest) + raca_des
mod_des = mod(int(re_dest))
    
const = inputer('Digite o valor da Constituição: ')
re_const = int(const) + raca_con
mod_con = mod(int(re_const))

inte = inputer('Digite o valor da Inteligência: ')
re_inte = int(inte) + raca_int
mod_int = mod(int(re_inte))

sab = inputer('Digite o valor da Sabedoria: ')
re_sab = int(sab) + raca_sab
mod_sab = mod(int(re_sab))

car = inputer('Digite  valor do Carisma: ')
re_car = int(sab) + raca_sab
mod_car = mod(int(re_car))

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

def anao():
    colina = ['Colina', 'colina']
    montanha = ['Montanha', 'montanha']
    raca_con = 2
    desloc = float(7.5)
    sub_raca = inputer(f'Digite sua sub-raça: ')
    if sub_raca in colina:
        raca_sab = 1
        cab()
        print(f'Anão da colina /n Habilidades: \n{dark} \nVantagens: \nPossui vantagem em testes de resistência a veneno e resistência contra danos de envenenamento \nIdiomas: \nComum e Anão')
    elif sub_raca in montanha:
        raca_for = 2
        cab()
        print(f'Anão da montanha /n Habilidades: \n{dark} \nVantagens: \nPossui vantagem em testes de resistência a veneno e resistência contra danos de envenenamento \nIdiomas: \nComum e Anão')
    else:
        print('Sub-Raça não encontrada')

def cab():
    print(f'Nome do personagem: [{nome}]')
    print(f'Classe: [{classe}]', ' '*5, f'Raça: [{raca}]', ' '*5, f'Pontos de vida: [{hp}]')
    print(f'C.A: [{ca}]')
    print('_'*10)
    print('')
    print('Atributos')
    print('_'*10)
    print(f'Força: {re_forca} \n{mod_for}')
    print(f'Destreza: {re_dest} \n{mod_des}')
    print(f'Constituição: {re_const} \n{mod_con}')
    print(f'Inteligência: {re_inte} \n{mod_int}')
    print(f'Sabedoria: {re_sab} \n[{mod_sab}]')
    print(f'Carisma: {re_car} \n[{mod_car}]')
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


def main():
    if(raca in anao):
        anao()
    else:
        print('later')


main()
