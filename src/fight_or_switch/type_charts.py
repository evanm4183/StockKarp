defensive_type_chart = {
    'normal': {
        'weaknesses': ['fighting'],
        'resistances': [],
        'immunities': ['ghost']
    },
    'fire': {
        'weaknesses': ['water', 'ground', 'rock'],
        'resistances': ['grass', 'bug', 'steel', 'ice', 'fire'],
        'immunities': []
    },
    'water': {
        'weaknesses': ['grass', 'electric'],
        'resistances': ['water', 'fire', 'ice', 'steel'],
        'immunities': []
    },
    'grass': {
        'weaknesses': ['fire', 'bug', 'poison', 'flying', 'ice'],
        'resistances': ['grass', 'water', 'ground', 'electric'],
        'immunities': []
    },
    'electric': {
        'weaknesses': ['ground'],
        'resistances': ['electric', 'flying', 'steel'],
        'immunities': []
    },
    'ice': {
        'weaknesses': ['fire', 'fighting', 'steel', 'rock'],
        'resistances': ['ice'],
        'immunities': []
    },
    'fighting': {
        'weaknesses': ['psychic', 'flying'],
        'resistances': ['bug', 'rock', 'dark'],
        'immunities': []
    },
    'poison': {
        'weaknesses': ['ground', 'psychic'],
        'resistances': ['poison', 'grass', 'bug', 'fighting'],
        'immunities': []
    },
    'ground': {
        'weaknesses': ['water', 'grass', 'ice'],
        'resistances': ['poison', 'rock'],
        'immunities': ['electric']
    },
    'flying': {
        'weaknesses': ['electric', 'rock', 'ice'],
        'resistances': ['grass', 'fighting', 'bug'],
        'immunities': ['ground']
    },
    'psychic': {
        'weaknesses': ['dark', 'bug', 'ghost'],
        'resistances': ['psychic', 'fighting'],
        'immunities': []
    },
    'bug': {
        'weaknesses': ['fire', 'flying', 'rock'],
        'resistances': ['grass', 'fire', 'ground'],
        'immunities': []
    },
    'rock': {
        'weaknesses': ['ground', 'fighting', 'water', 'grass', 'steel'],
        'resistances': ['normal', 'fire', 'poison', 'flying'],
        'immunities': []
    },
    'ghost': {
        'weaknesses': ['ghost', 'dark'],
        'resistances': ['poison', 'bug'],
        'immunities': ['normal', 'fighting']
    },
    'dragon': {
        'weaknesses': ['dragon', 'ice'],
        'resistances': ['water', 'grass', 'fire', 'electric'],
        'immunities': []
    },
    'dark': {
        'weaknesses': ['fighting', 'bug'],
        'resistances': ['ghost', 'dark'],
        'immunities': ['psychic']
    },
    'steel': {
        'weaknesses': ['fire', 'ground', 'fighting'],
        'resistances': ['normal', 'grass', 'ice', 'flying', 'psychic', 'bug', 'rock', 'dragon', 'steel', 'ghost', 'dark'],
        'immunities': ['poison']
    },
}