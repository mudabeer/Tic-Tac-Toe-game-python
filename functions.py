import string

#it text and remove all the special characters and return text without special characters
def special_c(text :str):
    new = text
    for _ in text:
        if _ in string.punctuation:
            new = new.replace( _ ,"")
    return new

#It the frame or map has input and then prints it based on the values
def map(frame :list[list[int]]):
    print('')
    for i in frame:
        print('\t',end="")
        for j in i:
            if j == -1:
                print('x\t',end='')
            elif j == 0:
                print('-\t',end='')
            elif j == 1:
                print('o\t',end='')
        print('\n')
    print('_'*50)

#It take the position number and return the indexs of the position
def index(num):
    if(num <= 3):
        return [0,num-1]
    elif(num <= 6):
        return [1,num-4]
    elif(num <= 9):
        return [2,num-7]

#It count the diagonal elements match based on the key and returns the counts 
def diagonal_check(frame :list[list[int]],  key :int):

    countw_1 = 0
    countw_2 = 0
    for i in range(3):
        if frame[i][i] == key:
            countw_1 = countw_1+1
        if frame[i][2-i] == key:
            countw_2 = countw_2+1
    return countw_1 , countw_2

#It count the  vertical and horizontal elements match based on the key and returns the counts with index cur
def VH_check(frame :list[list[int]],  key :int, rang, cur):
        
    countr = 0
    countc = 0
    for j in range(rang):
        if frame[cur][j] == key:
            countr = countr+1
        if frame[j][cur] == key:
            countc = countc+1
        
    if countr == rang or countc == rang:
        return countr,countc
    
    return 0,0


#It check that if there is any match or not
def win_check(frame :list[list[int]], key :int):
    
    #check there is any diagonal match if any then returns True
    count_d = diagonal_check(frame,key)
    if count_d[0] == 3 or count_d  == 3:
        return True
    
    #Check there is any horizontal and vertical match if any then returns True
    for i in range(3):

        check_vh = VH_check(frame,key,3,i)
        if check_vh[0] == 3 or check_vh[1] ==  3:
            return True
    #there is no match detected in previous steps then it returns False
    return False

#it checks if there is any possible match for next-move
def poss_match(frame :list[list[int]],key :int):

    # checks for the diagonal match
    check_d = diagonal_check(frame,key)
    if check_d[0] == 2:
        for j in range(3):
            if frame[j][j] == 0:
                return [j,j,True]
    if check_d[1] == 2:
        for j in range(3):
            if frame[j][2-j] == 0:
                return [j,2-j,True]
            
    #checks for the vertical and horizontal match
    for i in range(3):
        check_vh = VH_check(frame,key,2,i)
        if  check_vh[0] == 2:
            for j in range(3):
                if frame[i][j] == 0:
                    return [i,j,True]
        elif check_vh[1] == 2:
            for j in range(3):
                if frame[j][i] == 0:
                    return [j,i,True]

    #returns False if there is no match
    return [0,0,False]

#it check from 0 index to end if any space is there then it return the there indexs and True else False 
def random(frame :list[list[int]]):
    for m in range(3):
        for n in range(3):
            if frame[m][n] == 0:
                return [m,n,True]
    #return False if there is a draw
    else:
        return [0,0,False]
