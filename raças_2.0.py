import math
from updatedFicha import *
vl = Values()

def inputer(message):
    return input(message)

nivel = vl.level()

raw_str = is_int(inputer("Força: "))
raw_dex = is_int(inputer("Destreza: "))
raw_con = is_int(inputer("Constituição: "))
raw_int = is_int(inputer("Inteligência: "))
raw_wis = is_int(inputer("Sabedoria: "))
raw_cha = is_int(inputer("Carisma: "))


def table_skills(strength, dexterity, intelligence, wisdom, charisma):
    '''
    cria a lista de skills
    '''
    space = " "*3
    print(f"Acrobacia: [{dexterity}] {space} Arcanismo: [{intelligence}] {space} Atletismo: [{strength}] \nAtuação: [{charisma}] {space} Blefar: [{charisma}] {space} Furtividade: [{dexterity}] \nHistória: [{intelligence}] {space} Intimidação: [{charisma}] {space} Intuição: [{wisdom}] \nInvestigação: [{intelligence}] \nLidar com animais: [{wisdom}] \nMedicina: [{wisdom}]\nNatureza: [{intelligence}] {space} Percepção: [{wisdom}] {space} Persuasão: [{charisma}] \nPrestidigitação: [{dexterity}] {space} Religião: [{intelligence}] {space} Sobrevivência: [{wisdom}]")

def change_all(value, attribute):
    '''
    modifica o valor base, do mod e da skill de um atributo
    ''' 
    n_attribute = vl.change(value, attribute)
    n_attribute_mod = vl.modifier(attribute)
    n_attribute_skill = skill(n_attribute_mod)

    lista_de_attributos = [n_attribute, n_attribute_mod, n_attribute_skill]
    return lista_de_attributos

def in_range(entry, dictionary):
    '''
    verifica se valor existe no dict
    '''
    value = entry
    if value in dictionary:
        return value
    else:
        a = is_int(inputer("Valor não encontrado\nTente novamente: "))
        return in_range(a, dictionary)


def skill(modificador):
    '''
    retorna o valor da skill
    '''
    lista = vl.lvl(nivel)
    if modificador < int(0):
        return modificador + (int(vl.ind(lista))*-1)
    else:
        return modificador + int(vl.ind(lista))

