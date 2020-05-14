import time, math

dark = '18 metros na penumbra como se fosse luz plena e no escuro como se fosse penumbra, \nnão pode discernir cores, apenas tons de cinza'

def inputer(message):
    inputer = input(message)
    return inputer

def mod(atributo):
    mod = int(atributo) - 10
    fm = mod / 2
    j = round(fm)
    if fm == 0:
        fm = 'Zero'
    elif fm == float():
        j
    else:
        return j
    
nome = inputer('Nome do personagem: ')
classe = inputer('Classe: ')
raca = int(inputer('1 para Anão \n2 para Elfo \n3 para Halfling \n4 para Humano \n5 para Draconato \n6 para Gnomo \n7 para Meio-Elfo \n8 para Meio-Orc \n9 para Tiefling \n- '))
ca = int(inputer('Digite sua C.A: '))
hp = int(inputer('Quantidade de HP: '))

forca = inputer('Força: ')
mod_for = mod(int(forca))

dest = inputer('Destreza: ')
mod_des = mod(int(dest))
    
const = inputer('Constituição: ')
mod_con = mod(int(const))

inte = inputer('Inteligência: ')
mod_int = mod(int(inte))

sab = inputer('Sabedoria: ')
mod_sab = mod(int(sab))

car = inputer('Carisma: ')
mod_car = mod(int(car))

lvl = int(inputer('Nível: '))
if lvl >= 1 <= 4:
    proe = 2
elif lvl >= 5 <= 8:
    proe = 3
elif lvl >= 9 <= 12:
    proe = 4
elif lvl >= 13 <= 16:
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
    desloc = float(7.5)
    sub_raca = int(inputer('Sub-raça: \n1 para Anão da Colina \n2 para Anão da Montanha \n- '))
    cab()
    if sub_raca == 1:
        cab()
        print(f'\nAnão da colina \nHabilidades: \n{dark} \nVantagens: \nPossui vantagem em testes de resistência a veneno e resistência contra danos de envenenamento \nIdiomas: \nComum e Anão')
    elif sub_raca == 2:
        cab()
        print(f'\nAnão da montanha \nHabilidades: \n{dark} \nVantagens: \nPossui vantagem em testes de resistência a veneno e resistência contra danos de envenenamento \nIdiomas: \nComum e Anão')
    else:
        print('\nSub-Raça não encontrada')
        return sub_raca

def elfo():
    sub_raca = inputer('Sub_raça: \n1 para Alto elfo \n2 para Elfo da floresta \n3 para Drow(Elfo negro) \n- ')
    if sub_raca == 1:
        desloc = int(9)
        cab()
        print(f'\nAlto elfo \nHabilidades: \n{dark} \nVantagens: \nPossui um truque da lista de truques de mago, inteligênvia usado para conhuração \nPode ler, falar e escrever em comum, élfico e um idioma a sua escolha')
    elif sub_raca == 2:
        desloc = float(10.5)
        cab()
        print(f'\nElfo da floresta \nHabilidades: \nPode tentar se esconder mesmo quando estiver levemente obscurecido \npor folhagem, chuva forte, neve caindo, névoa \nou qualquer outr fenômeno natural \nIdioma: \nComum e Élfico')
    elif sub_raca == 3:
        desloc = int(9)
        cab()
        print(f'\nDrow(Elfo negro) \nHabilidades: \nVisão noturna até 36 metros como se fosse luz plena \nPossui desvangem em testes relacionados a visão \nquando você ou qualquer que seja o alvo estiver \nsob luz solar direta \nAo atingir o Nível 3 adquire Globos de luz \nAo atingir o Nível 5 adquire Escuridão /nPrecisa realizar descanso longo antes de usar magias do traço novamente \nIdioma: \nComum e Élfico')
    else:
        print('\nSub_raça não encontrada')
        return sub_raca

def halfling():
    desloc = float(7.5)
    sub_raca = inputer('Sub-raça: \n1 para Pés leves \n2 para Robusto \n- ')
    if sub_raca == 1:
        cab()
        print('\nHalflin pés leves \nHabilidades: \nQuando tirar 1 natural em jogadas de ataque, testes de habilidade ou resistência \npode jogar novamente o dado e deve usar o novo resultado \ndeve realizar descanso longo para utilizar novamente \nPossui vantagem em testes contra amedrontamento \nPode se mover através do espaço de qalquer criatra maior que ele \nPode tentar se esconder quando esconder quando estiver atrás de uma criatura \nIdioma: \nComum e Halfling')
    elif sub_raca == 2:
        cab()
        print('\nHalflin pés leves \nHabilidades: \nQuando tirar 1 natural em jogadas de ataque, testes de habilidade ou resistência \npode jogar novamente o dado e deve usar o novo resultado \ndeve realizar descanso longo para utilizar novamente \nPossui vantagem em testes contra amedrontamento \nPode se mover através do espaço de qalquer criatra maior que ele \nPossui vantagem em testes contra veneno e dano de envenenamento')
    else:
        print('\nSub-raça não encontrada')
        return sub_raca

