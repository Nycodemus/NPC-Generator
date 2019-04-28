armor_dict = {
    'no_armor':{
        'No armor':{'ac': None, 'str_req':None, 'stlth':None, 'type':None}
    },
    'light_armor':{
        'Padded':{'ac': 11, 'str_req':None, 'stlth':'Disadvantage', 'type':'light'},
        'Leather':{'ac': 11, 'str_req':None, 'stlth':None, 'type':'light'},
        'Studded':{'ac': 12, 'str_req':None, 'stlth':None, 'type':'light'}
    },
    'medium_armor':{
        'Hide':{'ac': 12, 'str_req':None, 'stlth':None, 'type':'medium'},
        'Chain shirt': {'ac': 13, 'str_req':None, 'stlth':None, 'type':'medium'},
        'Scale mail': {'ac': 14, 'str_req':None, 'stlth':'Disadvantage', 'type':'medium'},
        'Breastplate': {'ac': 14, 'str_req':None, 'stlth':None, 'type':'medium'},
        'Half plate': {'ac': 15, 'str_req':None, 'stlth':'Disadvantage', 'type':'medium'}
    },
    'heavy_armor':{
        'Ring mail':{'ac': 14, 'str_req':None, 'stlth':'Disadvantage', 'type':'heavy'},
        'Chain mail':{'ac': 16, 'str_req':13, 'stlth':'Disadvantage', 'type':'heavy'},
        'Splint':{'ac': 17, 'str_req':15, 'stlth':'Disadvantage', 'type':'heavy'},
        'Plate':{'ac': 18, 'str_req':15, 'stlth':'Disadvantage', 'type':'heavy'}
    },
    'shield':{
        'Shield':{'ac': 2, 'str_req':None, 'stlth':None}
    }
}


