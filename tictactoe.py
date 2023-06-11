from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('400x550')
root.title('TIC TAC TOE')
root.config(bg='black')
root.resizable(0,0)

turn = "X"
end_game= False

#to check winner
def check_winner(player):
    #to check rows
    if board[1]==board[2] and board[2]==board[3] and board[3]==player:
        return True
    elif board[4]==board[5] and board[5]==board[6] and board[6]==player:
        return True
    elif board[7]==board[8] and board[8]==board[9] and board[9]==player:
        return True
    #to check coloumns
    elif board[1]==board[4] and board[4]==board[7] and board[7]==player:
        return True
    elif board[2]==board[5] and board[5]==board[8] and board[8]==player:
        return True
    elif board[3]==board[6] and board[6]==board[9] and board[9]==player:
        return True
    #to check diagonal
    elif board[1]==board[5] and board[5]==board[9] and board[9]==player:
        return True
    elif board[3]==board[5] and board[5]==board[7] and board[7]==player:
        return True
    return False
#to check for draw
def check_draw():
    for i in board.keys():
        if board[i]== " ":
            return False
        
    return True
#to restart the game
def restart():
    global end_game
    end_game= False
    for button in buttons:
        button["text"]= " "

    for i in board.keys():
        board[i]=" "

    label= Label(topframe, text="Tic Tac Toe", font=("arial",25), fg='white',bg='black',width=20)
    label.grid(row=0, column=0)
#adding ai opponent(minimiax algo)
def minimax(board, isMaximizing):
    if check_winner("O"):
        return 1
    elif check_winner("X"):
        return -1
    elif check_draw():
        return 0
    
    if isMaximizing:
        bestScore= -100

        for key in board.keys():
            if board[key] == " ":
                board[key] = "O"
                score= minimax(board, False) #minimax algo
                board[key] =" "
                if score > bestScore:
                    bestScore= score
        return bestScore
    
    else:
        bestScore= 100

        for key in board.keys():
            if board[key] == " ":
                board[key] = "X"
                score= minimax(board, True) #minimax algo
                board[key] =" "
                if score < bestScore:
                    bestScore= score
        return bestScore
#ai opponent
def computer_turn():
    bestScore= -100
    bestMove =0

    for key in board.keys():
        if board[key] == " ":
            board[key] = "O"
            score= minimax(board, False) #minimax algo
            board[key] =" "
            if score > bestScore:
                bestScore= score
                bestMove= key
    board[bestMove]= "O"
#button click
def b_click(event):
    global turn, end_game
    if end_game:
        return
    b1= event.widget
    bText=str(b1)
    clicked=bText[-1]
    if clicked =="n":
        clicked=1
    else:
        clicked=int(clicked)            

    if b1["text"]==" ":
        if turn =="X":
            board[clicked]=turn
            if check_winner(turn)== True:
                winninglabel= Label(topframe, text=f"{turn} wins the game",bg="black", fg='darkgrey',font=("arial",25), width= 20)
                winninglabel.grid(row=0, column=0, columnspan=3)
                end_game= True
            turn ="O"
            computer_turn()
            if check_winner(turn)== True:
                winninglabel= Label(topframe, text=f"{turn} wins the game",bg="black", fg='darkgrey',font=("arial",25), width= 20)
                winninglabel.grid(row=0, column=0, columnspan=3)
                end_game= True

            turn ="X"
            update_board()

        else:
            b1["text"]="O"
            board[clicked]=turn
            if check_winner(turn)== True:
                winninglabel= Label(topframe, text=f"{turn} wins the game",bg="black", fg='darkgrey',font=("arial",25), width= 20)
                winninglabel.grid(row=0, column=0, columnspan=3)
                end_game= True
            turn="X"

        if check_draw():
            winninglabel= Label(topframe, text="Game is drawn",bg='black', fg='grey',font=("arial",25),width= 20)
            winninglabel.grid(row=0, column=0, columnspan=3)
#board dictionary
board={1:" ", 2:" ", 3:" ",
       4:" ", 5:" ", 6:" ",
       7:" ", 8:" ", 9:" ",}
#update board with ai opponent
def update_board():
    for key in board.keys():
        buttons[key-1]["text"] = board[key]
#ui of game
topframe= Frame(root)
topframe.pack()
label= Label(topframe, text="Tic Tac Toe", font=("arial",25), bg='black', fg='white')
label.grid(row=0, column=0)
middleframe=Frame(root)
middleframe.pack()
b1= Button(middleframe, text=" ", font=("arial",35),height=2,width=4,bg="grey",bd=2)
b1.grid(row =0 ,column= 0)
b1.bind('<Button-1>', b_click)
b2= Button(middleframe, text=" ", font=("arial",35),height=2,width=4,bg="grey",bd=2)
b2.grid(row =0 ,column= 1)
b2.bind('<Button-1>', b_click)
b3= Button(middleframe, text=" ", font=("arial",35),height=2,width=4,bg="grey")
b3.grid(row =0 ,column= 2)
b3.bind('<Button-1>', b_click)
b4= Button(middleframe, text=" ", font=("arial",35),height=2,width=4,bg="grey")
b4.grid(row =1 ,column= 0)
b4.bind('<Button-1>', b_click)
b5= Button(middleframe, text=" ", font=("arial",35),height=2,width=4,bg="grey")
b5.grid(row =1 ,column= 1)
b5.bind('<Button-1>', b_click)
b6= Button(middleframe, text=" ", font=("arial",35),height=2,width=4,bg="grey")
b6.grid(row =1 ,column= 2)
b6.bind('<Button-1>', b_click)
b7= Button(middleframe, text=" ", font=("arial",35),height=2,width=4,bg="grey")
b7.grid(row =2 ,column= 0)
b7.bind('<Button-1>', b_click)
b8= Button(middleframe, text=" ", font=("arial",35),height=2,width=4,bg="grey")
b8.grid(row =2 ,column= 1)
b8.bind('<Button-1>', b_click)
b9= Button(middleframe, text=" ", font=("arial",35),height=2,width=4,bg="grey")
b9.grid(row =2 ,column= 2)
b9.bind('<Button-1>', b_click)
restartbutton= Button(middleframe, text="Reset Game", font=("arial",20),height=1,width=21, command=restart,bg="white", fg="black",bd=0)
restartbutton.grid(row =5 ,column= 0, columnspan=3)

buttons=[b1,b2,b3,b4,b5,b6,b7,b8,b9]

root.mainloop()  