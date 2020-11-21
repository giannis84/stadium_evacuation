import numpy as np


def create_stadium(template):
    x = template['dimensions'][0]
    y = template['dimensions'][1]
    stadium = np.zeros([x, y])
    for element in template:
        if element != 'dimensions':
            x_start = template[element]['x'][0]
            x_end = template[element]['x'][1]
            y_start = template[element]['y'][0]
            y_end = template[element]['y'][1]
            for i in range(x_start, x_end + 1):
                for j in range(y_start, y_end + 1):
                    if template[element]['type'] == 'wall':
                        stadium[j][i] = 1
                    if template[element]['type'] == 'gate':
                        stadium[j][i] = 2
    return stadium
