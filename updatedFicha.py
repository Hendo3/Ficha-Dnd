#BOLAR ESQUEMA PARA ARMADURA COM MODS

def inputer(message):
    '''
    Retorna um input
    '''
    return input(message)

def is_int(arg1):
    '''
    Verifica se input é int 
    '''
    try:
        int(arg1)
        c = int(arg1)
    except ValueError:
        c = False

    if c is False:
        a = inputer("Não é um Número inteiro\nTente novamente: ")
        return is_int(a)

    else:
        return int(arg1)

class Values(object):

    def proeficience(self, lvl, rangea, rangeb, proe):
        '''
        Retorna a proeficiencia
        '''
        if lvl in range(rangea, rangeb):
            return str(proe)
        else:
            return False

    def level(self):
        '''
        nível
        '''
        return is_int(inputer("Nível: "))

    def name(self):
        '''
        nome
        '''
        return inputer("Nome: ")

    def race(self):
        '''
        raça
        '''
        return inputer("1 para Anão \n2 para Elfo \n3 para Halfling \n4 para Humano \n5 para Draconato \n6 para Gnomo \n7 para Meio-Elfo \n8 para Meio-Orc \n9 para Tiefling \n- ")

    def player_class(self):
        '''
        classe
        '''
        return str(inputer("Classe: "))

    def armor_class(self):
        '''
        armadura
        '''
        return is_int(inputer("Classe de Armadura: "))
    
    def health_points(self):
        '''
        vida
        '''
        return is_int(inputer("Pontos de vida totais: "))

    def temp_hp(self):
        '''
        valor de vida temporaria
        '''
        return is_int(inputer("Valor de vida temporária: "))
    
    def lvl(self, lvl):
        nivel = lvl

        um = Values().proeficience( lvl=nivel, rangea=0, rangeb=5, proe=2)
        dois = Values().proeficience(lvl=nivel, rangea=5, rangeb=9, proe=3)
        tres = Values().proeficience(lvl=nivel, rangea=9, rangeb=13, proe=4)
        quatro = Values().proeficience(lvl=nivel, rangea=13, rangeb=17, proe=5)
        cinco = Values().proeficience(lvl=nivel, rangea=17, rangeb=500**500, proe=6)

        lista_de_lvl = [um, dois, tres, quatro, cinco]
        return lista_de_lvl
    
    def ind(self, lista, index=0):
        '''
        retorna a condição true
        '''
        while lista[index] is False:
            index +=1
            return self.ind(lista=lista, index=index)
        else:
            return lista[index]

    def value_changed(self, value=0):
        '''
        retorna value como int
        '''
        return int(value)

    def change(self, value, attribute):
        '''
        retorna value + attribute
        '''
        return Values().value_changed(value=value) + attribute

    def final_life(self, modifier):
        '''
        retorna o max de hp
        '''
        life = Values().health_points()
        if modifier < 0:
            return int(life)
        else:
            return life + int(modifier)

    def modifier(self, attribute):
        '''
        retorna o modificador
        '''
        mod = (int(attribute)-10)/2
        if mod == float():
            return int(round(mod)-1)
        else:
            return int(mod)

    def resistence(self, attribute):
        '''
        retorna o valor das resistencias
        '''
        if Values().modifier(attribute) >= int(0):
            return Values().modifier(attribute) + int(Values().ind(Values().lvl(Values().level)))
        else:
            return (Values().modifier(attribute)*1) + (int(Values().ind(Values().lvl(Values().level))*-1))


