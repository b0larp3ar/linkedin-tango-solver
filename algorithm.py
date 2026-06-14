E="empty"
X="sun"
O="moon"

board=[[E, X, E, E, E, O], 
       [E, E, E, X, E, E],
       [E, E, E, E, X, E],
       [E, E, E, E, E, E],
       [E, E, O, E, E, E],
       [O, E, E, E, E, E]]

equality=[((2,1),(3,1)), ((3,0),(4,0)), ((3,5),(4,5)), ((5,4),(5,5))]
opposite=[((0,1),(0,2)), ((3,2),(3,3)), ((4,3),(4,4)), ((5,3),(5,4))]

def isFilled(board):
    for i in range(6):
        for j in range(6):
            if board[i][j]==E:
                return False
    return True

def findEmpty(board):
    for i in range(6):
        for j in range(6):
            if board[i][j]==E:
                return i, j
                       
def checkEquality(board, r, c):
    pairs = []

    if r > 0:
        pairs.append(((r-1,c), (r,c)))
    if c > 0:
        pairs.append(((r,c-1), (r,c)))
    if c < 5: 
        pairs.append(((r,c), (r,c+1)))
    if r < 5:
        pairs.append(((r,c), (r+1,c)))

    for cell1, cell2 in equality:
        if (r,c) not in [cell1, cell2]:
            continue

        r1,c1 = cell1
        r2,c2 = cell2

        if board[r1][c1] != E and board[r2][c2] != E:
            if board[r1][c1] != board[r2][c2]:
                return False
            
    return True

def checkOpposite(board, r, c):
    pairs = []

    if r > 0:
        pairs.append(((r-1,c), (r,c)))
    if c > 0:
        pairs.append(((r,c-1), (r,c)))
    if c < 5: 
        pairs.append(((r,c), (r,c+1)))
    if r < 5:
        pairs.append(((r,c), (r+1,c)))

    for cell1, cell2 in opposite:
        if (r,c) not in [cell1, cell2]:
            continue

        r1,c1 = cell1
        r2,c2 = cell2

        if board[r1][c1] != E and board[r2][c2] != E:
            if board[r1][c1] == board[r2][c2]:
                return False
            
    return True

def checkThreeConsecutive(board, r, c):
    #horizontal checking
    if c>1:
        if board[r][c-2]==board[r][c-1]==board[r][c]!=E:
            return False
    if c<4:
        if board[r][c]==board[r][c+1]==board[r][c+2]!=E:
            return False
    if c>0 and c<5:
        if board[r][c-1]==board[r][c]==board[r][c+1]!=E:
            return False
        
    #vertical checking
    if r>1:
        if board[r-2][c]==board[r-1][c]==board[r][c]!=E:
            return False
    if r<4:
        if board[r][c]==board[r+1][c]==board[r+2][c]!=E:
            return False
    if r>0 and r<5:
        if board[r-1][c]==board[r][c]==board[r+1][c]!=E:
            return False
        
    return True

def checkRowSum(board, r, c):
    n1=0
    n2=0
    emptyFound=False
    for i in range(6):
        if board[r][i]==X:
            n1+=1
        elif board[r][i]==O:
            n2+=1
        else:
            emptyFound=True
        if n1>3 or n2>3:
            return False
    if emptyFound==True:
        return True
    return n1==n2

def checkColumnSum(board, r, c):
    n1=0
    n2=0
    emptyFound=False
    for i in range(6):
        if board[i][c]==X:
            n1+=1
        elif board[i][c]==O:
            n2+=1
        else:
            emptyFound=True
        if n1>3 or n2>3:
            return False
    if emptyFound==True:
        return True
    return n1==n2

def isValid(board, r, c):
    if checkEquality(board, r, c)==False:
        return False
    if checkOpposite(board, r, c)==False:
        return False
    if checkThreeConsecutive(board, r, c)==False:
        return False
    if checkRowSum(board, r, c)==False:
        return False
    if checkColumnSum(board, r, c)==False:
        return False
    return True
    
def solve(board):
    if isFilled(board):
        return True

    r,c=findEmpty(board)

    board[r][c]=X
    if isValid(board, r, c):
        if solve(board):
            return True
    
    board[r][c]=O
    if isValid(board, r, c):
        if solve(board):
            return True
        
    board[r][c]=E
    return False    

solve(board)

for i in board:
    print(i)