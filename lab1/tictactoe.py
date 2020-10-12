board=[['','',''],['','',''],['','','_']]
count=0
man,comp=0,0
def display_board():
    for i in range(0,3):
        for j in range(0,3):
            print(board[i][j],end='   ')
        print("\n")
    print("\n")

def chk_won_zone(per):
    for i in range(0,3):
        if(board[i][0]==per and board[i][1]==per and board[i][2]==per):
            return 1;
    for j in range(0,3):
        if(board[0][j]==per and board[1][j]==per and board[2][j]==per):
            return 1;
    if(board[0][0]==per and board[1][1]==per and board[2][2]==per):
            return 1;
    if(board[0][2]==per and board[1][1]==per and board[2][0]==per):
            return 1;
    return 0;
def chk_win_zone(per):
    for i in range(0,3):
        if(board[i][0]==per and board[i][1]==per and board[i][2]=='_'):
            return 1,i,2;
        if(board[i][0]==per and board[i][1]=='_' and board[i][2]==per):
            return 1,i,1;
        if(board[i][0]=='_' and board[i][1]==per and board[i][2]==per):
            return 1,i,0;
    for j in range(0,3):
        if(board[0][j]==per and board[1][j]==per and board[2][j]=='_'):
            return 1,2,j;
        if(board[0][j]==per and board[1][j]=='_' and board[2][j]==per):
            return 1,1,j;
        if(board[0][j]=='_' and board[1][j]==per and board[2][j]==per):
            return 1,0,j;
    #diagonal 1
    if(board[0][0]=='_' and board[1][1]==per and board[2][2]==per):
            return 1,0,0;
    if(board[0][0]==per and board[1][1]=='_' and board[2][2]==per):
            return 1,1,1;
    if(board[0][0]==per and board[1][1]==per and board[2][2]=='_'):
            return 1,2,2;
    #diagonal 2
    if(board[0][2]=='_' and board[1][1]==per and board[2][0]==per):
            return 1,0,2;
    if(board[0][2]==per and board[1][1]=='_' and board[2][0]==per):
            return 1,1,1;
    if(board[0][2]==per and board[1][1]==per and board[2][0]=='_'):
            return 1,2,0;
    return 0,-1,-1
    
    
def comp_turn():
 global count
 if(count<9):
    count+=1
    res=-1
    res,row,col=chk_win_zone(comp)
    if(res==1):
        board[row][col]=comp
        if(chk_won_zone(comp)==1):
            display_board()
            print("Oho! You lost...")
            return
    elif(res==0):
        res1,row,col=chk_win_zone(man)
        if(res1==1):
            board[row][col]=comp
            display_board()
            
        else:
            for i in range(0,3):
                for j in range(0,3):
                    if(board[i][j]=='_'):
                        break
                if(board[i][j]=='_'):
                    board[i][j]=comp
                    break
            display_board()
            
    if(count==9):
            print("And it's a draw!,NO WIN NO LOSS")
            return 
    else:
        man_turn()
        
        
    
def man_turn():
 global count
 if(count<9):
    count+=1
    row=int(input("Enter the row (1 to 3) : "))
    col=int(input("Enter the col (1 to 3) : "))
    if(board[row-1][col-1]!='_'):
        print("Please enter the position that is not occupied!")
        count-=1
        man_turn()
    else:
        board[row-1][col-1]=man
        display_board()
        if(chk_won_zone(man)==1):
            print("Congo! You Won....PARTY?")
            return
        else:
            if(count==9):
                print("And it's a draw!,NO WIN NO LOSS")
                return
            else:
                comp_turn()
        
def main():
    global comp
    global man
    display_board()
    p=int(input('Enter 1 to play as first player or 2 to play second player : '))
    if(p==1):
        man=1
        comp=2
        man_turn()
    else:
        comp=1
        man=2
        comp_turn()

    
    
    
    
    
main()