weapon_dict = {
    'simple_melee': {
        'Club':             {'die_num': 1, 'dmg_num': 4, 'finesse': False, 'versatile': None,  'range': '5ft', 'prop': 'Light'},
        'Dagger':           {'die_num': 1, 'dmg_num': 4, 'finesse': True,  'versatile': None,  'range': '5ft', 'prop': 'Finesse, light, thrown(range 20/60)'},
        'Greatclub':        {'die_num': 1, 'dmg_num': 8, 'finesse': False, 'versatile': None,  'range': '5ft', 'prop': 'Two-handed'},
        'Handaxe':          {'die_num': 1, 'dmg_num': 6, 'finesse': False, 'versatile': None,  'range': '5ft', 'prop': 'Light, thrown (range 20/60'},
        'Javelin':          {'die_num': 1, 'dmg_num': 6, 'finesse': False, 'versatile': None,  'range': '5ft', 'prop': 'Thrown (range 30/120)'},
        'Light hammer':     {'die_num': 1, 'dmg_num': 4, 'finesse': False, 'versatile': None,  'range': '5ft', 'prop': 'Light, thrown (range 20/60)'},
        'Mace':             {'die_num': 1, 'dmg_num': 6, 'finesse': False, 'versatile': None,  'range': '5ft', 'prop': ''},
        'Quarterstaff':     {'die_num': 1, 'dmg_num': 6, 'finesse': False, 'versatile': '1d8', 'range': '5ft', 'prop': 'Versatile (1d8)'},
        'Sickle':           {'die_num': 1, 'dmg_num': 4, 'finesse': False, 'versatile': None,  'range': '5ft', 'prop': 'Light'},
        'Spear':            {'die_num': 1, 'dmg_num': 6, 'finesse': False, 'versatile': '1d8', 'range': '5ft', 'prop': 'Thrown (range 20/60), versatile (1d8)'}
    },
    'martial_melee': {
        'Battleaxe':        {'die_num': 1, 'dmg_num': 8, 'finesse': False, 'versatile': '1d10','range': '5ft', 'prop': 'Versatile (1d10)'},
        'Flail':            {'die_num': 1, 'dmg_num': 8, 'finesse': False, 'versatile': None,  'range': '5ft', 'prop': ''},
        'Glaive':           {'die_num': 1, 'dmg_num': 10,'finesse': False, 'versatile': None,  'range': '10ft', 'prop': 'Heavy, reach, two-handed'},
        'Greataxe':         {'die_num': 1, 'dmg_num': 12,'finesse': False, 'versatile': None,  'range': '5ft', 'prop': 'Heavy, two-handed'},
        'Greatword':        {'die_num': 2, 'dmg_num': 6, 'finesse': False, 'versatile': None,  'range': '5ft', 'prop': 'Heavy, two-handed'},
        'Halberd':          {'die_num': 1, 'dmg_num': 10,'finesse': False, 'versatile': None,  'range': '10ft', 'prop': 'Heavy, reach, two-handed'},
        'Lance':            {'die_num': 1, 'dmg_num': 12,'finesse': False, 'versatile': None,  'range': '10ft', 'prop': 'Reach, special'},
        'Longsword':        {'die_num': 1, 'dmg_num': 8, 'finesse': False, 'versatile': '1d10','range': '5ft', 'prop': 'Versatile (1d10)'},
        'Maul':             {'die_num': 2, 'dmg_num': 6, 'finesse': False, 'versatile': None,  'range': '5ft', 'prop': 'Heavy, two-handed'},
        'Morningstar':      {'die_num': 1, 'dmg_num': 8, 'finesse': False, 'versatile': None,  'range': '5ft', 'prop': ''},
        'Pike':             {'die_num': 1, 'dmg_num': 10,'finesse': False, 'versatile': None,  'range': '10ft', 'prop': 'Heavy, reach, two-handed'},
        'Rapier':           {'die_num': 1, 'dmg_num': 8, 'finesse': True,  'versatile': None,  'range': '5ft', 'prop': 'Finesse'},
        'Scimitar':         {'die_num': 1, 'dmg_num': 6, 'finesse': True,  'versatile': None,  'range': '5ft', 'prop': 'Finesse, light'},
        'Shortword':        {'die_num': 1, 'dmg_num': 6, 'finesse': True,  'versatile': None,  'range': '5ft', 'prop': 'Finesse'},
        'Trident':          {'die_num': 1, 'dmg_num': 6, 'finesse': False, 'versatile': '1d8', 'range': '5ft', 'prop': 'Thrown (range 20/60), versatile(1d8)'},
        'War pick':         {'die_num': 1, 'dmg_num': 8, 'finesse': False, 'versatile': None,  'range': '5ft', 'prop': ''},
        'Warhammer':        {'die_num': 1, 'dmg_num': 8, 'finesse': False, 'versatile': '1d10','range': '5ft', 'prop': 'Versatile (1d10)'},
        'Whip':             {'die_num': 1, 'dmg_num': 4, 'finesse': True,  'versatile': None,  'range': '10ft', 'prop': 'Finese, reach'}
    },
    'simple_ranged': {
        'Light crossbow':   {'die_num': 1, 'dmg_num': 8, 'finesse': True,  'versatile': None,  'range': '80/320ft', 'prop': 'Ammunition, loading, two-handed'},
        'Dart':             {'die_num': 1, 'dmg_num': 4, 'finesse': True,  'versatile': None,  'range': '20/60ft',  'prop': 'Finesse, thrown'},
        'Shortbow':         {'die_num': 1, 'dmg_num': 6, 'finesse': True,  'versatile': None,  'range': '80/320ft', 'prop': 'Ammunition, two-handed'},
        'Sling':            {'die_num': 1, 'dmg_num': 4, 'finesse': True,  'versatile': None,  'range': '30/120ft', 'prop': 'Ammunition'}
    },
    'martial_ranged': {
        'Blowgun':          {'die_num': 1, 'dmg_num': 1, 'finesse': True,  'versatile': None,  'range': '25/100ft', 'prop': 'Ammunition, loading'},
        'Hand crossbow':    {'die_num': 1, 'dmg_num': 6, 'finesse': True,  'versatile': None,  'range': '30/120ft', 'prop': 'Ammunition, light, loading'},
        'Heavy crossbow':   {'die_num': 1, 'dmg_num': 10,'finesse': True,  'versatile': None,  'range': '100/400ft', 'prop': 'Ammunition, heavy, loading, two-handed'},
        'Longbow':          {'die_num': 1, 'dmg_num': 8, 'finesse': True,  'versatile': None,  'range': '150/600ft', 'prop': 'Ammunition, heavy, two-handed'},
        'Net':              {'die_num': None, 'dmg_num': None, 'finesse': True, 'versatile': None,  'range': '5/15ft','prop': 'Special, thrown'}
    }
}


special_ability_key = {

}


special_ability_dict = {                # Name: Name of ability. Action: 0 = action 1 = bonus action 2 = reaction. Description

}


spell_dict = {

}