# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#      NPC Generator
#       by Nicodemus
#       September 9, 2018
#
#       This is an attempt to build a basic generator to fill out basic DnD 5e numeric NPC needs.
#
#       Scope:  Randomly generate a stat block for a melee, ranged, arcane, or divine based npc
#               including race, features, special abilities, and varying CRs.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


import math
import random
import dictionaries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Feature List v1:
# TODO - random alignment generator
# TODO - random name generator
# TODO - armor selector             DONE
# TODO - weapon selector            DONE
#           TODO - add damage type to weapons
#           TODO - add versatile to weapons
#           TODO - adjust weapon format to account for negative modifiers
# TODO - hit point calculator
# TODO - saving throw calculator
# TODO - skill selector             DONE
# TODO - senses
# TODO - Create Dictionaries
#           TODO - Abilities
#           TODO - Spells
# TODO - Generate actions based on abilities and spells

# Feature List v2
# TODO - generate image or formatted image of state block
# TODO - Modify-able statblocks
# TODO - Save alternate images of stat block
# TODO - Save alternate plain-text of stat block

# Feature List web v1
# TODO - Create website
# TODO - Put stuff on website

# Feature List v2.1
# TODO - Add Charisma Caster
# TODO - Add Druid-style Divine Caster


attributes = {
        'str': 0, 'str_mod': 0,
        'dex': 0, 'dex_mod': 0,
        'con': 0, 'con_mod': 0,
        'int': 0, 'int_mod': 0,
        'wis': 0, 'wis_mod': 0,
        'cha': 0, 'cha_mod': 0
    }


def determine_archetype():                      # Select the archetype of the NPC you would like to generate
    print('Select NPC Archetype')
    print('1: warrior, 2: archer, 3: roguish, 4: arcane caster, 5: divine caster, 6: random')
    arch_input = input()
    arch_input = arch_input.lower()
    if arch_input == '1' or arch_input == 'one' or arch_input == 'warrior' or arch_input == 'war':
        archetype = 1
    elif arch_input == '2' or arch_input == 'two' or arch_input == 'archer' or arch_input == 'arch':
        archetype = 2
    elif arch_input == '3' or arch_input == 'three' or arch_input == 'rogue' or arch_input == 'roguish':
        archetype = 3
    elif arch_input == '4' or arch_input == 'four' or arch_input == 'arcane' or arch_input == 'arcane-caster':
        archetype = 4
    elif arch_input == '5' or arch_input == 'five' or arch_input == 'divine' or arch_input == 'divine-caster':
        archetype = 5
    else:                                       # If there is no input, the archetype is randomly selected
        if random.randint(1, 4) == 1:           # Increases the likelihood of the 'warrior' being randomly selected
            archetype = 1
        else:
            archetype = random.randint(1, 5)
    return archetype


def generate_attributes():
    gen_attributes = []
    for num in range(6):                        # Loop to generate each attribute
        stat_roll = []
        stat_sum = 0
        for i in range(5):                      # Loop to roll dice for each attribute
            roll = random.randint(1, 4)         # d4 roll (5 iterations)
            stat_sum = stat_sum + roll          # Add roll to total for single attribute
        gen_attributes.append(stat_sum)         # Add total roll for list of generated attributes
    gen_attributes.sort(reverse=True)           # Sort list of attributes in descending order
    return gen_attributes


