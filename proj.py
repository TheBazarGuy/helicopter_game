import pygame
import time
import random
pygame.init()
'''COLOURS'''
black=(0,0,0)
yellow=(255,255,0)
white=(255,255,255)

score=0
'''SIZE OF IMAGE'''
imageheight=43
imagewidth=100

'''RESOLUTION'''
surfaceHeight=400
surfaceWidth=800

'''CREATES A WINDOW'''
Surface=pygame.display.set_mode((surfaceWidth,surfaceHeight))
pygame.display.set_caption("Fly-or-Die")
clock=pygame.time.Clock() #Track time

img=pygame.image.load("Helicopter.png")  #Load Heli

def blocks(x_block,y_block,block_width,block_height,gap):
    pygame.draw.rect(Surface, white, [x_block, y_block, block_width, block_height])
    pygame.draw.rect(Surface, white, [x_block, y_block+block_height+gap, block_width, surfaceHeight])
  #  pygame.draw.rect(Surface, white, [x_block, surfaceHeight-y_block-gap+10, block_width, block_height])

def score_display(score):

    font=pygame.font.Font('freesansbold.ttf',20)
    text=font.render("Score:"+str(score),True,yellow)
    Surface.blit(text,[0,0])


def replay_quit():
    for event in pygame.event.get([pygame.KEYDOWN,pygame.QUIT]):
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x: #Check if 'X' key is pressed
                pygame.quit()
                quit()
            #continue
            return event.key
    return None


def makeTextObj(text,font):

    '''RETURS RECTANGLE OF REQUIRED TEXT'''

    textSurface = font.render(text,True,white)
    return textSurface, textSurface.get_rect()



def msg_display(text):
    smallText=pygame.font.Font('freesansbold.ttf',20)
    largeText=pygame.font.Font('freesansbold.ttf',130)

    bigtext, bigtextrect = makeTextObj(text,largeText)
    bigtextrect.center = surfaceWidth/2, surfaceHeight /2
    Surface.blit(bigtext,bigtextrect)

    minitext , minitextrect = makeTextObj("Press any key to restart",smallText)
    minitextrect.center=surfaceWidth/2 ,((surfaceHeight/2) +100)
    Surface.blit(minitext,minitextrect)

    minitext, minitextrect = makeTextObj("Press 'X' key to quit", smallText)
    minitextrect.center = surfaceWidth / 2, ((surfaceHeight / 2) + 120)
    Surface.blit(minitext, minitextrect)

    minitext, minitextrect = makeTextObj("Score is "+str(score), smallText)
    minitextrect.center = surfaceWidth / 2, ((surfaceHeight / 2) + 140)
    Surface.blit(minitext, minitextrect)

    global score
    score=0



    pygame.display.update()
    #time.sleep(1)

    while replay_quit()==None:
        clock.tick()
    main()



def func_game_over():
    msg_display('GAME OVER')

def kappa(x,y,image):
    Surface.blit(image,(x,y))

def main():
    global score
    '''IMAGE CO-ORDINATES'''
    x = 150
    y = 200

    y_move = 0

    x_block= surfaceWidth
    y_block =0
    block_width=75
    block_height=random.randint(0,surfaceHeight-100) #Generate a random number for height of block

    gap=imageheight*3
    block_move=4

    game_over = False

    '''GAME LOOP'''
    while not game_over:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:   #Close is clicked
                game_over=True
            if event.type==pygame.KEYDOWN:   #to check if button is pressed
                if event.key ==  pygame.K_UP: #K_UP is upper arrow key
                    y_move=-5 #Move Heli Up by 5 units

            if event.type == pygame.KEYUP:     #to check if released
                if event.key == pygame.K_UP:
                    y_move = 5 #Move Heli Down by 5 units

        y+=y_move
        Surface.fill(black)
        blocks(x_block,y_block,block_width,block_height,gap) #Function to create blocks
        x_block-=3 #Move Blocks by 3 units
        kappa(x,y,img)

        if y>surfaceHeight-40 or y<0:
            func_game_over()

        if x_block<(-1*block_width):
            x_block=surfaceWidth
            block_height=random.randint(0,surfaceHeight-100)

        '''CHECK UPPER BLOCK'''
        if x + imagewidth>x_block:
           if x < x_block+block_width:
                if y < block_height:
                    func_game_over()

        '''CHECK LOWER BLOCK'''
        if x+imagewidth>x_block:
            if x<x_block+block_width:
                if y +imageheight> block_height+gap:
                    func_game_over()

        '''CACLULATE SCORE'''
        if x<x_block and x>x_block-block_move:
            score=score +1
        score_display(score)
        pygame.display.update()
        clock.tick(60)
main()

pygame.quit()
quit()