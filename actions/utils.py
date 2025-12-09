import re

BASIC_ENERGY_TYPES = {
    "Water Energy":"base1-102",
    "Psychic Energy": "base1-101",
    "Lightning Energy": "base1-100",
    "Fighting Energy":"base1-97", 
    "Fire Energy": "base1-98",
    "Grass Energy": "base1-99",
    "Metal Energy":"bw1-111",
    "Darkness Energy":"bw1-112"

}

def pythonize_name(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    s1 = s1.replace(' ', '')
    s1 = s1.replace("'","_")
    s1 = s1.replace("-","_")
    s1 = s1.replace("__", "_")
    para_start = s1.find("(")
    if para_start > -1:
        s1 = s1[0:para_start]
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()