def assign_attributes(generated_attributes, archetype):     # Assigns attribute rolls based on archetypal importance
    if archetype == 1:                                      # Warrior
        attributes['str'] = generated_attributes[0]
        attributes['dex'] = generated_attributes[2]
        attributes['con'] = generated_attributes[1]
        attributes['int'] = generated_attributes[4]
        attributes['wis'] = generated_attributes[3]
        attributes['cha'] = generated_attributes[5]
    elif archetype == 2:                                    # Archer
        attributes['str'] = generated_attributes[3]
        attributes['dex'] = generated_attributes[0]
        attributes['con'] = generated_attributes[1]
        attributes['int'] = generated_attributes[2]
        attributes['wis'] = generated_attributes[5]
        attributes['cha'] = generated_attributes[4]
    elif archetype == 3:                                    # Roguish
        attributes['str'] = generated_attributes[4]
        attributes['dex'] = generated_attributes[0]
        attributes['con'] = generated_attributes[2]
        attributes['int'] = generated_attributes[1]
        attributes['wis'] = generated_attributes[5]
        attributes['cha'] = generated_attributes[3]
    elif archetype == 4:                                    # Arcane-caster
        attributes['str'] = generated_attributes[5]
        attributes['dex'] = generated_attributes[1]
        attributes['con'] = generated_attributes[2]
        attributes['int'] = generated_attributes[0]
        attributes['wis'] = generated_attributes[3]
        attributes['cha'] = generated_attributes[4]
    elif archetype == 5:                                    # Divine-caster
        attributes['str'] = generated_attributes[3]
        attributes['dex'] = generated_attributes[4]
        attributes['con'] = generated_attributes[1]
        attributes['int'] = generated_attributes[5]
        attributes['wis'] = generated_attributes[0]
        attributes['cha'] = generated_attributes[2]
    else:
        print('ERROR: func(assign_attributes)')
        exit(-1)

    attributes['str_mod'] = modifier_calc(attributes['str'])        # Calculates the attribute modifiers
    attributes['dex_mod'] = modifier_calc(attributes['dex'])        # for each ability score
    attributes['con_mod'] = modifier_calc(attributes['con'])
    attributes['int_mod'] = modifier_calc(attributes['int'])
    attributes['wis_mod'] = modifier_calc(attributes['wis'])
    attributes['cha_mod'] = modifier_calc(attributes['cha'])


def modifier_calc(attribute):                   # Calculates ability modifiers
    modifier = ((attribute - 10) / 2)
    modifier = math.floor(modifier)
    return modifier


def determine_challenge_rating():               # Returns CR between 1/4 and 30.
    print('Enter Challenge Rating (0.25-30)')
    challenge_rating = input()
    try:
        challenge_rating = float(challenge_rating)
    except ValueError:
        print('Invalid Entry. Randomly Generated CR.')
        challenge_rating = (random.uniform(0.25, 65) / 5)
    if challenge_rating >= 1:
        challenge_rating = round(challenge_rating, 0)
    elif 1 > challenge_rating >= 0.5:
        challenge_rating = 0.5
    elif challenge_rating < 0.5:
        challenge_rating = 0.25
    return challenge_rating


def determine_xp_value(challenge_rating):           # Returns the XP value of the generated CR of the NPC
    xp = [0,                                        # XP by Cr table.
          200,   450,    700,    1100,   1800,      # Ignores CR 1/8
          2300,  2900,   3900,   5000,   5900,      # DMG pg. 275
          7200,  8400,   10000,  11500,  13000,
          15000, 18000,  20000,  22000,  25000,
          33000, 41000,  50000,  62000,  75000,
          90000, 105000, 120000, 135000, 155000]
    if 1 <= challenge_rating <= 30:
        return xp[int(challenge_rating)]
    elif challenge_rating == 0.25:
        return 50
    elif challenge_rating == 0.5:
        return 100
    else:
        print('ERROR! This doesnt make Gods!')       # TODO Raise an Error instead pf exit
        return 0


def determine_hit_points(cr, archetype):
    # Number of hit dice is semi arbitrary (random, and influenced by archetype)
    if archetype == 1:
        hit_dice = (math.log((cr ** 15) + 40, 20) * (cr / random.uniform(2, 3))) + random.uniform(1, 3)
    elif archetype == 2 or archetype == 3:
        hit_dice = (math.log((cr ** 15) + 40, 20) * (cr / random.uniform(2.8, 4))) + random.uniform(1, 3)
    elif archetype == 4:
        hit_dice = (math.log((cr ** 15) + 40, 20) * (cr / random.uniform(3, 4))) + random.uniform(1, 2)
    elif archetype == 5:
        hit_dice = (math.log((cr ** 15) + 40, 20) * (cr / random.uniform(2.5, 3.5))) + random.uniform(1, 2)

    hit_dice = math.floor(hit_dice)
    dice_hp = hit_dice * 4.5
    con_hp = hit_dice * attributes['con_mod']
    total_hp = math.floor(dice_hp + con_hp)
    return total_hp, hit_dice, con_hp


