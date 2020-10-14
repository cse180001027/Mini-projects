
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

choices = ['X', 'O']


win = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]


def isfree():
    for i in board:
        if i not in ('X','O'):
        	return True
    return False
    


def print_board():
    x=1
    for i in board:
        end = ' | '
        if x%3 == 0:
            end = ' \n'
            end+='---------\n';
        char=' '
        if i in ('X','O'): char=i;
        x+=1
        print(char,end=end)


player1 = 'O'
player2 = 'X'

player1 = input("choose symbol for player1 out of 'O' and 'X' " )

while player1 not in ('o','x','O','X'):
	player1 = input("choose symbol for player1 out of 'O' and 'X' only " )

if player1 == 'X' or player1 == 'x':
	player1 = 'X'
	player2 = 'O'
curplayer = player1
cont = False



def tictactoe():
	global board,cont,win,board,player1,player2,curplayer,choices
	while(cont or isfree()):

		cont = False

		print_board()
		move = int(input("enter your choice 1-9:   "))

		if move not in range(1,10):
			print("please enter valid choice 1-9:   ")
			cont = True
			continue
		if (board[move-1] in choices):
			print("please enter unoccupied values:    ")
			cont = True
			continue
		board[move-1] = curplayer
		for patt in win:
			if(board[patt[0]]==curplayer and 
				board[patt[1]]==curplayer and board[patt[2]]==curplayer):
				print("Congratulations  ",curplayer,"  You Won! ")
				print_board()
				return
				


		if curplayer == player1:
			curplayer = player2
		else:
			curplayer = player1

	print("It's a Tie. Oh god! you both are genius.")





if __name__== "__main__":
	tictactoe()
