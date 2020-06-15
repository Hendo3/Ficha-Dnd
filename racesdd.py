def mod(atributo):
    mod = (int(atributo) - 10 ) / 2
    r = round(mod)
    if mod == float():
        r
    else:
        return r

def inputer(message):
    inputer = input(message)
    return inputer

lvl = int(inputer('Nível: '))
def between(a, b):
    if lvl >= int(a) <= int(b):
        return

def proe():
    if between(1, 4):
        proe = 2
        return proe
    elif between(5, 8):
        proe = 3
        return proe
    elif between(9, 12):
        proe = 4
        return proe
    elif between(13, 16):
        proe = 5
        return proe
    else:
        proe = 6
        return proe
print(proe())

nome = inputer('Nome do personagem: ')
classe = inputer('Classe: ')
raca = int(inputer('1 para Anão \n2 para Elfo \n3 para Halfling \n4 para Humano \n5 para Draconato \n6 para Gnomo \n7 para Meio-Elfo \n8 para Meio-Orc \n9 para Tiefling \n- '))
ca = int(inputer('Digite sua C.A: '))
hp = int(inputer('Quantidade de HP: '))

def non(atributo):
    t = mod(atributo)
    global res_for, res_des, res_con, res_int, res_sab, res_car, proe
    
    if mod(atributo) >= int(1):
        res_for = proe() + mod(forca)
        res_des = proe() + mod(dest)
        res_con = proe() + mod(const)
        res_int = proe() + mod(inte)
        res_sab = proe() + mod(sab)
        res_car = proe() + mod(car)
    else:
        t

forca = inputer('Força: ')
mod_for = mod(forca)
print(mod_for)

dest = inputer('Destreza: ')
mod_des = mod(dest)
print(mod_des)

const = inputer('Constituição: ')
mod_con = mod(const)
print(mod_con)

inte = inputer('Inteligência: ')
mod_int = mod(inte)
print(mod_int)

sab = inputer('Sabedoria: ')
mod_sab = mod(sab)
print(mod_sab)

car = inputer('Carisma: ')
mod_car = mod(car)
print(mod_sab)


res_for = proe() + mod_for
res_des = proe() + mod_des
res_con = proe() + mod_con
res_int = proe() + mod_int
res_sab = proe() + mod_sab
res_car = proe() + mod_car

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


