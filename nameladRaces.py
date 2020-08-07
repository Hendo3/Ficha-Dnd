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
    def strength_modifier(modfier=raw_strength):
        return s.mod(int(modfier))

    def dexterity_modifier(modifier=raw_dexterity):
        return s.mod(int(modifier))

    def constituition_modifier(modifier=raw_constituition):
        return s.mod(int(modifier))

    def intelligence_modifier(modifier=raw_intelligence):
        return s.mod(int(modifier))

    def wisdom_modifier(modifier=raw_wisdom):
        return s.mod(int(modifier))

    def charisma_modifier(modifier=raw_charisma):
        return s.mod(int(modifier))

class Header():

    def name_place(lvl=h.lvl(), name=h.name(), race=h.race(), p_class=h.p_class, armor_class=h.armor_class(), health_points=h.health_points()):
        space = " "*3
        print(f"Nome: {name} {space} Nível: {lvl} {space} \nRaça: {race} {space} Classe: {p_class} \nVida Total: {health_points} Classe de armadura: {armor_class}")

class Races():
    dark = '18 metros na penumbra como se fosse luz plena e no escuro como se fosse penumbra, \nnão pode discernir cores, apenas tons de cinza'


    def dwarf():
        new_constituition = c.change_constituition(2)
        desloc = float(7.5)
        sub_race  = int(inputer('Sub-raça: \n1 para Anão da Colina \n2 para Anão da Montanha \n- '))

        def colina():
            strength = raw_strength
            dexterity = raw_dexterity
            constituition = new_constituition
            intelligence = raw_intelligence
            wisdom = c.change_wisdom(1)
            charisma = raw_charisma

            strength_mod = Modifiers.strength_modifier(strength)
            dexterity_mod = Modifiers.dexterity_modifier(dexterity)
            constituition_mod = Modifiers.constituition_modifier(constituition)
            intelligence_mod = Modifiers.intelligence_modifier(intelligence)
            wisdom_mod = Modifiers.wisdom_modifier(wisdom)
            charisma_mod = Modifiers.charisma_modifier(charisma)

            stts = f"Força: {strength} [{strength_mod}] \nDestreza: {dexterity} [{dexterity_mod}] \nConstituição: {constituition} [{constituition_mod}] \nInteligência: {intelligence} [{intelligence_mod}] \nSabedoria: {wisdom} [{wisdom_mod}] \nCarisma: {charisma} [{charisma_mod}]"
            return stts
        
        def montanha():
            strength = c.change_strength(2)
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

            stts = f"Força: {strength} [{strength_mod}] \nDestreza: {dexterity} [{dexterity_mod}] \nConstituição: {constituition} [{constituition_mod}] \nInteligência: {intelligence} [{intelligence_mod}] \nSabedoria: {wisdom} [{wisdom_mod}] \nCarisma: {charisma} [{charisma_mod}]"
            return stts
            
        dwarf_races = [colina(), montanha()]

        end_value = c.return_value(lista=dwarf_races, change=sub_race, rangea=1, rangeb=3, index=0)
        return end_value


    def elf():
        new_dexterity = c.change_dexterity(2)
        sub_races = int(inputer('Sub_raça: \n1 para Alto elfo \n2 para Elfo da floresta \n3 para Drow(Elfo negro) \n- '))

        def high_elf():
            desloc = int(9)

            strength = raw_strength
            dexterity = new_dexterity
            constituition = raw_constituition
            intelligence = c.change_intelligence(1)
            wisdom = raw_wisdom
            charisma = raw_charisma

            strength_mod = Modifiers.strength_modifier(strength)
            dexterity_mod = Modifiers.dexterity_modifier(dexterity)
            constituition_mod = Modifiers.constituition_modifier(constituition)
            intelligence_mod = Modifiers.intelligence_modifier(intelligence)
            wisdom_mod = Modifiers.wisdom_modifier(wisdom)
            charisma_mod = Modifiers.charisma_modifier(charisma)

            stts = f"Força: {strength} [{strength_mod}] \nDestreza: {dexterity} [{dexterity_mod}] \nConstituição: {constituition} [{constituition_mod}] \nInteligência: {intelligence} [{intelligence_mod}] \nSabedoria: {wisdom} [{wisdom_mod}] \nCarisma: {charisma} [{charisma_mod}]"
            return stts

        def florest_elf():
            desloc = int(12)

            strength = raw_strength
            dexterity = new_dexterity
            constituition = raw_constituition
            intelligence = raw_intelligence
            wisdom = c.change_wisdom(1)
            charisma = raw_charisma

            strength_mod = Modifiers.strength_modifier(strength)
            dexterity_mod = Modifiers.dexterity_modifier(dexterity)
            constituition_mod = Modifiers.constituition_modifier(constituition)
            intelligence_mod = Modifiers.intelligence_modifier(intelligence)
            wisdom_mod = Modifiers.wisdom_modifier(wisdom)
            charisma_mod = Modifiers.charisma_modifier(charisma)

            stts = f"Força: {strength} [{strength_mod}] \nDestreza: {dexterity} [{dexterity_mod}] \nConstituição: {constituition} [{constituition_mod}] \nInteligência: {intelligence} [{intelligence_mod}] \nSabedoria: {wisdom} [{wisdom_mod}] \nCarisma: {charisma} [{charisma_mod}]"
            return stts

        elf_races = [high_elf(), florest_elf()]

        end_value = c.return_value(lista=elf_races, change=sub_races, rangea=1, rangeb=3, index=0)
        return end_value


print(Races.elf())