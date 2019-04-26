#!/usr/bin/python3

import random
import time

class creature:
    def __init__(self, hp):
        self.hp = hp

class survivor(creature):
    def __init__(self, hp):
        super().__init__(hp)

class zombie(creature):
    def __init__(self, hp):
        super().__init__(hp)

survivor.hp=100
zombie.hp=100

print('battle begins!')

def zombie_attack(defense):
    print('zombie attacks!')
    damage = random.randint(0,20)
    print(f'zombie attempts to damage {damage} points!')
    if defense > damage:
        damage = 0
        survivor.hp=survivor.hp-damage
        print(f'survivor gets damage: -0 hp! (defense: {defense} points)')
    else:
        survivor.hp=survivor.hp-damage+defense
        print(f'survivor gets damage: -{damage-defense} hp! (defense: {defense} points)')

def survivor_tactic():
    tactic=input('choose tactics: [1]deffensive, [2]agressive, [3]neutral:\n[1-3]: ')
    while tactic != '1' and tactic != '2' and tactic != '3':
        tactic = input('choose 1-3: ')
    else:
        if tactic == '1':
            defense=random.randint(0,10)
            damage=random.randint(0,20)-random.randint(0, 10)
            if damage < 0:
                damage = 0
            crit=0
    
        elif tactic=='2':
            damage=random.randint(0,20)
            crit=random.randint(0,10)
            defense=-random.randint(0,10)

        elif tactic=='3':
            damage=random.randint(0, 20)
            defense=0
            crit=0
    
    return defense,damage,crit

def survivor_attack(damage, crit):
    print('survivor attacks!')
    zombie.hp=zombie.hp-damage-crit
    print(f'survivor attempts to damage {damage} points!')
    if crit != 0:
        print(f'zombie gets damage: -{damage+crit} hp! ({crit} - bonus for critical hit)')
    else:
        print(f'zombie gets damage: -{damage} hp!')

round=0
while True:
    round +=1
    print(f'round {round}\n\nsurvivor health: {survivor.hp} hp\nzombie health: {zombie.hp} hp')
    defense, damage, crit = survivor_tactic()
    print()
    if random.randint(0, 1)==0:
        print('survivor attacks first!')
        survivor_attack(damage, crit)
        if zombie.hp <= 0:
            print('survivor wins!')
            break
        zombie_attack(defense)
        if survivor.hp <= 0:
            print('zombie wins!')
            break
    else:
        print('zombie attacks first!')
        zombie_attack(defense)
        if survivor.hp <= 0:
            print('zombie wins!')
            break
        survivor_attack(damage, crit)
        if zombie.hp <= 0:
            print ('survivor wins!')
            break
    time.sleep(1)
    print()
