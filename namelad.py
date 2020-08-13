import math


def inputer(message):
    return input(message)

class Head():

    def lvl(self):
        a = inputer("Nível: ")
        return int(a)

    def name(self):
        return inputer("Nome: ")

    def race(self):
        return str(inputer('1 para Anão \n2 para Elfo \n3 para Halfling \n4 para Humano \n5 para Draconato \n6 para Gnomo \n7 para Meio-Elfo \n8 para Meio-Orc \n9 para Tiefling \n- '))

    def p_class(self):
        return str(inputer("Classe: "))

    def armor_class(self):
        return int(inputer("Digite sua Classe de Armadura: "))
    
    def health_points(self):
        return int(inputer("Pontos de vida totais: "))

class PlayerStats():

    def strength(self):
        return int(inputer("Força: "))

    def dexterity(self):
        return int(inputer("Destreza: "))

    def constituition(self):
        return int(inputer("Constituição: "))

    def intelligence(self):
        return int(inputer("Inteligência: "))

    def wisdom(self):
        return int(inputer("Sabedoria: "))

    def charisma(self):
        return int(inputer("Carisma: "))

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
        return int(r) 
    
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

    def change_strength(self, value, raw_strength):
        c = ChangeValues()
        valor = c.value_changed(value)
        return valor + raw_strength

    def change_dexterity(self, value, raw_dexterity):
        c = ChangeValues()
        valor = c.value_changed(value)
        return valor + raw_dexterity

    def change_constituition(self, value, raw_constituition):
        c = ChangeValues()
        valor = c.value_changed(value)
        return valor + raw_constituition

    def change_intelligence(self, value, raw_intelligence):
        c = ChangeValues()
        valor = c.value_changed(value)
        return valor + raw_intelligence

    def change_wisdom(self, value, raw_wisdom):
        c = ChangeValues()
        valor = c.value_changed(value)
        return valor + raw_wisdom

    def change_charisma(self, value, raw_charisma):
        c = ChangeValues()
        valor = c.value_changed(value)
        return valor + raw_charisma

    def return_value(self, change, lista, rangea, rangeb, index=0):
        if change in range(rangea, rangeb):
            index = change-1
            return lista[index]
        else:
            return False

    def life_filler(self, modifer):
        h = Head()
        life = h.health_points()
        full_life = int(life) + int(modifer)

        return full_life