

#def raqspecs():
#    '''Record racqet specifications.'''
#    racquet=[]
#    rqspecs=input(str('Enter racquet specs in format of: Make/Model/Headsize '))
#    racquet.append(rqspecs)
#    return racquet
#print(raqspecs())

def raqspecs():
    '''Record racqet specifications.'''
    raqmake,raqmodel,raqsize=input('raquet make?  '),input('raquet model?  '),input('raqheadsize?  ')
    return (str.capitalize(raqmake),str.capitalize(raqmodel),int(raqsize))
    
print(raqspecs())
#print(int(raqspecs()[2]))






#[raqmake,raqmodel,raqsize]=input('raquet make?  '),input('raquet model?'),input('raqheadsize') 
#print(f'the racquet make is {raqmake}, the racquet model is {raqmodel}, racquet head size was {raqsize}')