class Races(object):
    dark = '18 metros na penumbra como se fosse luz plena e no escuro como se fosse penumbra, \nnão pode discernir cores, apenas tons de cinza'

    def __init__(self, stre=raw_str, dex=raw_dex, con=raw_con, inte=raw_int, wis=raw_wis, cha=raw_cha):
        self.stre = stre
        self.dex = dex
        self.con = raw_con
        self.inte = inte
        self.wis = wis
        self.cha = cha

        self.stre_mod = vl.modifier(stre)
        self.dex_mod = vl.modifier(dex)
        self.con_mod = vl.modifier(con)
        self.inte_mod = vl.modifier(inte)
        self.wis_mod = vl.modifier(wis)
        self.cha_mod = vl.modifier(cha)

        self.stre_skill = skill(self.stre_mod)
        self.dex_skill = skill(self.dex_mod)
        self.con_skill = skill(self.con_mod)
        self.inte_skill = skill(self.inte_mod)
        self.wis_skill = skill(self.wis_mod)
        self.cha_skill = skill(self.cha_mod)

    def dwarf(self):
        desloc = float(7.5)
        changed_con = change_all(2, raw_con)

        sub_race = is_int(inputer('Sub-raça: \n1 para Anão da Colina \n2 para Anão da Montanha \n- '))

        def colina():
            changed_wis = change_all(1, raw_wis)
            table_skills(self.stre_skill, self.dex_skill, self.inte_skill, changed_wis[2], self.cha_skill)

            return f"Força: {self.stre} [{self.stre_mod}] \nDestreza: {self.dex} [{self.dex_mod}] \nConstituição: {changed_con[0]} [{changed_con[1]}] \nInteligência: {self.inte} [{self.inte_mod}] \nSabedoria: {changed_wis[0]} [{changed_wis[1]}] \nCarisma: {self.cha} [{self.cha_mod}]"

        def montanha():
            change_stre = change_all(2, raw_str)
            table_skills(change_stre[2], self.dex, self.inte, self.wis, self.cha)

            return f"Força: {change_stre[0]} [{change_stre[1]}] \nDestreza: {self.dex} [{self.dex_mod}] \nConstituição: {change_stre[0]} [{change_stre[1]}] \nInteligência: {self.inte} [{self.inte_mod}] \nSabedoria: {self.wis} [{self.wis_mod}] \nCarisma: {self.cha} [{self.cha_mod}]"

        dwarf_races ={
            1:colina,
            2:montanha
        }
        
        end_value = dwarf_races.get(in_range(sub_race, dwarf_races))
        return end_value()

    def elf(self):
        changed_dex = change_all(2, raw_dex)
        sub_race = is_int(inputer('Sub_raça: \n1 para Alto elfo \n2 para Elfo da floresta \n3 para Drow(Elfo negro) \n- '))

        def high_elf():
            desloc = int(9)
            changed_inte = change_all(1, raw_int)
            table_skills(self.stre_skill, changed_dex[2], changed_inte[2], self.wis_skill, self.cha_skill)
            return f"Força: {self.stre} [{self.stre_mod}] \nDestreza: {changed_dex[0]} [{changed_dex[1]}] \nConstituição: {self.con} [{self.con_mod}] \nInteligência: {changed_inte[0]} [{changed_inte[1]}] \nSabedoria: {self.wis} [{self.wis_mod}] \nCarisma: {self.cha} [{self.cha_mod}]"

        def forest_elf():
            desloc = int(12)
            changed_wis = change_all(1, raw_wis)
            table_skills(self.stre_skill, changed_dex[2], self.inte_skill, changed_wis[2], self.cha_skill)

            return f"Força: {self.stre} [{self.stre_mod}] \nDestreza: {changed_dex[0]} [{changed_dex[1]}] \nConstituição: {self.con} [{self.con_mod}] \nInteligência: {self.inte} [{self.inte}] \nSabedoria: {changed_wis[0]} [{changed_wis[1]}] \nCarisma: {self.cha} [{self.cha_mod}]"

        def dark_elf():
            desloc = int(9)
            changed_cha = change_all(1, raw_cha)
            table_skills(self.stre_skill, changed_dex[2], self.inte_skill, self.wis_skill, changed_cha[2])

            return f"Força: {self.stre} [{self.stre_mod}] \nDestreza: {changed_dex[0]} [{changed_dex[1]}] \nConstituição: {self.con} [{self.con_mod}] \nInteligência: {self.inte} [{self.inte}] \nSabedoria: {self.wis} [{self.wis_mod}] \nCarisma: {changed_cha[0]} [{changed_cha[1]}]"

        elf_races = {
            1:high_elf,
            2:forest_elf,
            3:dark_elf
        }

        end_value = elf_races.get(in_range(sub_race, elf_races))
        return end_value()

    def halfling(self):
        desloc = int(9)
        changed_dex = change_all(2, raw_dex)
        sub_race = is_int(inputer('Sub-raça: \n1 para Pés leves \n2 para Robusto \n- '))

        def pe_leve():
            changed_cha = change_all(1, raw_cha)
            table_skills(self.stre_skill, changed_dex[2], self.inte_skill, self.wis_skill, changed_cha[2])
            return f"Força: {self.stre} [{self.stre_mod}] \nDestreza: {changed_dex[0]} [{changed_dex[1]}] \nConstituição: {self.con} [{self.con_mod}] \nInteligência: {self.inte} [{self.inte_mod}] \nSabedoria: {self.wis} [{self.wis_mod}] \nCarisma: {changed_cha[0]} [{changed_cha[1]}]"

        def robustos():
            changed_con = change_all(1, raw_con)
            table_skills(self.stre_skill, changed_dex[2], self.inte_skill, self.wis_skill, self.ch_skilla)
            return f"Força: {self.stre} [{self.stre_mod}] \nDestreza: {changed_dex[0]} [{changed_dex[1]}] \nConstituição: {changed_con[0]} [{changed_con[1]}] \nInteligência: {self.inte} [{self.inte_mod}] \nSabedoria: {self.wis} [{self.wis_mod}] \nCarisma: {self.cha} [{self.cha_mod}]"

        halfling_races = {
            1:pe_leve,
            2:robustos
        }

        end_value = halfling_races.get(in_range(sub_race, halfling_races))
        return end_value()

    def human(self):
        stre = change_all(1, raw_str)
        dex = change_all(1, raw_dex)
        con = change_all(1, raw_con)
        inte = change_all(1, raw_int)
        wis = change_all(1, raw_wis)
        cha = change_all(1, raw_wis)

        table_skills(stre[2], dex[2], inte[2], wis[2], cha[2])
        return f"Força: {stre[0]} [{stre[1]}] \nDestreza: {dex[0]} [{dex[1]}] \nConstituição: {con[0]} [{con[1]}] \nInteligência: {inte[0]} [{inte[1]}] \nSabedoria: {wis[0]} [{wis[1]}] \nCarisma: {cha[0]} [{cha[1]}]"

    def dragonborn(self):
        ancestor = is_int(inputer('Selecione seu ancestral Draconico: \n1 para Azul(Elétrico) \n2 para Branco(Frio) \n3 para Bronze(Elétrico) \n4 para Cobre(Ácido) \n5 para Latão(Fogo) \n6 para Negro(Ácido) \n7 para Ouro(Fogo) \n8 para Prata(Frio) \n9 para Verde(Veneno) \n10 para Vermelho(Fogo) \n- '))        
        changed_stre = change_all(2, raw_str)
        
        changed_cha = change_all(1, raw_cha)
        
        stts = f"Força: {changed_stre[0]} [{changed_stre[1]}] \nDestreza: {self.dex} [{self.dex_mod}] \nConstituição: {self.con} [{self.con_mod}] \nInteligência: {self.inte} [{self.inte_mod}] \nSabedoria: {self.wis} [{self.wis_mod}] \nCarisma: {changed_cha[0]} [{changed_cha[1]}]"

        table_skills(changed_stre[2], self.dex_skill, self.inte_skill, self.wis_skill, changed_cha[2])
        
        lol = 'Você pode usar uma Ação para exalar energia destrutiva'
        idioma = 'Idioma: \nComum e Dracônico'
        cd = 'CD 8 + modificador de Constituição + bônus de proeficiência'
        damage = 'Uma criatura sofre 2d6 de dano num fracasso e metade disso num sucesso \nO dano aumenta para 3d6 no nível 6, 4d6 no nível 11 e 5d6 no nível 16 \nApós o uso é preciso realizar descanso curto/longo '
        desloc = int(9)

        colors_list = {1:"Azul", 2:"Branco",3:"Bronze", 4:"Cobre", 5:"Latão", 6:"Negro", 7:"Ouro", 8:"Prata", 9:"Verde", 10:"Vermelho"}
        resist_list = {1:"Cone de 4.5 metros (Teste de Constituição)", 2:"Cone de 4.5 metros (Teste de Destreza)", 3:"Linha de 1.5/9 metros (Teste de Destreza)"}
        lista =  {"Azul":"Elétrico", "Branco":"Frio", "Bronze":"Elétrico", "Cobre":"Ácido", "Latão":"Fogo", "Negro":"Ácido", "Ouro":"Fogo", "Prata":"Frio", "Verde":"Veneno", "Vermelho":"Vermelho"}
        lista2 = {"Veneno":1, "Frio":1, "Fogo":2, "Elétrico":2, "Negro":3}
        
        cor = colors_list.get(in_range(ancestor, colors_list))
        dano = lista.get(cor, lambda:"invalid")

        if cor == "Negro":
            val = lista2.get(cor)
        else:
            val1 = lista.get(cor)
            val = lista2.get(val1)

        resistencia = resist_list.get(val)
        return f"{stts} \nDraconato {cor} \n{desloc} \n{lol} de dano {dano} \n{cd} \n{damage} \n{idioma}"

    def gnome(self):
        desloc = int(9)
        changed_int = change_all(2, raw_int)
        sub_race = is_int(inputer('Sub-Raça: \n1 para Gnomo da Floresta \n2 para Gnomo das Rochas \n- '))

        def forest():
            changed_dex = change_all(2, raw_dex)
            table_skills(self.stre_skill, changed_dex[2], changed_int[2], self.wis_skill, self.cha_skill)

            return f"Força: {self.stre} [{self.stre_mod}] \nDestreza: {changed_dex[0]} [{changed_dex[1]}] \nConstituição: {self.con} [{self.con_mod}] \nInteligência: {changed_int[0]} [{changed_int[1]}] \nSabedoria: {self.wis} [{self.wis_mod}] \nCarisma: {self.cha} [{self.cha_mod}]"

        def mountain():
            changed_con = change_all(1, raw_con)
            table_skills(self.stre_skill, self.dex_skill, changed_int[2], self.wis_skill, self.cha_skill)

            return f"Força: {self.stre} [{self.stre_mod}] \nDestreza: {self.dex} [{self.dex_mod}] \nConstituição: {changed_con[0]} [{changed_con[1]}] \nInteligência: {self.inte} [{self.inte_mod}] \nSabedoria: {self.wis} [{self.wis_mod}] \nCarisma: {self.cha} [{self.cha_mod}]"

        gnome_races = {
            1:forest,
            2:mountain
            }

        end_value = gnome_races.get(in_range(sub_race, gnome_races))
        return end_value()

    def half_elf(self):
        desloc = int(9)
        select = is_int(inputer("Escolha 1 atributo: \n1 para Força \n2 para Destreza \n3 para Constituição \n4 para Inteligência \n5 para Sabedoria \n- "))
        flag = False
        changed_cha = change_all(2, raw_cha)
        
        while flag == False:

            if select == 1:
                self.stre +=1
                flag = True
            elif select == 2:
                self.dex +=1
                flag = True
            elif select == 3:
                self.con +=1
                flag = True
            elif select == 4:
                self.inte +=1
                flag = True
            elif select == 5:
                self.wis +=1
                flag = True
            else:
                select = is_int(inputer("Error. Try again: "))

        table_skills(self.stre_skill, self.dex_skill, self.inte_skill, self.wis_skill, self.cha_skill)
        return f"Força: {self.stre} [{self.stre_mod}] \nDestreza: {self.dex} [{self.dex_mod}] \nConstituição: {self.con} [{self.con_mod}] \nInteligência: {self.inte} [{self.inte_mod}] \nSabedoria: {self.wis} [{self.wis_mod}] \nCarisma: {self.cha} [{self.cha_mod}]"

    def half_orc(self):
        desloc = int(9)
        changed_stre = change_all(2, raw_str)
        changed_con = change_all(1, raw_con)
        table_skills(changed_stre[2], self.dex_skill, self.inte_skill, self.wis_skill, self.cha_skill)

        return f"Força: {changed_stre[0]} [{changed_stre[1]}] \nDestreza: {self.dex} [{self.dex_mod}] \nConstituição: {changed_con[0]} [{changed_con[1]}] \nInteligência: {self.inte} [{self.inte_mod}] \nSabedoria: {self.wis} [{self.wis_mod}] \nCarisma: {self.cha} [{self.cha_mod}]"

    def tiefling(self):
        desloc = int(9)
        tr = 'Possui o truque Tramaturgia'
        lvl3 = 'Ao atingir o nível 3 adquire Repreensão infernal como uma magia de nível 2'
        lvl5 = 'Ao atingir o nível 5 adquire Escuridão \nPode utilizar magias desse traço 1 vez por descanso longo'

        changed_inte = change_all(1, raw_int)
        changed_cha = change_all(2, raw_cha)

        table_skills(self.stre_skill, self.dex_skill, changed_inte[2], self.wis_skill, changed_cha[2])
        return f"Força: {self.stre} [{self.stre_mod}] \nDestreza: {self.dex} [{self.dex_mod}] \nConstituição: {self.con} [{self.con_mod}] \nInteligência: {changed_inte[0]} [{changed_inte[1]}] \nSabedoria: {self.wis} [{self.wis_mod}] \nCarisma: {changed_cha[0]} [{changed_cha[1]}] \nHabilidades: {tr} \n{lvl3} \n{lvl5}"


