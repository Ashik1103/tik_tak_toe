moves={'TL':" ",'TC':" ",'TR':" ",
       'ML':" ",'MC':" ",'MR':" ",
       'LL':" ",'LC':" ",'LR':" "}
turn=True
for i in range(9):
    print(moves['TL']+"|"+moves['TC']+"|"+moves['TR'])
    print("_ _ _")
    print(moves['ML'] + "|" + moves['MC'] + "|" + moves['MR'])
    print("_ _ _")
    print(moves['LL'] + "|" + moves['LC'] + "|" + moves['LR'])

    if (moves['TL'] == 'X' and moves['TC'] == 'X' and moves['TR'] == 'X'):
        print("X is the winner")
        break
    elif (moves['ML'] == 'X' and moves['MC'] == 'X' and moves['MR'] == 'X'):
        print("X is the winner")
        break
    elif(moves['LL'] == 'X' and moves['LC'] == 'X' and moves['LR'] == 'X'):
        print("X is the winner")
        break
    elif(moves['TL'] == 'X' and moves['MC'] == 'X' and moves['LR'] == 'X'):
        print("X is the winner")
        break
    elif(moves['TR'] == 'X' and moves['MC'] == 'X' and moves['LL'] == 'X'):
        print("X is the winner")
        break
    elif(moves['TL'] == 'X' and moves['ML'] == 'X' and moves['LL'] == 'X'):
        print("X is the winner")
        break
    elif(moves['TC'] == 'X' and moves['MC'] == 'X' and moves['LC'] == 'X'):
        print("X is the winner")
        break
    elif(moves['TR'] == 'X' and moves['MR'] == 'X' and moves['LR'] == 'X'):
        print("X is the winner")
        break
    elif (moves['TL'] == 'O' and moves['TC'] == 'O' and moves['TR'] == 'O'):
        print("O is the winner")
        break
    elif (moves['ML'] == 'O' and moves['MC'] == 'O' and moves['MR'] == 'O'):
        print("O is the winner")
        break
    elif(moves['LL'] == 'O' and moves['LC'] == 'O' and moves['LR'] == 'O'):
        print("O is the winner")
        break
    elif(moves['TL'] == 'O' and moves['MC'] == 'O' and moves['LR'] == 'O'):
        print("O is the winner")
        break
    elif(moves['TR'] == 'O' and moves['MC'] == 'O' and moves['LL'] == 'O'):
        print("O is the winner")
        break
    elif(moves['TL'] == 'O' and moves['ML'] == 'O' and moves['LL'] == 'O'):
        print("O is the winner")
        break
    elif(moves['TC'] == 'O' and moves['MC'] == 'O' and moves['LC'] == 'O'):
        print("O is the winner")
        break
    elif(moves['TR'] == 'O' and moves['MR'] == 'O' and moves['LR'] == 'O'):
        print("O is the winner")
        break

    if turn==True:
        inp = input("Turn for X:")
        if(inp not in moves):
            print("please enter a valid position")
        if(inp in moves):
            if(moves[inp] is not None):
                print("Enter a position where its empty")
                inp=input("Turn for X:")
                moves[inp] = "X"
                turn = False
            else:
                moves[inp] = "X"
                turn = False



    elif turn==False:
        inp=input("Turn for O: ")
        if (inp not in moves):
            print("please enter a valid position")
        if(inp in moves):
            if (moves[inp] == 'X'):
                print("Enter a position where O is there")
                inp = input("Turn for O:")
                moves[inp] = "O"
                turn = True
            else:
                moves[inp] = "O"
                turn = True