class Races():    
    dark = '18 metros na penumbra como se fosse luz plena e no escuro como se fosse penumbra, \nnão pode discernir cores, apenas tons de cinza'
    def anao(self):
        alt_con(int(2))
        desloc = float(7.5)
        sub_raca = int(inputer('Sub-raça: \n1 para Anão da Colina \n2 para Anão da Montanha \n- '))
        cab()
        if sub_raca == 1:
            alt_sab(1)
            cab()
            print(f'\nAnão da colina \n{desloc} \nHabilidades: \n{dark} \nVantagens: \nPossui vantagem em testes de resistência a veneno e resistência contra danos de envenenamento \nIdiomas: \nComum e Anão')
        elif sub_raca == 2:
            alt_for(2)
            cab()
            print(f'\nAnão da montanha \n{desloc} \nHabilidades: \n{dark} \nVantagens: \nPossui vantagem em testes de resistência a veneno e resistência contra danos de envenenamento \nIdiomas: \nComum e Anão')
        else:
            print('\nSub-Raça não encontrada')
            return sub_raca

    def elfo(self):
        alt_des(2)
        sub_raca = int(inputer('Sub_raça: \n1 para Alto elfo \n2 para Elfo da floresta \n3 para Drow(Elfo negro) \n- '))
        if sub_raca == 1:
            alt_int(1)
            desloc = int(9)
            cab()
            print(f'\nAlto elfo \n{desloc} \nHabilidades: \n{dark} \nVantagens: \nPossui um truque da lista de truques de mago, inteligência usado para conjuração \nPode ler, falar e escrever em comum, élfico e um idioma a sua escolha')
        elif sub_raca == 2:
            alt_sab(1)
            desloc = float(10.5)
            cab()
            print(f'\nElfo da floresta \n{desloc} \nHabilidades: \nPode tentar se esconder mesmo quando estiver levemente obscurecido \npor folhagem, chuva forte, neve caindo, névoa \nou qualquer outr fenômeno natural \nIdioma: \nComum e Élfico')
        elif sub_raca == 3:
            alt_car(1)
            desloc = int(9)
            cab()
            print(f'\nDrow(Elfo negro) \n{desloc} \nHabilidades: \nVisão noturna até 36 metros como se fosse luz plena \nPossui desvangem em testes relacionados a visão \nquando você ou qualquer que seja o alvo estiver \nsob luz solar direta \nAo atingir o Nível 3 adquire Globos de luz \nAo atingir o Nível 5 adquire Escuridão /nPrecisa realizar descanso longo antes de usar magias do traço novamente \nIdioma: \nComum e Élfico')
        else:
            print('\nSub_raça não encontrada')
            return sub_raca

    def halfling(self):
        alt_des(2)
        desloc = float(7.5)
        sub_raca = int(inputer('Sub-raça: \n1 para Pés leves \n2 para Robusto \n- '))
        if sub_raca == 1:
            alt_car(1)
            cab()
            print(f'\nHalflin pés leves \n{desloc} \nHabilidades: \nQuando tirar 1 natural em jogadas de ataque, testes de habilidade ou resistência \npode jogar novamente o dado e deve usar o novo resultado \ndeve realizar descanso longo para utilizar novamente \nPossui vantagem em testes contra amedrontamento \nPode se mover através do espaço de qalquer criatra maior que ele \nPode tentar se esconder quando esconder quando estiver atrás de uma criatura \nIdioma: \nComum e Halfling')
        elif sub_raca == 2:
            alt_con(1)
            cab()
            print(f'\nHalflin pés leves \n{desloc}\nHabilidades: \nQuando tirar 1 natural em jogadas de ataque, testes de ha0bilidade ou resistência \npode jogar novamente o dado e deve usar o novo resultado \ndeve realizar descanso longo para utilizar novamente \nPossui vantagem em testes contra amedrontamento \nPode se mover através do espaço de qalquer criatra maior que ele \nPossui vantagem em testes contra veneno e dano de envenenamento')
        else:
            print('\nSub-raça não encontrada')
            return sub_raca

    def humano(self):
        desloc = int(9)
        alt_all(1)
        cab()
        print(f'\nHumano: \n{desloc} \nIdioma: \nComum e um a sua escolha')

    def draconato(self):
        alt_for(2)
        alt_car(1)
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
            print(f'\nDraconato Azul \n{desloc} \nHabilidades: \n{lol} elétrica {destre} \n{cd} \n(dano) \nResistência a dano Elétrico {idioma}')
        elif anc == 2:
            cab()
            print(f'\nDraconato Branco \n{desloc} \nHabilidades: \n{lol} de frio {con} \n{cd} \n{dano} \nResistência a dano de Frio \n{idioma}')
        elif anc == 3:
            cab()
            print(f'\nDraconato Bronze \n{desloc}  \nHabilidades: \n{lol} elétrica {destre} \n{cd} \n{dano} \nResistência a danos Elétrico \n{idioma}')
        elif anc == 4:
            cab()
            print(f'\nDraconato Cobre \n{desloc}  \nHabilidades: \n{lol} acída {destre} \n{cd} \n{dano} \nResistência a dano Acído \n{idioma}')
        elif anc == 5:
            cab()
            print(f'\nDraconato Latão \n{desloc}  \nHabilidades: \n{lol} de fogo {destre} \n{cd} \n{dano} \nResistência a dano de Fogo \nidioma')
        elif anc == 6:
            cab()
            print(f'\nDraconato Negro \n{desloc}  \nHabilidades: \n{lol} acído {destre} \n{cd} {de} \n{dano} \nResistência a dano Acído \n{idioma}')
        elif anc == 7:
            cab()
            print(f'\nDraconato Ouro \n{desloc}  \nHabilidades: \n{lol} de fogo {de} \n{cd} \n{dano} \nResistência a dano de Fogo \n{idioma}')
        elif anc == 8:
            cab()
            print(f'\nDraconato Prata \n{desloc}  \nHabilidades: \n{lol} de frio {con} \n{cd} \n{dano} \nResistência a dano de frio \n{idioma}')
        elif anc == 9:
            cab()
            print(f'\nDraconato Verde \n{desloc}  \nHabilidades: \n{lol} de veneno {con} \n{cd} \n{dano} \nResistência a dano Venenoso \n{idioma}')
        elif anc == 10:
            cab()
            print(f'\nDraconato Vermelho \n{desloc}  \nHabilidades: \n{lol} de fogo {de} \n{cd} \n{dano} \nResistência a dano de Fogo \n{idioma}')
        else:
            print('\nAncestral não encontrado')
            return anc

    def gnomo(self):
        alt_int(2)
        desloc = int(9)
        sub_raca = int(inputer('Sub-Raça: \n1 para Gnomo da Floresta \n2 para Gnomo das Rochas \n- '))
        if sub_raca == 1:
            alt_des(2)
            cab()
            print(f'\nGnomo da Floresta: \n{desloc}  \nHabilidades: \nVantagem em testes de resistência em testes de inteligência, sabedoria e carisma contra magias \n{dark} \nPossui o truque Ilusão menor, usa Inteligência \nAtravés de sons e gestos, você pode comunicar ideias simples para Bestas pequenas ou menores')
        elif sub_raca == 2:
            alt_con(1)
            cab()
            print(f'\nGnomo das Montanhas: \n{desloc}  \nHabilidades: \nVantagem em testes de resistência em testes de inteligência, sabedoria e carisma contra magias \n{dark} \nUsa o dobro de proeficiência em testes de história relacionado a itens mágicos, \nobjetos alquímicos ou mecânismos tecnologicos \nPode gastar 1 hora e 10 PO para criar um mecanismo pequeno(5 C.A, 1 HP, \npara de funcionar em 24h a menos que \ngaste 1h reparando-o, pode er até 3 fucionando simultâneamente')
        
    def meio_elfo(self):
        alt_car(2)
        alt_choose(1)
        desloc = int(9)
        cab()
        print(f'Meio-Elfo \n{desloc}  \nHabilidades: \nVantagem em teste de resistência a encantamento \nNão pode ser colocado pra dormir por magia \n{dark} \nIdiomas: \nComum, Élfico e outro a sua escolha')

    def meio_orc(self):
        alt_for(2)
        alt_con(1)
        desloc = int(9)
        cab()
        print(f'Meio-Orc \n{desloc}  \nHabilidades: \n quando atingir 0 de HP serm morrer, retorna com 1 de HP \nAo acertar um golpe crítico em algum golpe corpo-a-corpo \npode rolar dois dados de ataque extra \n{dark} \nIdioma: Comum e Orc')

    def tiefling(self):
        alt_int(1)
        alt_car(2)
        desloc = int(9)
        tr = 'Possui o truque Tramaturgia'
        lvl3 = 'Ao atingir o nível 3 adquire Repreensão infernal como uma magia de nível 2'
        lvl5 = 'Ao atingir o nível 5 adquire Escuridão \nPode utilizar magias desse traço 1 vez por descanso longo'
        cab()
        print(f'Tiefling \n{desloc}  \nHabilidades: \nPossui resistência contra dano de fogo \n{tr} \n{lvl3} \n{lvl5} \nIdioma: \nComum e Infernal')

