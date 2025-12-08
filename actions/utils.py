import re

def pythonize_name(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    s1 = s1.replace(' ', '')
    s1 = s1.replace("'","_")
    para_start = s1.find("(")
    if para_start > -1:
        s1 = s1[0:para_start]
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()