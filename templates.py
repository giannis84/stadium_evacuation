test_template = {
    'dimensions': [40, 40],
    1: {'type': 'wall', 'x': [10, 30], 'y': [10, 10]},
    2: {'type': 'wall', 'x': [10, 30], 'y': [30, 30]},
    3: {'type': 'wall', 'x': [30, 30], 'y': [10, 30]},
    4: {'type': 'wall', 'x': [10, 10], 'y': [10, 30]},
    5: {'type': 'gate', 'x': [10, 10], 'y': [19, 21]},
    6: {'type': 'inside', 'x': [11, 29], 'y': [11, 29]}
}


def big_stadium():
    n_rows = 60
    stage_size = [100,180]
    stadium_size = [stage_size[0]+n_rows*2,stage_size[1]+n_rows*2]
    template_size = [int(stadium_size[0]*1.5),int(stadium_size[1]*1.5)]

    x_min = int((template_size[1]-stadium_size[1])/2)
    y_min = int((template_size[0]-stadium_size[0])/2)
    x_max = x_min + stadium_size[1]
    y_max = y_min + stadium_size[0]

    template = {}
    template.update({'dimensions':template_size})

    template.update({'outer wall 1':{'type':'wall','x':[x_min,x_max],'y':[y_min,y_min]}})
    template.update({'outer wall 2':{'type':'wall','x':[x_min,x_max],'y':[y_max,y_max]}})
    template.update({'outer wall 3':{'type':'wall','x':[x_min,x_min],'y':[y_min,y_max]}})
    template.update({'outer wall 4':{'type':'wall','x':[x_max,x_max],'y':[y_min,y_max]}})
    
    template.update({'stage':{'type':'wall','x':[int((template_size[1]-stage_size[1])/2),int((template_size[1]-stage_size[1])/2+stage_size[1])],'y':[int((template_size[0]-stage_size[0])/2),int((template_size[0]-stage_size[0])/2)+stage_size[0]]}})

    for i in range(int((stadium_size[0]-stage_size[0])/4)):
        template.update({'upper '+str(i):{'type':'wall','x':[x_min+2*i,x_max-2*i],'y':[y_min+2*i,y_min+2*i]}})
        template.update({'lower '+str(i):{'type':'wall','x':[x_min+2*i,x_max-2*i],'y':[y_max-2*i,y_max-2*i]}})

    for j in range(int((stadium_size[1]-stage_size[1])/4)):
        template.update({'leftmost '+str(j):{'type':'wall','x':[x_min+2*j,x_min+2*j],'y':[y_min+2*j,y_max-2*j]}})
        template.update({'rightmost '+str(j):{'type':'wall','x':[x_max-2*j,x_max-2*j],'y':[y_min+2*j,y_max-2*j]}})

    template.update({'path 1':{'type':'path','direction':[1,1],'length':n_rows-1,'start':[x_min,y_min]}})
    template.update({'path 2':{'type':'path','direction':[1,-1],'length':n_rows-1,'start':[x_min,y_max]}})
    template.update({'path 3':{'type':'path','direction':[-1,1],'length':n_rows-1,'start':[x_max,y_min]}})
    template.update({'path 4':{'type':'path','direction':[-1,-1],'length':n_rows-1,'start':[x_max,y_max]}})
    template.update({'path 5':{'type':'path','direction':[1,0],'length':n_rows-1,'start':[x_min,int(y_min+stadium_size[0]/2)]}})
    template.update({'path 6':{'type':'path','direction':[-1,0],'length':n_rows-1,'start':[x_max,int(y_min+stadium_size[0]/2)]}})
    template.update({'path 7':{'type':'path','direction':[0,1],'length':n_rows-1,'start':[int(x_min+stadium_size[1]/3),y_min]}})
    #template.update({'path 8':{'type':'path','direction':[0,1],'length':n_rows-1,'start':[int(x_min+stadium_size[1]/2),y_min]}})
    template.update({'path 9':{'type':'path','direction':[0,1],'length':n_rows-1,'start':[int(x_max-stadium_size[1]/3),y_min]}})
    template.update({'path 10':{'type':'path','direction':[0,-1],'length':n_rows-1,'start':[int(x_min+stadium_size[1]/3),y_max]}})
    #template.update({'path 11':{'type':'path','direction':[0,-1],'length':n_rows-1,'start':[int(x_min+stadium_size[1]/2),y_max]}})
    template.update({'path 12':{'type':'path','direction':[0,-1],'length':n_rows-1,'start':[int(x_max-stadium_size[1]/3),y_max]}})

    template.update({'gate 1':{'type':'gate','x':[x_min,x_min+2],'y':[y_min,y_min]}})
    template.update({'gate 2':{'type':'gate','x':[int(x_min+stadium_size[1]/3)-1,int(x_min+stadium_size[1]/3)+1],'y':[y_min,y_min]}})
    #template.update({'gate 3':{'type':'gate','x':[int(x_min+stadium_size[1]/2)-1,int(x_min+stadium_size[1]/2)+1],'y':[y_min,y_min]}})
    template.update({'gate 4':{'type':'gate','x':[int(x_max-stadium_size[1]/3)-1,int(x_max-stadium_size[1]/3)+1],'y':[y_min,y_min]}})
    template.update({'gate 5':{'type':'gate','x':[x_max-2,x_max],'y':[y_min,y_min]}})
    template.update({'gate 6':{'type':'gate','x':[x_min,x_min],'y':[y_min,y_min+2]}})
    template.update({'gate 7':{'type':'gate','x':[x_min,x_min],'y':[int(y_min+stadium_size[0]/2)-1,int(y_min+stadium_size[0]/2)+1]}})
    template.update({'gate 8':{'type':'gate','x':[x_min,x_min],'y':[y_max-2,y_max]}})
    template.update({'gate 9':{'type':'gate','x':[x_max,x_max],'y':[y_min,y_min+2]}})
    template.update({'gate 10':{'type':'gate','x':[x_max,x_max],'y':[int(y_min+stadium_size[0]/2)-1,int(y_min+stadium_size[0]/2)+1]}})
    template.update({'gate 11':{'type':'gate','x':[x_max,x_max],'y':[y_max-2,y_max]}})
    template.update({'gate 12':{'type':'gate','x':[x_min,x_min+2],'y':[y_max,y_max]}})
    template.update({'gate 13':{'type':'gate','x':[int(x_min+stadium_size[1]/3)-1,int(x_min+stadium_size[1]/3)+1],'y':[y_max,y_max]}})
    #template.update({'gate 14':{'type':'gate','x':[int(x_min+stadium_size[1]/2)-1,int(x_min+stadium_size[1]/2)+1],'y':[y_max,y_max]}})
    template.update({'gate 15':{'type':'gate','x':[int(x_max-stadium_size[1]/3)-1,int(x_max-stadium_size[1]/3)+1],'y':[y_max,y_max]}})
    template.update({'gate 16':{'type':'gate','x':[x_max-2,x_max],'y':[y_max,y_max]}})



    template.update({'inside':{'type':'inside','x':[x_min+1,x_max-1],'y':[y_min+1,y_max-1]}})

    return template