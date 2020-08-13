import namelad

c = namelad.ChangeValues()
p = namelad.PlayerStats()
h = namelad.Head()
s = namelad.Status()

def inputer(message):
    return input(message)

raw_strength = p.strength()
raw_dexterity = p.dexterity()
raw_constituition = p.constituition()
raw_intelligence = p.intelligence()
raw_wisdom = p.wisdom()
raw_charisma = p.charisma()

class Modifiers():

    def strength_modifier(self, mod=raw_strength):
        return s.mod(int(mod))
        
    def dexterity_modifier(self, mod=raw_dexterity):
        return s.mod(int(mod))

    def constituition_modifier(self, mod=raw_constituition):
        return s.mod(int(mod))

    def intelligence_modifier(self, mod=raw_intelligence):
        return s.mod(int(mod))

    def wisdom_modifier(self, mod=raw_wisdom):
        return s.mod(int(mod))

    def charisma_modifier(self, mod=raw_charisma):
        return s.mod(int(mod))

m = Modifiers()

race_selector = h.race()
name = h.name()
hp = c.life_filler(m.constituition_modifier())
classe = h.p_class()
c_a = h.armor_class()

class Header():

    def name_place():
        space = " "*3

        raças = {
            "1":"Anão",
            "2":"Elfo",
            "3":"Halfling",
            "4":"Humano",
            "5":"Draconato",
            "6":"Gnomo",
            "7":"Meio Elfo",
            "8":"Meio Orc",
            "9":"Tiefling"
        }

        race = raças.get(race_selector, lambda: invalid)   

        return f"Nome: {name} {space} Nível: {namelad.nivel} {space} \nRaça: {race} {space} Classe: {classe} \nHp Total: {hp} {space} Classe de armadura: {c_a}"