def cab():
    print(f'Nome do personagem: [{nome}] \nPontos de vida: [{hp}]', ' '*5, f'C.A: [{ca}]')
    print('_'*10)
    print('')
    print('Atributos')
    print('_'*10)
    print(f'Força: {forca} \n{mod_for} \nDestreza: {dest} \n{mod_des} \nConstituição: {const} \n{mod_con} \nInteligência: {inte} \n{mod_int} \nSabedoria: {sab} \n{mod_sab} \nCarisma: {car} \n{mod_car}')
    print('_'*10)
    print('')
    print('Testes de resistência')
    print('_'*10)
    print(f'Força: {res_for} \nDestreza: {res_des} \nConstituição: {res_con} \nInteligência: {res_int} \nSabedoria: {res_sab} \nCarisma: {res_car}')
    print('')
    print('_'*10)
    print('')
    print('Perícias')
    print('_'*10)
    print(f'Acrobacia {acrobacia} \nAdestrar Animais: {adestrar} \nArcanismo: {arcanismo} \nAtletismo: {atletismo} \nAtuação: {atuacao} \nEnganação: {enganacao} \nFurtividade: {furtividade} \nHistória: {historia} \nIntimidação: {intimidacao} \nIntuição: {intuicao} \nInvestigação: {investigacao} \nMedicina: {medicina} \nNatureza: {natureza} \nPercepção: {percepcao} \nPersuasão: {persuasao} \nPrestidigitação {prestidigitacao} \nReligião: {religiao} \nSobrevivência: {sobrevivencia}')
    