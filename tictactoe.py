board = [[0 for x in range(3)] for y in range(3)]

def printBoard():
	for i in range(len(board)):
			for j in range(len(board[i])):
				print(board[i][j], end=" ")
			print()

class Player:
	def __init__(self, _symbol):
		self.symbol = _symbol

	def turn(self):
		printBoard()
		chosen = self.selectInput()
		return self.checkWon(chosen)
	
	def selectInput(self):
		while True:
			selected = input("insert cell and row: ").replace(' ', '')
			if not ',' in selected: continue

			temp = selected.split(",")
			if temp[0].isnumeric() and temp[1].isnumeric():
				x,y = int(temp[0]), int(temp[1])
				
				if(x > 2 or y > 2): continue
				if(len(temp) > 2): continue

				if(board[x][y] != 0): continue
				else: 
					board[x][y] = self.symbol
					return x, y

	def checkWon(self, chosen):
		x, y = chosen[0], chosen[1]
		won = False

		# check lines
		if (board[x][0] == self.symbol and board[x][1] == self.symbol and board[x][2] == self.symbol):
			won = True
		if (board[0][y] == self.symbol and board[1][y] == self.symbol and board[2][y] == self.symbol):
			won = True

		# check diagonals
		if (board[0][0] == self.symbol and board[1][1] == self.symbol and board[2][2] == self.symbol):
			won = True
		if (board[0][2] == self.symbol and board[1][1] == self.symbol and board[2][0] == self.symbol):
			won = True
		return won

p1 = Player("X")
p2 = Player("O")

turn = 0
while turn < 9:
	print(f"turn {turn}:")
	if (turn % 2) == 0:		won = p1.turn()
	else: 								won = p2.turn()
	
	if won: break
	turn += 1

print("Final board!")
printBoard()