def determine_prof_bonus(cr):
    if cr < 5:
        prof_bonus = 2
    elif 5 <= cr <= 30:
        prof_bonus = math.floor(((cr - 1) / 4) + 2)
    else:
        print('ERROR! User is not Proficient!')
        exit(-1)                                # TODO Raise Error instead of quitting
    return prof_bonus


def determine_armor(cr, archetype):
    while True:
        rand_num = random.randint(1, 3)
        if archetype == 1:
            if rand_num < 3:
                armor_type = 'medium_armor'
            else:
                armor_type = 'heavy_armor'
        elif archetype == 2 or archetype == 3:
            if rand_num < 3:
                armor_type = 'light_armor'
            else:
                armor_type = 'medium_armor'
        elif archetype == 4:
            if rand_num < 3:
                armor_type = 'no_armor'
            else:
                armor_type = 'light_armor'
        elif archetype == 5:
            if rand_num == 1:
                armor_type = 'light_armor'
            elif rand_num == 2:
                armor_type = 'medium_armor'
            elif rand_num == 3:
                armor_type = 'heavy_armor'

        armor = random.choice(list(dictionaries.armor_dict[armor_type].keys()))
        armor_ac = dictionaries.armor_dict[armor_type][armor]['ac']
        armor_str_req = dictionaries.armor_dict[armor_type][armor]['str_req']
        armor_stlth = dictionaries.armor_dict[armor_type][armor]['stlth']

        shield = True
        if shield is True:
            shield_string = 'and shield'
        else:
            shield_string = ''

        if archetype == 2 and armor_stlth is not None:
            continue
        elif armor_str_req is None or attributes['str'] >= armor_str_req:
            break
        else:
            continue
    return armor_type, armor, armor_ac, armor_str_req, armor_stlth, shield, shield_string


def calculate_ac(armor):
    if armor[0] == 'no_armor':
        ac = 10 + attributes['dex_mod']
    elif armor[0] == 'light_armor':
        ac = armor[2] + attributes['dex_mod']
    elif armor[0] == 'medium_armor':
        if attributes['dex_mod'] <= 0:
            ac = armor[2]
        elif attributes['dex_mod'] == 1:
            ac = armor[2] + 1
        elif attributes['dex_mod'] >= 2:
            ac = armor[2] + 2
    elif armor[0] == 'heavy_armor':
        ac = armor[2]
    if armor[5] == True:
        ac = ac + 2
    return ac


def determine_melee_weapons(cr, archetype):
    if cr >= 6 and archetype == 1:
        num_weapons = 3
    elif cr < 6 and archetype == 1:
        num_weapons = 2
    else:
        num_weapons = 1
    melee_weapons = []
    i = 0
    while True:
        if i == 0:
            wep_type = 'simple_melee'
        else:
            wep_type = 'martial_melee'
        weapon = random.choice(list(dictionaries.weapon_dict[wep_type]))
        melee_weapon = get_weapon_prop(wep_type, weapon)
        melee_weapons.append(melee_weapon)
        i += 1
        if i == num_weapons:
            break
    return melee_weapons


def determine_ranged_weapons(cr, archetype):
    num_weapons = 1
    ranged_weapons = []
    i = 0
    while True:
        rand_num = random.randint(1, 4)
        if ((archetype == 1 or archetype == 2) and rand_num > 1) or (archetype != 1 or archetype != 2) and rand_num > 3:
            wep_type = 'martial_ranged'
        else:
            wep_type = 'simple_ranged'
        weapon = random.choice(list(dictionaries.weapon_dict[wep_type]))
        ranged_weapon = get_weapon_prop(wep_type, weapon)
        ranged_weapons.append(ranged_weapon)
        i += 1
        if i == num_weapons:
            break
    return ranged_weapons