def return_shet():
    '''
    cria a base da ficha
    '''
    
    r = Races()
    races = {
        1:r.dwarf,
        2:r.elf,
        3:r.halfling,
        4:r.human,
        5:r.dragonborn,
        6:r.gnome,
        7:r.half_elf,
        8:r.half_orc,
        9:r.tiefling
    }

    names = {
        r.dwarf:"Anão",
        r.elf:"Elfo",
        r.halfling:"Halfling",
        r.human:"Humano",
        r.dragonborn:"Draconato",
        r.gnome:"Gnomo",
        r.half_elf:"Meio Elfo",
        r.half_orc:"Meio Orc",
        r.tiefling:"Tiefling"
    }
    race_choosen = in_range(vl.race(),races)
    race = races.get(in_range(race_choosen, races))
    race_name = names.get(in_range(race, names))

    def race_sheet():
        return race()

    def name_place():
        space = " "*3

        name = vl.name()
        hp = vl.final_life(vl.modifier(raw_con))
        ca = vl.armor_class()

        race = race_name
        classe = "WORKING HERE"
        return f"Nome: {name} {space} Nível: {nivel} {space} \nRaça: {race} {space} Classe: {classe} \nHp Total: {hp} {space} Classe de armadura: {ca}"

    print(name_place())
    print(race_sheet())


return_sheet()
