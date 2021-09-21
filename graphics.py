

def create_board(canvas):
    canvas.create_rectangle(0,0,800,800)
    for i in range(1,8):
        canvas.create_line(100*i,0,100*i,800)
        canvas.create_line(0,100*i,800,100*i)

def draw(canvas,player,position):
    if player == 1:
        canvas.create_line(position[1]*100,position[0]*100,(1+position[1])*100,(1+position[0])*100, fill = 'blue', width = 4)
        canvas.create_line((1+position[1])*100,position[0]*100,position[1]*100,(1+position[0])*100, fill = 'blue', width = 4)
    else:
        canvas.create_oval(position[1]*100,position[0]*100,(1+position[1])*100,(1+position[0])*100, outline = 'red', width = 4)

def make_text(canvas,win):
    if win == 1:
        canvas.create_text(400,400, text = 'Player 1 wins', font = 'Arial 20 bold')
    elif win == 2:
        canvas.create_text(400,400, text = 'Player 2 wins', font = 'Arial 20 bold')
