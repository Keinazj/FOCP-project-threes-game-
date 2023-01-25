board1 = []
board2 = []

n = int(input())
moves = ''

for i in range(n):
    mat1 = []
    a = input().split()
    for i in a:
        mat1+=[i]
    board1 +=[mat1]
    
num = int(input())

for i in range(num):
    mat2 = []
    b = input().split()
    for i in b:
        mat2+=[i]
    board2 +=[mat2]
    
#------------------------------------------------------------------------- movement function 

def left (board1):
    for list1 in board1: 
        
         for j in range(len(board1)):
             if j+1 < len(board1):
                 if list1[j] == '0':

                     
                     list1[j],list1[j+1]= list1[j+1],list1[j]
            
                 elif list1[j] !='0' and list1[j] == list1[j+1] and list1[j]!='1' and list1[j]!='2':
            
                    list1[j] = str(int(list1[j]) + int(list1[j+1]))
                    list1[j+1] = '0'
                    
                 elif (list1[j]=='1' and list1[j+1]=='2') or (list1[j] =='2' and list1[j+1] =='1'):
                    list1[j] = str(int(list1[j]) + int(list1[j+1]))
                    list1[j+1] ='0'
    
    return (board1)
           
#--------------------------------------------------------------------------

def right(board1):
    for list1 in board1:
        
         for j in range(-1,-((len(board1))),-1):
             if j > -len(board1):
                 if list1[j] == '0':
                     list1[j],list1[j-1]= (list1[j-1],list1[j])
        
                 elif list1[j] !='0' and list1[j] == list1[j-1] and list1[j]!='1' and list1[j]!='2':
                        
                     list1[j] = str(int(list1[j]) + int(list1[j-1]))
                     list1[j-1] ='0'
                
                 elif (list1[j]=='1' and list1[j-1]=='2') or (list1[j] =='2' and list1[j-1] =='1'):
                     list1[j] = str(int(list1[j]) + int(list1[j-1]))
                     list1[j-1] = '0'
               
            
         
    return (board1)
      
#--------------------------------------------------------------------------
        
def up(board):
    
    for i in range(len(board)):
        for j in range(len(board)):
            if j+1 < len(board):
            
                if int(board[j][i]) == 0:                                
                        board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
                        
                elif int(board[j][i]) >2 and (board[j][i]) == board[j+1][i] :
                    (board[j][i]) = str((int(board[j][i])) + (int(board[j+1][i])))
                    (board[j+1][i]) = '0'
                  
                elif (board[j][i] == '1' and board[j+1][i] == '2') or( board[j][i] =='2' and board[j+1][i] == '1'):
                     (board[j][i]) = str(int(board[j][i]) + int(board[j+1][i]))
                     board[j+1][i] = '0'
                    
            
    return (board )
#--------------------------------------------------------------------------
                
def down(board):
    
    for i in range(-1,-(len(board1))-1,-1):
        for j in range(-1,-(len(board))-1,-1):
            if j-1 > -(len(board)+1):
            
                if int(board[j][i]) == 0:                                  
                        board[j][i], board[j-1][i] = board[j-1][i], board[j][i]
                        
                elif int(board[j][i]) >2 and board[j][i] == board[j-1][i] :
                    board[j][i] = str(int(board[j][i]) + int(board[j-1][i]))
                    board[j-1][i] ='0'
                    
                elif (board[j][i] == '1' and board[j-1][i] == '2') or( board[j][i] == '2' and board[j-1][i] == '1'):
                     (board[j][i]) = str(int(board[j][i]) + int(board[j-1][i]))
                     board[j-1][i] = '0'
                
    return board        
            
#-------------------------------------------------------------------------- counting zeros function

def count_zero_left(board1):
    
    m = 0
    for j in range(len(board1)):
        
        i = len(board1)-1
        if int(board1[j][i]) == 0:
            m+=1
    return m

#--------------------------------------------------------------------------

def count_zero_right(board1):
    
    m = 0
    for i in range(len(board1)):
        
        j = 0
        if int(board1[i][j]) == 0:
            m+=1
    return m

#--------------------------------------------------------------------------

def count_zero_up(board):
    
    m = 0
    for j in range(len(board)):
        
        i = len(board)-1
        if int(board[i][j]) == 0:
            m+=1
    return m 

#--------------------------------------------------------------------------
    
