sudo = [[3,6,0,9,0,4,1,0,0],
        [0,0,0,0,0,0,0,7,0],
        [0,0,4,0,0,3,0,6,0],
        [9,0,5,0,1,0,8,0,7],
        [0,0,0,7,5,0,0,0,9],
        [0,0,0,0,0,0,0,3,0],
        [7,0,0,0,0,8,0,9,0],
        [0,0,3,5,4,0,0,0,8],
        [0,0,0,0,0,0,0,0,0]]

def isTrue(row,column,num):
    global sudo
    for i in range(0,9):
        if sudo[row][i] == num:
            return False
    
    for i in range(0,9):
        if sudo[i][column] == num:
            return False
        
    y = (row // 3) * 3   
    x = (column // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if sudo[y + i][x + j] == num:
                return False
    
    return True
count = 0
count2 = 0
def solve():
    global sudo,count,count2
    for row in range(0,9):
        for column in range(0,9):
            if sudo[row][column] == 0:
                for num in range(1,10):
                    if isTrue(row,column,num) == True:
                        sudo[row][column] = num
                        solve()
                        sudo[row][column] = 0
                return
    for i in sudo:
        for j in i:
            count += 1
            print('',j,end='   ')
            if count % 3 == 0 and count != 9:
                print('|',end = '  ')
            elif count == 9:
                print('')
                count = 0
        count2 += 1 
        if count2 % 3 == 0 and count2 != 9:
            print('\n''__  ___   ___    __    ___   __    ___   ___   __ ','\n')
        elif count2 == 9:
            print('')
        else:
            print('\n')
   
    input('Press "Enter" for more possible solutions: ')
solve()

