from .type_charts import defensive_type_chart

def scout_type_matchups(my_types, opponent_types):
    print(get_defensive_profile(['steel', 'psychic']))


def get_defensive_profile(types):
    '''
    Takes a list of containing the types of a pokemon

    Returns a dictionary containing the damage multiplier
    for each type of attack on the pokemon

    Currently does not support ablilites, items, or anything else
    that would effect resistances/weaknesses besides typing
    '''

    # initial defensive profile for a pokemon
    # all multipliers are 1, meaning no attack is super effective or not very effective
    defensive_profile = {
        'normal': 1,
        'fire': 1,
        'water': 1,
        'grass': 1,
        'electric': 1,
        'ice': 1,
        'fighting': 1,
        'poison': 1,
        'ground': 1,
        'flying': 1,
        'psychic': 1,
        'bug': 1,
        'rock': 1,
        'ghost': 1,
        'dragon': 1,
        'dark': 1,
        'steel': 1
    }

    for type in types:
        for weakness in defensive_type_chart[type]['weaknesses']:
            defensive_profile[weakness] *= 2
        for resistance in defensive_type_chart[type]['resistances']:
            defensive_profile[resistance] /= 2
        for immunity in defensive_type_chart[type]['immunities']:
            defensive_profile[immunity] *= 0

    return defensive_profile