class Races():
    dark = '18 metros na penumbra como se fosse luz plena e no escuro como se fosse penumbra, \nnão pode discernir cores, apenas tons de cinza'
    
    def dwarf(self):
        new_constituition = c.change_constituition(2, raw_constituition)
        desloc = float(7.5)
        sub_race  = str(inputer('Sub-raça: \n1 para Anão da Colina \n2 para Anão da Montanha \n- '))

        def colina():
            strength = raw_strength
            dexterity = raw_dexterity
            constituition = new_constituition
            intelligence = raw_intelligence
            wisdom = c.change_wisdom(1, raw_wisdom)
            charisma = raw_charisma

            strength_mod = Modifiers.strength_modifier(strength)
            dexterity_mod = Modifiers.dexterity_modifier(dexterity)
            constituition_mod = Modifiers.constituition_modifier(constituition)
            intelligence_mod = Modifiers.intelligence_modifier(intelligence)
            wisdom_mod = Modifiers.wisdom_modifier(wisdom)
            charisma_mod = Modifiers.charisma_modifier(charisma)

            return f"Força: {strength} [{strength_mod}] \nDestreza: {dexterity} [{dexterity_mod}] \nConstituição: {constituition} [{constituition_mod}] \nInteligência: {intelligence} [{intelligence_mod}] \nSabedoria: {wisdom} [{wisdom_mod}] \nCarisma: {charisma} [{charisma_mod}]"
        
        def montanha():
            strength = c.change_strength(2, raw_strength)
            dexterity = raw_dexterity
            constituition = new_constituition
            intelligence = raw_intelligence
            wisdom = raw_wisdom
            charisma = raw_charisma

            strength_mod = Modifiers.strength_modifier(strength)
            dexterity_mod = Modifiers.dexterity_modifier(dexterity)
            constituition_mod = Modifiers.constituition_modifier(constituition)
            intelligence_mod = Modifiers.intelligence_modifier(intelligence)
            wisdom_mod = Modifiers.wisdom_modifier(wisdom)
            charisma_mod = Modifiers.charisma_modifier(charisma)

            return f"Força: {strength} [{strength_mod}] \nDestreza: {dexterity} [{dexterity_mod}] \nConstituição: {constituition} [{constituition_mod}] \nInteligência: {intelligence} [{intelligence_mod}] \nSabedoria: {wisdom} [{wisdom_mod}] \nCarisma: {charisma} [{charisma_mod}]"

        dwarf_races = {
            "1":colina, 
            "2":montanha
            }

        end_value = dwarf_races.get(sub_race, lambda: "invalid")
        return end_value()

    def elf(self):
        new_dexterity = c.change_dexterity(2, raw_dexterity)
        sub_races = str(inputer('Sub_raça: \n1 para Alto elfo \n2 para Elfo da floresta \n3 para Drow(Elfo negro) \n- '))


        def high_elf():
            desloc = int(9)

            strength = raw_strength
            dexterity = new_dexterity
            constituition = raw_constituition
            intelligence = c.change_intelligence(1, raw_intelligence)
            wisdom = raw_wisdom
            charisma = raw_charisma

            strength_mod = Modifiers.strength_modifier(strength)
            dexterity_mod = Modifiers.dexterity_modifier(dexterity)
            constituition_mod = Modifiers.constituition_modifier(constituition)
            intelligence_mod = Modifiers.intelligence_modifier(intelligence)
            wisdom_mod = Modifiers.wisdom_modifier(wisdom)
            charisma_mod = Modifiers.charisma_modifier(charisma)

            return f"Força: {strength} [{strength_mod}] \nDestreza: {dexterity} [{dexterity_mod}] \nConstituição: {constituition} [{constituition_mod}] \nInteligência: {intelligence} [{intelligence_mod}] \nSabedoria: {wisdom} [{wisdom_mod}] \nCarisma: {charisma} [{charisma_mod}]"

        def florest_elf():
            desloc = int(12)

            strength = raw_strength
            dexterity = new_dexterity
            constituition = raw_constituition
            intelligence = raw_intelligence
            wisdom = c.change_wisdom(1, raw_wisdom)
            charisma = raw_charisma

            strength_mod = Modifiers.strength_modifier(strength)
            dexterity_mod = Modifiers.dexterity_modifier(dexterity)
            constituition_mod = Modifiers.constituition_modifier(constituition)
            intelligence_mod = Modifiers.intelligence_modifier(intelligence)
            wisdom_mod = Modifiers.wisdom_modifier(wisdom)
            charisma_mod = Modifiers.charisma_modifier(charisma)

            return f"Força: {strength} [{strength_mod}] \nDestreza: {dexterity} [{dexterity_mod}] \nConstituição: {constituition} [{constituition_mod}] \nInteligência: {intelligence} [{intelligence_mod}] \nSabedoria: {wisdom} [{wisdom_mod}] \nCarisma: {charisma} [{charisma_mod}]"

        def dark_elf():
            desloc = int(9)
            strength = raw_strength
            dexterity = new_dexterity
            constituition = raw_constituition
            intelligence = raw_intelligence
            wisdom = raw_wisdom
            charisma = c.change_charisma(1, raw_charisma)

            strength_mod = Modifiers.strength_modifier(strength)
            dexterity_mod = Modifiers.dexterity_modifier(dexterity)
            constituition_mod = Modifiers.constituition_modifier(constituition)
            intelligence_mod = Modifiers.intelligence_modifier(intelligence)
            wisdom_mod = Modifiers.wisdom_modifier(wisdom)
            charisma_mod = Modifiers.charisma_modifier(charisma)

            return f"Força: {strength} [{strength_mod}] \nDestreza: {dexterity} [{dexterity_mod}] \nConstituição: {constituition} [{constituition_mod}] \nInteligência: {intelligence} [{intelligence_mod}] \nSabedoria: {wisdom} [{wisdom_mod}] \nCarisma: {charisma} [{charisma_mod}]"

        races = {
            "1":high_elf,
            "2":florest_elf, 
            "3":dark_elf
            }
        end_value = races.get(sub_races, lambda: "invalid")
        return end_value()
        
    def halfling(self):
        new_dexterity = c.change_dexterity(2, raw_dexterity)
        desloc = int(9)
        sub_race = str(inputer('Sub-raça: \n1 para Pés leves \n2 para Robusto \n- '))

        def pe_leve():
            strength = raw_strength
            dexterity = new_dexterity
            constituition = raw_dexterity
            intelligence = raw_intelligence
            wisdom = raw_wisdom
            charisma = c.change_charisma(1, raw_charisma)

            strength_mod = Modifiers.strength_modifier(strength)
            dexterity_mod = Modifiers.dexterity_modifier(dexterity)
            constituition_mod = Modifiers.constituition_modifier(constituition)
            intelligence_mod = Modifiers.intelligence_modifier(intelligence)
            wisdom_mod = Modifiers.wisdom_modifier(wisdom)
            charisma_mod = Modifiers.charisma_modifier(charisma)

            return f"Força: {strength} [{strength_mod}] \nDestreza: {dexterity} [{dexterity_mod}] \nConstituição: {constituition} [{constituition_mod}] \nInteligência: {intelligence} [{intelligence_mod}] \nSabedoria: {wisdom} [{wisdom_mod}] \nCarisma: {charisma} [{charisma_mod}]"


        def robustos():
            strength = raw_strength
            dexterity = new_dexterity
            constituition = c.change_constituition(1, raw_constituition)
            intelligence = raw_intelligence
            wisdom = raw_wisdom
            charisma = raw_charisma

            strength_mod = Modifiers.strength_modifier(strength)
            dexterity_mod = Modifiers.dexterity_modifier(dexterity)
            constituition_mod = Modifiers.constituition_modifier(constituition)
            intelligence_mod = Modifiers.intelligence_modifier(intelligence)
            wisdom_mod = Modifiers.wisdom_modifier(wisdom)
            charisma_mod = Modifiers.charisma_modifier(charisma)

            return f"Força: {strength} [{strength_mod}] \nDestreza: {dexterity} [{dexterity_mod}] \nConstituição: {constituition} [{constituition_mod}] \nInteligência: {intelligence} [{intelligence_mod}] \nSabedoria: {wisdom} [{wisdom_mod}] \nCarisma: {charisma} [{charisma_mod}]"


        halfling_races = {
            "1":pe_leve, 
            "2":robustos
            }

        end_value = halfling_races.get(sub_race, lambda: "invalid")
        return end_value()

    def human(self):
        desloc = int(9)
        strength = c.change_strength(1, raw_strength)
        dexterity = c.change_dexterity(1, raw_dexterity)
        constituition = c.change_constituition(1, raw_constituition)
        intelligence = c.change_intelligence(1, raw_intelligence)
        wisdom = c.change_wisdom(1, raw_wisdom)
        charisma = c.change_charisma(1, raw_charisma)

        strength_mod = Modifiers.strength_modifier(strength)
        dexterity_mod = Modifiers.dexterity_modifier(dexterity)
        constituition_mod = Modifiers.constituition_modifier(constituition)
        intelligence_mod = Modifiers.intelligence_modifier(intelligence)
        wisdom_mod = Modifiers.wisdom_modifier(wisdom)
        charisma_mod = Modifiers.charisma_modifier(charisma)

        return f"Força: {strength} [{strength_mod}] \nDestreza: {dexterity} [{dexterity_mod}] \nConstituição: {constituition} [{constituition_mod}] \nInteligência: {intelligence} [{intelligence_mod}] \nSabedoria: {wisdom} [{wisdom_mod}] \nCarisma: {charisma} [{charisma_mod}]"

    def dragonborn(self):

        anc = str(inputer('Selecione seu ancestral Draconico: \n1 para Azul(Elétrico) \n2 para Branco(Frio) \n3 para Bronze(Elétrico) \n4 para Cobre(Acído) \n5 para Latão(Fogo) \n6 para Negro(Acído) \n7 para Ouro(Fogo) \n8 para Prata(Frio) \n9 para Verde(Veneno) \n10 para Vermelho(Fogo) \n- '))
        lol = 'Você pode usar uma Ação para exalar energia destrutiva'
        idioma = 'Idioma: \nComum e Dracônico'
        destre = 'Linha de 1.5/9 metros (Teste de Destreza)'
        con = 'Cone de 4.5 metros (Testede Constituição)'
        de = 'Cone de 4.5 metros (Teste de Destreza)'
        cd = 'CD 8 + modificador de Constituição + bônus de proeficiência'
        dano = 'Uma criatura sofre 2d6 de dano num fracasso e metade disso num sucesso \nO dano aumenta para 3d6 no nível 6, 4d6 no nível 11 e 5d6 no nível 16 \nApós o uso é preciso realizar descanso curto/longo '
        desloc = int(9)

        strength = c.change_strength(2, raw_strength)
        dexterity = raw_strength
        constituition = raw_constituition
        intelligence = raw_intelligence
        wisdom = raw_wisdom
        charisma = c.change_charisma(1, raw_charisma)

        strength_mod = Modifiers.strength_modifier(strength)
        dexterity_mod = Modifiers.dexterity_modifier(dexterity)
        constituition_mod = Modifiers.constituition_modifier(constituition)
        intelligence_mod = Modifiers.intelligence_modifier(intelligence)
        wisdom_mod = Modifiers.wisdom_modifier(wisdom)
        charisma_mod = Modifiers.charisma_modifier(charisma)

        stts = f"Força: {strength} [{strength_mod}] \nDestreza: {dexterity} [{dexterity_mod}] \nConstituição: {constituition} [{constituition_mod}] \nInteligência: {intelligence} [{intelligence_mod}] \nSabedoria: {wisdom} [{wisdom_mod}] \nCarisma: {charisma} [{charisma_mod}]"
        
        def azul():
            return f'{stts}\nDraconato Azul \n{desloc} \nHabilidades: \n{lol} elétrica {destre} \n{cd} \n(dano) \nResistência a dano Elétrico {idioma}'

        def branco():
            return f'{stts}\nDraconato Branco \n{desloc} \nHabilidades: \n{lol} de frio {con} \n{cd} \n{dano} \nResistência a dano de Frio \n{idioma}'

        def bronze():
            return f'{stts}\nDraconato Bronze \n{desloc}  \nHabilidades: \n{lol} elétrica {destre} \n{cd} \n{dano} \nResistência a danos Elétrico \n{idioma}'

        def cobre():
            return f'{stts}\nDraconato Cobre \n{desloc}  \nHabilidades: \n{lol} acída {destre} \n{cd} \n{dano} \nResistência a dano Acído \n{idioma}' 

        def latao():
            return f'{stts}\nDraconato Latão \n{desloc}  \nHabilidades: \n{lol} de fogo {destre} \n{cd} \n{dano} \nResistência a dano de Fogo \nidioma'

        def negro():
            return f'{stts}\nDraconato Negro \n{desloc}  \nHabilidades: \n{lol} acído {destre} \n{cd} {de} \n{dano} \nResistência a dano Acído \n{idioma}'

        def ouro():
            return f'{stts}\nDraconato Ouro \n{desloc}  \nHabilidades: \n{lol} de fogo {de} \n{cd} \n{dano} \nResistência a dano de Fogo \n{idioma}'

        def prata():
            return f'{stts}\nDraconato Prata \n{desloc}  \nHabilidades: \n{lol} de frio {con} \n{cd} \n{dano} \nResistência a dano de frio \n{idioma}'

        def verde():
            return f'{stts}\nDraconato Verde \n{desloc}  \nHabilidades: \n{lol} de veneno {con} \n{cd} \n{dano} \nResistência a dano Venenoso \n{idioma}'
      
        def vermelho():
            return f'{stts}\nDraconato Vermelho \n{desloc}  \nHabilidades: \n{lol} de fogo {de} \n{cd} \n{dano} \nResistência a dano de Fogo \n{idioma}'

        ancestors_list = {
            "1":azul, 
            "2":branco,
            "3":bronze, 
            "4":cobre, 
            "5":latao, 
            "6":negro, 
            "7":ouro, 
            "8":prata, 
            "9":verde,
            "10":vermelho
        }
        end_value = ancestors_list.get(anc, lambda: "invalid")
        return end_value()

    def gnome(self):
        desloc = int(9)
        new_intelligence = c.change_intelligence(2, raw_intelligence)
        sub_race = str(inputer('Sub-Raça: \n1 para Gnomo da Floresta \n2 para Gnomo das Rochas \n- '))

        def forest():
            strength = raw_strength
            dexterity = c.change_dexterity(2, raw_dexterity)
            constituition = raw_constituition
            intelligence = new_intelligence
            wisdom = raw_wisdom

            charisma = raw_charisma

            strength_mod = Modifiers.strength_modifier(strength)
            dexterity_mod = Modifiers.dexterity_modifier(dexterity)
            constituition_mod = Modifiers.constituition_modifier(constituition)
            intelligence_mod = Modifiers.intelligence_modifier(intelligence)
            wisdom_mod = Modifiers.wisdom_modifier(wisdom)
            charisma_mod = Modifiers.charisma_modifier(charisma)

            return f"Força: {strength} [{strength_mod}] \nDestreza: {dexterity} [{dexterity_mod}] \nConstituição: {constituition} [{constituition_mod}] \nInteligência: {intelligence} [{intelligence_mod}] \nSabedoria: {wisdom} [{wisdom_mod}] \nCarisma: {charisma} [{charisma_mod}]" 
        
        def mountain():
            strength = raw_strength
            dexterity = raw_dexterity
            constituition = c.change_constituition(1, raw_constituition)
            intelligence = new_intelligence
            wisdom = raw_wisdom
            charisma = raw_charisma

            charisma = raw_charisma

            strength_mod = Modifiers.strength_modifier(strength)
            dexterity_mod = Modifiers.dexterity_modifier(dexterity)
            constituition_mod = Modifiers.constituition_modifier(constituition)
            intelligence_mod = Modifiers.intelligence_modifier(intelligence)
            wisdom_mod = Modifiers.wisdom_modifier(wisdom)
            charisma_mod = Modifiers.charisma_modifier(charisma)

            return f"Força: {strength} [{strength_mod}] \nDestreza: {dexterity} [{dexterity_mod}] \nConstituição: {constituition} [{constituition_mod}] \nInteligência: {intelligence} [{intelligence_mod}] \nSabedoria: {wisdom} [{wisdom_mod}] \nCarisma: {charisma} [{charisma_mod}]"

        gnomes_races = {
            "1":forest, 
            "2":mountain
            }

        end_value = gnomes_races.get(sub_race, lambda: "invalid")
        return end_value()

    def half_elf(self): 
        desloc = int(9)
        select = int(inputer("Escolha 1 atributo: \n1 para Força \n2 para Destreza \n3 para Constituição \n4 para Inteligência \n5 para Sabedoria \n- "))

        strength = raw_strength
        dexterity = raw_dexterity
        constituition = raw_constituition
        intelligence = raw_intelligence
        wisdom = raw_wisdom
        charisma = c.change_charisma(2, raw_charisma)

        if select == 1:
            strength = strength + 1
        
        elif select ==  2:
            dexterity = dexterity +1

        elif select == 3:
            constituition = constituition + 1
        
        elif select == 4:
            intelligence = intelligence + 1

        elif select == 5:
            wisdom = wisdom + 1 

        strength_mod = s.mod(strength)
        dexterity_mod = s.mod(dexterity)
        constituition_mod = s.mod(constituition)
        intelligence_mod = s.mod(intelligence)
        wisdom_mod = s.mod(wisdom)
        charisma_mod = s.mod(charisma)

        return f"Força: {strength} [{strength_mod}] \nDestreza: {dexterity} [{dexterity_mod}] \nConstituição: {constituition} [{constituition_mod}] \nInteligência: {intelligence} [{intelligence_mod}] \nSabedoria: {wisdom} [{wisdom_mod}] \nCarisma: {charisma} [{charisma_mod}]"

    def half_orc(self):
        desloc = int(9)

        strength = c.change_strength(2, raw_strength)
        dexterity = raw_dexterity
        constituition = c.change_constituition(1, raw_constituition)
        intelligence = raw_intelligence
        wisdom = raw_wisdom
        charisma = raw_charisma

        strength_mod = Modifiers.strength_modifier(strength)
        dexterity_mod = Modifiers.dexterity_modifier(dexterity)
        constituition_mod = Modifiers.constituition_modifier(constituition)
        intelligence_mod = Modifiers.intelligence_modifier(intelligence)
        wisdom_mod = Modifiers.wisdom_modifier(wisdom)
        charisma_mod = Modifiers.charisma_modifier(charisma)

        return f"Força: {strength} [{strength_mod}] \nDestreza: {dexterity} [{dexterity_mod}] \nConstituição: {constituition} [{constituition_mod}] \nInteligência: {intelligence} [{intelligence_mod}] \nSabedoria: {wisdom} [{wisdom_mod}] \nCarisma: {charisma} [{charisma_mod}]"

    def tiefling(self):
        desloc = int(9) 
        tr = 'Possui o truque Tramaturgia'
        lvl3 = 'Ao atingir o nível 3 adquire Repreensão infernal como uma magia de nível 2'
        lvl5 = 'Ao atingir o nível 5 adquire Escuridão \nPode utilizar magias desse traço 1 vez por descanso longo'
        
        strength = raw_strength
        dexterity = raw_dexterity
        constituition = raw_constituition
        intelligence = c.change_intelligence(1, raw_intelligence)
        wisdom = raw_wisdom
        charisma = c.change_charisma(2, raw_charisma)


        strength_mod = Modifiers.strength_modifier(strength)
        dexterity_mod = Modifiers.dexterity_modifier(dexterity)
        constituition_mod = Modifiers.constituition_modifier(constituition)
        intelligence_mod = Modifiers.intelligence_modifier(intelligence)
        wisdom_mod = Modifiers.wisdom_modifier(wisdom)
        charisma_mod = Modifiers.charisma_modifier(charisma)

        return f"Força: {strength} [{strength_mod}] \nDestreza: {dexterity} [{dexterity_mod}] \nConstituição: {constituition} [{constituition_mod}] \nInteligência: {intelligence} [{intelligence_mod}] \nSabedoria: {wisdom} [{wisdom_mod}] \nCarisma: {charisma} [{charisma_mod}] \nHabilidades: {tr} \n{lvl3} \n{lvl5}"

class PlayerSheet():

    def races_sheet(self):

        r = Races()
        races = {
            "1":r.dwarf,
            "2":r.elf,
            "3":r.halfling,
            "4":r.human,
            "5":r.dragonborn,
            "6":r.gnome,
            "7":r.half_elf,
            "8":r.half_orc,
            "9":r.tiefling
        }

        races_get = races.get(race_selector, lambda: "invalid")
        return races_get()

    def head(self):
        return Header.name_place()


ps = PlayerSheet()

print(ps.head())
print(ps.races_sheet())

