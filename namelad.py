import math


def inputer(message):
    return input(message)

class Head():

    def lvl(self):
        a = inputer("Level: ")
        return int(a)

    def name(self):
        return inputer("Name: ")

    def race(self):
        return int(inputer('1 para Anão \n2 para Elfo \n3 para Halfling \n4 para Humano \n5 para Draconato \n6 para Gnomo \n7 para Meio-Elfo \n8 para Meio-Orc \n9 para Tiefling \n- '))

    def p_class(self):
        return inputer("Class: ")

    def armor_class(self):
        return int(inputer("Type your Armor Class: "))
    
    def health_points(self):
        return int(inputer("Total Heath Points: "))

class PlayerStats():
    def strength(self):
        return int(inputer("Strength: "))

    def dexterity(self):
        return int(inputer("Dexterity: "))

    def constituition(self):
        return int(inputer("Constituition: "))

    def intelligence(self):
        return int(inputer("Intelligence: "))

    def wisdom(self):
        return int(inputer("Wisdom: "))

    def charisma(self):
        return int(inputer("Charisma: "))




def proe_give(lvl, rangea, rangeb, proe):
    if lvl in range(rangea, rangeb):
        return str(proe)
    else:
        return False

h = Head()
nivel = h.lvl()

um = proe_give(nivel, 0, 5, 2)
dois = proe_give(nivel, 5, 9, 3)
tres = proe_give(nivel, 9, 13, 4)
quatro = proe_give(nivel, 13, 17, 5)
cinco = proe_give(nivel, 17, 21, 6)

lista = [um, dois, tres, quatro, cinco]
    

def ind(index=0):
    while lista[index] is False:
        index = index + 1
        return ind(index)
    else:
        return lista[index]

class Status():

    def mod(self, attribute):
        mod = (int(attribute) -10)/2
        r = round(mod)
        return r 
    
    def proeficience():
        proe = ind(index=0)
        return proe

    def resistence(self, attribute):
        if Status.mod(attribute) >= int(0):
            resistence = Status.mod(atributte) + Status.proeficience()
            return resistence
        else:
            resistence = Status.mod(attribute)
            return resistence

    def positive(self, number):
        if int(number) < 0:
            result = number *-1
            return result
        else:
            return number

    def call_negative(self, number, proeficience=proeficience()):
        if int(number) > 0:
            result = number + proeficience
            return result
        else:
            result = (Status.pos(number) + proeficience)*-1
            return result

    def skill_number(self, skill):
        if skill < int(0):
            value = Status.call_negative(int(skill))
            return value
        else:
            return skill

class ChangeValues():

    def value_changed(self, value=0):
        return int(value)

    def change_strength(self, value):
        c = ChangeValues()
        valor = c.value_changed(value)
        return valor + raw_stregth

    def change_dexterity(self, value):
        c = ChangeValues()
        valor = c.value_changed(value)
        return valor + raw_dexterity

    def change_constituition(self, value):
        c = ChangeValues()
        valor = c.value_changed(value)
        return valor + raw_constituition

    def change_intelligence(self, value):
        c = ChangeValues()
        valor = c.value_changed(value)
        return valor + raw_intelligence

    def change_wisdom(self, value):
        c = ChangeValues()
        valor = c.value_changed(value)
        return valor + raw_wisdom

    def change_charisma(self, value):
        c = ChangeValues()
        valor = c.value_changed(value)
        return valor + raw_wisdom

    def return_value(self, change, lista, rangea, rangeb, index=0):
        if change in range(rangea, rangeb):
            index = change-1
            return lista[index]
        else:
            return False

p = PlayerStats()

raw_strength = p.strength()
raw_dexterity = p.dexterity()
raw_constituition = p.constituition()
raw_intelligence = p.intelligence()
raw_wisdom = p.wisdom()
raw_charisma = p.charisma()