def count_zero_down(board):
    
    m = 0
    for j in range(len(board)):
        
        i = 0
        if int(board[i][j]) == 0:
            m+=1
    return m 

#-------------------------------------------------------------------------- add_random function

def add_random_down(board,d,mod):
        
    tedad0 = -1
    satr1 = board[0]
    for i in range(len(satr1)):
        if satr1[i] =='0':
            tedad0 +=1
            if tedad0 == mod:
               board[0][i] = d
               break
                
           
    return board
           
#--------------------------------------------------------------------------

def add_random_up(board,d,mod):
    
    tedad0 = -1
    satr = board[len(board)-1]
    for i in range(len(satr)):
        if satr[i] == "0":
            tedad0 +=1
            if tedad0 == mod:
                board[len(board)-1][i]= d
                break
               
    return board

#--------------------------------------------------------------------------

def add_random_right(board,d,mod):
    
    tedad0 = -1
    i = 0
    for j in range(len(board)):
        if board[j][i] == '0':
            tedad0+=1
            if tedad0 == mod:
                board[j][0] = d
                break

    return board

#--------------------------------------------------------------------------

def add_random_left(board,d,mod):

    tedad0 = -1
    i = -1
    for j in range(len(board)):
        if board[j][i] =='0':
            tedad0+=1
            if tedad0 ==mod:
                board[j][-1] = d
                break
           
    return board


#-------------------------------------------------------------------------- score function
def score(board,cboard):
    final_board = []
    score = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if int(board[i][j]) !=0 and int(board[i][j]) != 1 and int(board[i][j]) != 2:
                final_board+=[board[i][j]]
                
    for i in range(len(final_board)):
        x = int(final_board[i])//3
        k = 0
        while x%2 ==0:
            k+=1
            x//=2
        score +=3**(k+1)
    
       
    return score

#-------------------------------------------------------------------------- actual moves

count = -1

while count<num :
    k = board2[0][0]
    d = board2[0][1]
    cboard = [i[:] for i in board1]
    
    

# left
    
    while count<num : 
        k = board2[0][0] 
        d = board2[0][1] 
        cboard = [i[:] for i in board1]
        board1 = left(board1)
        if board1 != cboard:
            m2 = count_zero_left(board1) 
            if m2!=0:                    
                mod = int(k)%int(m2)     
                board1 = add_random_left(board1,d,mod)  
            moves+='L'
            count+=1
            del board2[0]
        else:
            break   
       
    
        
# down
            
    while count<num :
        k = board2[0][0]
        d = board2[0][1]
        cboard = [i[:] for i in board1]
        board1 = down(board1)

        if board1 != cboard:
            m2 = count_zero_down(board1)
            if m2!=0:
                
                mod = int(k)%int(m2)
                board1 = add_random_down(board1,d,mod)
            moves+='D'
            count+=1
            
            del board2[0]

                
        else:
            break
     
        
        
# right
        
    while count<num:
        k = board2[0][0]
        d = board2[0][1]
        cboard = [i[:] for i in board1]
        board1 = right(board1)

        if board1 != cboard:
            m2 = count_zero_right(board1)
            if m2!=0:
                
                mod = int(k)%int(m2)
                board1 = add_random_right(board1,d,mod)
            moves +='R'
            count +=1
            del board2[0]
                
        else:
            break
  
     
        
    
#up
    while count<num:
        k = board2[0][0]
        d = board2[0][1]
        cboard = [i[:] for i in board1]
        board1 = up(board1)
        if board1 != cboard:
            m2 = count_zero_up(board1)
            if m2 !=0:
                mod = int(k)%int(m2)
                board1 = add_random_up(board1,d,mod)
            moves +='U'
            count +=1
            del board2[0]
        else:
            break                 
         
    count+=1
#-------------------------------------------------------------------------- print part 

print(moves)

for i in range(n):
    for j in range(n):
        print(board1[i][j], end = "\t")
    print()
    
score = score(board1,cboard)

c2board =  [i[:] for i in board1]
c3board =  [i[:] for i in board1]
c4board =  [i[:] for i in board1]
c5board =  [i[:] for i in board1]
    
if  left(c2board) == board1 and right(c3board) == board1 and up(c4board) == board1 and down(c5board) == board1: # can't move anymore 
        print ("The final score is " + str(score) + '.')
else:        
        print ("The partial score is " + str(score) + '.')
                        