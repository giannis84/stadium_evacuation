import numpy as np


def create_stadium(template):
    x = template['dimensions'][0]
    y = template['dimensions'][1]
    stadium = np.zeros([x, y])
    for element in template:
        if element != 'dimensions':
            if template[element]['type'] != 'path':
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
                        if ((template[element]['type']=='inside') & (stadium[j][i] == 0)):
                            stadium[j][i] = 3
            if template[element]['type'] == 'path':
                x_start = template[element]['start'][1]
                y_start = template[element]['start'][0]
                length = template[element]['length']
                dx = template[element]['direction'][1]
                dy = template[element]['direction'][0]
                for d in range(length):
                    i = d*dx+x_start
                    j = d*dy+y_start
                    stadium[i-1][j-1] = 0
                    stadium[i-1][j] = 0
                    stadium[i-1][j+1] = 0
                    stadium[i][j-1] = 0
                    stadium[i][j] = 0
                    stadium[i][j+1] = 0
                    stadium[i+1][j-1] = 0
                    stadium[i+1][j] = 0
                    stadium[i+1][j+1] = 0
    return stadium
