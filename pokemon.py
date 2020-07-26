

import time
import numpy as np
import sys

# delay do tempo

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


#Criando as Classes

class Pokemon:
    def __init__(self, name, types, moves, EVs, health= '===================='):
        #salvar as variaveis como atributos
        self.name = name
        self.types = types
        self.moves = moves
        self.health = health
        self.EVs = EVs
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.bars = 20 # quantidade de hp

    
    def fight(self, Pokemon2):
        #Permite que os pokemons lutem
        print("-----Pokemon Battle------") 
        #Primeiro Pokemon
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENCE/", self.defense)
        print("LVL/", 3*(1+np.mean([self.attack, self.defense])))
        print("\nVS")
        #Segundo Pokemon
        print(f"\n{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENCE/", Pokemon2.defense)
        print("LVL/", 3*(1+np.mean([Pokemon2.attack, Pokemon2.defense])))

        time.sleep(2)

        #Variaveis de Tipo
        versions = ['Fire', 'Water', 'Grass']

        for i, k in enumerate(versions):
            if self.types == k:
                # mesmo tipo
                if Pokemon2.types == k:
                    string1_attack = "\nNot very effective..."
                    string2_attack = "\nNot very effective..."

                #Caso o Pokemon2 seja mais forte
                if Pokemon2.types == versions[(i+1)%3]:  
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string1_attack = "\nNot very Effective..."
                    string2_attack = "\nIts supper Effective!"

                #Caso o Pokemon 2 seja mais fraco
                if Pokemon2.types == versions[(i+2)%3]:
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    self.attack *= 2
                    self.defense *= 2
                    string1_attack = "\nIts supper Effective!"
                    string2_attack = "\nNot very Effective..."
        #criando a luta
        while (self.bars >= 0) and (Pokemon2.bars >=0):
            

            #A luta continua se a vida for maior que zero
            #Imprimir a barra de vida dos pokemons
            print(f"\n{self.name}\t\tHEALTH\t{self.health}")        
            print(f"\n{Pokemon2.name}\t\tHEALTH\t{Pokemon2.health}\n")  

            print("Go " + self.name + "!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)

            index = int(input('Pick a move: '))
            delay_print(f"\n{self.name} used {self.moves[index-1]}!")
            time.sleep(1)
            delay_print(string1_attack)

            #calcular dano

            Pokemon2.bars -= self.attack
            Pokemon2.health = ""

            #Adicionar a barra de vida + defesa
            for j in range(int (Pokemon2.bars+.1*Pokemon2.defense)):
                Pokemon2.health += "="

            time.sleep(1)

            #Imprimir de novo a barra de vida
            print(f"\n{self.name}\t\tHEALTH\t{self.health}")        
            print(f"\n{Pokemon2.name}\t\tHEALTH\t{Pokemon2.health}\n")

            time.sleep(.5)
            
            #Verificar se o pokemons desmaiou
            if Pokemon2.bars <= 0:
                delay_print("\n... " +Pokemon2.name+ "has fainted!")
                break

            #Iniciando o turno do oponente (Pokemon2)

            print("Go" + " " + Pokemon2.name + "!")
            for i, x in enumerate(Pokemon2.moves):
                print(f"{i+1}.", x)

            index = int(input('Pick a move: '))
            delay_print(f"\n{Pokemon2.name} used {Pokemon2.moves[index-1]}!")
            time.sleep(1)
            delay_print(string2_attack)

            #calcular dano

            self.bars -= Pokemon2.attack
            self.health = ""

            #Adicionar a barra de vida + defesa
            for j in range(int (self.bars+.1*self.defense)):
                self.health += "="

            time.sleep(1)

            #Imprimir de novo a barra de vida
            print(f"\n{self.name}\t\tHEALTH\t{self.health}")        
            print(f"\n{Pokemon2.name}\t\tHEALTH\t{Pokemon2.health}\n")

            time.sleep(.5)
            
            #Verificar se o pokemons desmaiou
            if self.bars <= 0:
                delay_print(f"\n..."+ self.name +" has fainted!")
                break



if __name__ == "__main__":
    #Criar os pokemons

    

    Charizard = Pokemon('Charizard', 'Fire', ['FlameThrower', 'Fly', 'Blast burn', 'Fire Punch'], {'ATTACK':12, 'DEFENSE':8})
    Blastoise = Pokemon('Blastoise', 'Water', ['HidroPump', 'WaterGun', 'Ice Beam', 'Surf'], {'ATTACK':10, 'DEFENSE':10})
    Venossaur = Pokemon('Venossaur', 'Grass', ['Razzor Leafs', 'Solar Bean', 'Vampiric Seeds', 'Vine Wip'], {'ATTACK':8, 'DEFENSE':12})

    
    Charizard.fight(Venossaur)
    