def get_weapon_prop(wep_type, weapon):
    die_num   = dictionaries.weapon_dict[wep_type][weapon]['die_num']
    dmg_num   = dictionaries.weapon_dict[wep_type][weapon]['dmg_num']
    finesse   = dictionaries.weapon_dict[wep_type][weapon]['finesse']
    versatile = dictionaries.weapon_dict[wep_type][weapon]['versatile']
    wep_range = dictionaries.weapon_dict[wep_type][weapon]['range']
    prop      = dictionaries.weapon_dict[wep_type][weapon]['prop']
    return wep_type, weapon, die_num, dmg_num, finesse, versatile, wep_range, prop


def print_weapons(melee_weapons, ranged_weapons, prof_bonus):
    weapons = melee_weapons
    weapons.extend(ranged_weapons)
    for wep in weapons:
        if wep[4] == True and ((attributes['dex_mod'] > attributes['str_mod'] and wep[6] == '5ft') or (wep[6] != '5ft')):
            attack_bonus = prof_bonus + attributes['dex_mod']
            damage_bonus = attributes['dex_mod']
        else:
            attack_bonus = prof_bonus + attributes['str_mod']
            damage_bonus = attributes['str_mod']

        print(wep[1], '. Weapon Attack: +', attack_bonus, ' to hit, reach ', wep[6], '. Damage: (', wep[2], 'd', wep[3], '+', damage_bonus, ')', sep='')
    return None


def determine_skills(archtype, prof_bonus):
    skill_list = [['Athletics'],
              ['Acrobatics', 'Sleight of hand', 'Stealth'],
              ['Arcana', 'History', 'Investigation', 'Nature', 'Religion'],
              ['Animal Handling', 'Insight', 'Medicine', 'Perception', 'Survival'],
              ['Deception', 'Intimidation', 'Performance', 'Persuasion']]

    if archtype == 1 or archtype == 2:
        num_skills = random.randint(2, 4)
    if archtype == 3:
        num_skills = random.randint(4, 6)
    if archtype == 4 or archtype == 5:
        num_skills = random.randint(3, 5)
    skills = []
    i = 1
    while True:
        skill_attribute = random.randint(0, 4)
        skill = random.choice(skill_list[skill_attribute])
        skills.append(skill)
        if skill_attribute == 0:
            skills.append(stat_bonus('str', prof_bonus))
        elif skill_attribute == 1:
            skills.append(stat_bonus('dex', prof_bonus))
        elif skill_attribute == 2:
            skills.append(stat_bonus('int', prof_bonus))
        elif skill_attribute == 3:
            skills.append(stat_bonus('wis', prof_bonus))
        elif skill_attribute == 4:
            skills.append(stat_bonus('cha', prof_bonus))
        if i == num_skills:
            break
        i += 1
    return skills


def print_list(skills):
    # TODO sort skills alphabetically
    i = 0
    while True:
        print(skills[i], ' +', skills[i+1], sep='', end='')
        i += 2
        if i < len(skills):
            print(', ', end='')
        if i == len(skills):
            break


def determine_saves(cr, archetype, prof_bonus):
    if cr <= 1:
        num_saves = 1
    elif 1 < cr < 4:
        num_saves = 2
    elif 4 <= cr < 10:
        num_saves = 3
    elif 10 <= cr < 20:
        num_saves = 4
    else:
        num_saves = 5

    if archetype == 1:
        saves_list = ['Strength', stat_bonus('str', prof_bonus),
                      'Constitution', stat_bonus('con', prof_bonus),
                      'Dexterity', stat_bonus('dex', prof_bonus),
                      'Intelligence', stat_bonus('int', prof_bonus),
                      'Wisdom', stat_bonus('wis', prof_bonus)]
    elif archetype == 2:
        saves_list = ['Dexterity', stat_bonus('dex', prof_bonus),
                      'Strength', stat_bonus('str', prof_bonus),
                      'Wisdom', stat_bonus('wis', prof_bonus),
                      'Intelligence', stat_bonus('int', prof_bonus),
                      'Constitution', stat_bonus('con', prof_bonus)]
    elif archetype == 3:
        saves_list = ['Dexterity', stat_bonus('dex', prof_bonus),
                      'Intelligence', stat_bonus('int', prof_bonus),
                      'Wisdom', stat_bonus('wis', prof_bonus),
                      'Charisma', stat_bonus('cha', prof_bonus),
                      'Constitution', stat_bonus('con', prof_bonus)]
    elif archetype == 4:
        saves_list = ['Intelligence', stat_bonus('int', prof_bonus),
                      'Wisdom', stat_bonus('wis', prof_bonus),
                      'Charisma', stat_bonus('cha', prof_bonus),
                      'Dexterity', stat_bonus('dex', prof_bonus),
                      'Constitution', stat_bonus('con', prof_bonus)]
    elif archetype == 5:
        saves_list = ['Charisma', stat_bonus('cha', prof_bonus),
                      'Strength', stat_bonus('str', prof_bonus),
                      'Constitution', stat_bonus('con', prof_bonus),
                      'Dexterity', stat_bonus('dex', prof_bonus),
                      'Intelligence', stat_bonus('int', prof_bonus)]
    saves = []
    i = 0
    while True:
        saves.append(saves_list[i])
        saves.append(saves_list[i+1])
        i += 2
        if i == (2 * num_saves):
            break
    return saves


