# imports
import pandas as pd
from random import randrange

# creating data frame
id_list = []
for i in range(1, 2401):
    id_list.append(i)

def get_random_value():
    value_list = []
    for i in range(1, 2401):
        value_list.append(randrange(11))
    return value_list


def get_multiplied_value(multiplier):
    value_list = []
    for i in range(1, 11):
        value_list.extend([i] * multiplier)
    return value_list


regime_list = []
for i in range(1, 2401):
    if i < 1201:
        regime_list.append('S')
    else:
        regime_list.append('G')

plant_list = []
for i in range(1, 2401):
    if i < 801:
        plant_list.append('wheat')
    elif i < 1601:
        plant_list.append('barley')
    else:
        plant_list.append('smooth brome')

kairomone_list = []
for i in range(1, 2401):
    if i < 601:
        kairomone_list.append('control')
    elif i < 1201:
        kairomone_list.append('wheat')
    elif i < 1801:
        kairomone_list.append('barley')
    else:
        kairomone_list.append('smooth brome')

data = {'id': id_list,
        'regime': regime_list,
        'line': (get_multiplied_value(10)) * 24,
        'trial': (get_multiplied_value(1)) * 240,
        'start_plant': plant_list,
        'kairomone_source': kairomone_list,
        'start_numb': get_random_value(),
        'end_numb': get_random_value()
        }
df = pd.DataFrame(data)

# saving data frame
df.to_excel("../data/data_raw.xlsx",
            index=False)
