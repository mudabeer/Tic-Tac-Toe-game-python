import functions
import string

def main():
    print("\n                1        2       3\n                4        5       6\n                7        8       9")
    print("this are the postion of box according to the number or index shown above you can select any box\nfor example if press 0 the it select the row 1 and colum 1 box")
    print("after selecting the box now you can incert o by pressing o key")

    #It loops until the user enter invalid input or else loops
    while True:
        start_m = input("press 1 if want to play first move\npress 2 if want to play second\nchoice: ").lower()
        clean = functions.special_c(start_m)

        #check the given input is invalid input or not
        if clean in ['1','one','2','two']:
            break


    frame = [[0,0,0],[0,0,0],[0,0,0]]

    #check if the input is one then it print frame
    if clean in ['1','one']:
        functions.map(frame)

    #check if the input is two then it place first move in center
    elif clean in ['2','two']:
        frame[1][1] = 1
    
    #it loops until user or algorithm win the game or if the game draw
    while True:
        functions.map(frame)

        #it check there any draw if random returns False then its draw
        check = functions.random(frame)
        if check[2] == False:
            print('game draw')
            return 0
        
        #it loops until user enter a valid position
        while True:

            postion = int(input("enter index: "))
            if postion <= 9 and postion > 0:
                index = functions.index(postion)

                #check the position given is empty or already played position
                if frame[index[0]][index[1]] == 0:
                    frame[index[0]][index[1]] = -1
                    functions.map(frame)
                    break #if valid and empty position break the loop
                else:
                    print("you can not change played position")

            else:
                print("invalid index")

        #check if the user win the game -1 is used to represent the user moves, 1 for computer & 0 for empty position 
        check1 = functions.win_check(frame,-1)
        if check1 == False:

            #checks if playing next-move at certain position can win then it play the move or else skip
            move1 = functions.poss_match(frame,1)
            if move1[2] == True:
                frame[move1[0]][move1[1]] = 1
                check2 = functions.win_check(frame,1)
                if check2 == True:
                    functions.map(frame)
                    print('computer win the game')
                    return 0    
            else:
                #checks if user playing next-move at certain position can win then the computer place his move there
                move = functions.poss_match(frame,-1)
                if move[2] == True:
                    frame[move[0]][move[1]] = 1
                    check3 = functions.win_check(frame,1)
                    if check3 == True:
                        functions.map(frame)
                        print('computer win the game')
                        return 0
                else:
                    check4 = functions.random(frame)
                    if check4[2] == True:
                        frame[check4[0]][check4[1]] = 1
                    else:
                        print('game draw')
                        return 0
        else:
            functions.map(frame)
            print('you win the game')
            return 0
            
main()