def determine_spells():
    return None


def stat_bonus(stat, prof_bonus):      #requires three letter stat format. ex. 'str'
    bonus = attributes[f'{stat}_mod'] + prof_bonus
    return bonus


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main():
    generated_attributes = generate_attributes()
    print('Attributes:',generated_attributes)
    archetype = determine_archetype()
    assign_attributes(generated_attributes,archetype)
    challenge_rating = determine_challenge_rating()

    armor = determine_armor(challenge_rating, archetype)
    melee_weapons = determine_melee_weapons(challenge_rating, archetype)
    ranged_weapons = determine_ranged_weapons(challenge_rating, archetype)
    prof_bonus = determine_prof_bonus(challenge_rating)
    hp = determine_hit_points(challenge_rating, archetype)
    saves = determine_saves(challenge_rating, archetype, prof_bonus)
    skills = determine_skills(archetype, prof_bonus)
    #hd_element = [hp[1], challenge_rating, hp[0], archetype]
    #hd_list.append(hd_element)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



    print('\n\n')
    print('Name', archetype)
    print('Medium humanoid, alignment')    # TODO add alignment
    print('-----------------------------------')
    print('Armor Class ', calculate_ac(armor), ' (', armor[1], ' ', armor[6], ')', sep='')
    print('Hit Points ', hp[0], ' (', hp[1], 'd8+', hp[2], ')', sep='')
    print('Speed 30ft.')
    print('-----------------------------------')
    print(' STR   DEX   CON   INT   WIS   CHA')
    print(attributes['str'], '(', attributes['str_mod'], ') ', sep='', end='')
    print(attributes['dex'], '(', attributes['dex_mod'], ') ', sep='', end='')
    print(attributes['con'], '(', attributes['con_mod'], ') ', sep='', end='')
    print(attributes['int'], '(', attributes['int_mod'], ') ', sep='', end='')
    print(attributes['wis'], '(', attributes['wis_mod'], ') ', sep='', end='')
    print(attributes['cha'], '(', attributes['cha_mod'], ') ', sep='', end='\n')
    print('-----------------------------------')
    print('Saves ', end='')
    print_list(saves)
    print('\nSkills ', end='')
    print_list(skills)
    print('\nLanguages: any one language (usually Common)')
    print('Challenge ', challenge_rating, ' (', determine_xp_value(challenge_rating), ' XP)\n', sep='')
    print('ABILITIES__________________________')
    print('ACTIONS____________________________')
    print_weapons(melee_weapons, ranged_weapons, prof_bonus)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


main()

'''
hd_list = []
itera = 0
rand_file_number = random.randint(1, 10000000000)
while True:
    main()
    itera += 1
    if itera == 100000:
        break
df = pd.DataFrame(hd_list, columns=['HD', 'CR', 'HP', 'Archetype'])
df.sort_values('CR', inplace=True)
print(df.head(1000))
print(df.describe())

avgs = df.groupby(['CR', 'Archetype']).mean()
avgs = avgs.reset_index()
print(avgs.head(100))
print(avgs.tail(100))
ax = sns.scatterplot(x='CR', y='HP', data=df, hue='Archetype')
ax = sns.lineplot(x='CR', y='HP', data=avgs, hue='Archetype')
plt.show()
'''
