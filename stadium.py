import numpy as np

def create_stadium(template):
    x = template['dimensions'][0]
    y = template['dimensions'][1]
    stadium = np.zeros([x, y])
    for element in template:
        if element != 'dimensions':
            xstart = template[element]['x'][0]
            xend = template[element]['x'][1]
            ystart = template[element]['y'][0]
            yend = template[element]['y'][1]
            for i in range(xstart, xend+1):
                for j in range(ystart, yend+1):
                    if template[element]['type']=='wall':
                        stadium[j][i] = 1
                    if template[element]['type']=='gate':
                        stadium[j][i] = 2
    return stadium