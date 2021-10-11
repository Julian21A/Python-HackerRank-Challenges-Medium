def minion_game(string):
    vocales='AEIOU'
    
    puntos_kevin=0
    puntos_stuart=0
    
    for i in range(len(string)):
        if string[i] in vocales: puntos_kevin+= len(string)-i
        else: puntos_stuart+= len(string)-i
    
    if puntos_kevin>puntos_stuart: print('Kevin', puntos_kevin, end=' ')
    elif puntos_kevin<puntos_stuart: print('Stuart', puntos_stuart, end=' ')
    else: print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)