def humano():
    desloc = int(9)
    cab()
    print('\nHumano: \nIdioma: \nComum e um a sua escolha')

def draconato():
    desloc = int(9)
    anc = int(inputer('Selecione seu ancestral Draconico: \n1 para Azul(Elétrico) \n2 para Branco(Frio) \n3 para Bronze(Elétrico) \n4 para Cobre(Acído) \n5 para Latão(Fogo) \n6 para Negro(Acído) \n7 para Ouro(Fogo) \n8 para Prata(Frio) \n9 para Verde(Veneno) \n10 para Vermelho(Fogo) \n- '))
    lol = 'Você pode usar uma Ação para exalar energia destrutiva'
    idioma = 'Idioma: \nComum e Dracônico'
    destre = 'Linha de 1.5/9 metros (Teste de Destreza)'
    con = 'Cone de 4.5 metros (Testede Constituição)'
    de = 'Cone de 4.5 metros (Teste de Destreza)'
    cd = 'CD 8 + modificador de Constituição + bônus de proeficiência'
    dano = 'Uma criatura sofre 2d6 de dano num fracasso e metade disso num sucesso \nO dano aumenta para 3d6 no nível 6, 4d6 no nível 11 e 5d6 no nível 16 \nApós o uso é preciso realizar descanso curto/longo '
    if anc == 1:
        cab()
        print(f'\nDraconato Azul \nHabilidades: \n{lol} elétrica {destre} \n{cd} \n(dano) \nResistência a dano Elétrico {idioma}')
    elif anc == 2:
        cab()
        print(f'\nDraconato Branco \nHabilidades: \n{lol} de frio {con} \n{cd} \n{dano} \nResistência a dano de Frio \n{idioma}')
    elif anc == 3:
        cab()
        print(f'\nDraconato Bronze \nHabilidades: \n{lol} elétrica {destre} \n{cd} \n{dano} \nResistência a danos Elétrico \n{idioma}')
    elif anc == 4:
        cab()
        print(f'\nDraconato Cobre \nHabilidades: \n{lol} acída {destre} \n{cd} \n{dano} \nResistência a dano Acído \n{idioma}')
    elif anc == 5:
        cab()
        print(f'\nDraconato Latão \nHabilidades: \n{lol} de fogo {destre} \n{cd} \n{dano} \nResistência a dano de Fogo \nidioma')
    elif anc == 6:
        cab()
        print(f'\nDraconato Negro \nHabilidades: \n{lol} acído {destre} \n{cd} {de} \n{dano} \nResistência a dano Acído \n{idioma}')
    elif anc == 7:
        cab()
        print(f'\nDraconato Ouro \nHabilidades: \n{lol} de fogo {de} \n{cd} \n{dano} \nResistência a dano de Fogo \n{idioma}')
    elif anc == 8:
        cab()
        print(f'\nDraconato Prata \nHabilidades: \n{lol} de frio {con} \n{cd} \n{dano} \nResistência a dano de frio \n{idioma}')
    elif anc == 9:
        cab()
        print(f'\nDraconato Verde \nHabilidades: \n{lol} de veneno {con} \n{cd} \n{dano} \nResistência a dano Venenoso \n{idioma}')
    elif anc == 10:
        cab()
        print(f'\nDraconato Vermelho \nHabilidades: \n{lol} de fogo {de} \n{cd} \n{dano} \nResistência a dano de Fogo \n{idioma}')
    else:
        print('\nAncestral não encontrado')
        return anc
    
    

              
def main():
    if raca == 1:
        anao()
    elif raca == 2:
        elfo()
    elif raca == 3:
        halfling()
    elif raca == 4:
        humano()
    elif raca == 5:
        draconato()
    elif raca == 6:
        gnomo()
    elif raca == 7:
        meio_elfo()
    elif raca == 8:
        eio_orc()
    elif raca == 9:
        tiefling()
    else:
        print('later')


main()
