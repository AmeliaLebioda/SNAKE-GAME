
import pygame
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake Game')
logo = pygame.image.load('logo.png')
headsquare = pygame.image.load('headhead.png')
greensquare = pygame.image.load('green.png')
purplesquare = pygame.image.load('purple.png')
bluesquare = pygame.image.load('blue.png')
redsquare = pygame.image.load('red.png')
violetsquare = pygame.image.load('violet.png')
pygame.display.set_icon(logo)

segmentlist = [greensquare,purplesquare,bluesquare,redsquare,violetsquare]
clock = pygame.time.Clock()

FPS =8
                       
direction =  "right"
smallfont = pygame.font.SysFont("comicsansms", 20)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 70)


def score (score):
    text = smallfont.render ("Score: " +str (score), True, black)
    gameDisplay.blit(text,  [0,0])

def text_objects(text, color, size):
    if size == "small":
        textSurface=smallfont.render(text, True, color)
    elif size == "med":
        textSurface=medfont.render(text, True, color)
    elif size == "large":
        textSurface=largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width/2),(display_height/2)+ y_displace
    gameDisplay.blit(textSurf, textRect)

def snake(block_size, snakelist):

    gameDisplay.blit(headsquare, (snakelist [-1] [0], snakelist [-1][1]))
    gameDisplay.blit(greensquare, (snakelist [0] [0], snakelist [0][1]))

    segmentcounter=1
    
    for body in snakelist[1:-1]:
       
    
        party = segmentlist [segmentcounter]
        gameDisplay.blit(party, (body[0],body[1]))
        
        segmentcounter+=1
        if segmentcounter == 5:
            segmentcounter=0
        
    
  
def pause ():
    paused = True
    message_to_screen("paused", black , -100, size = "large")
    message_to_screen ("Press C to continue or Q to quit", black, 25)
    pygame.display.update()


    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        
    
def start_menu():
    intro =True
    
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    intro = False

        gameDisplay.fill(white)
        message_to_screen("Welcome to Slither" , red, -100,"large")
        message_to_screen("The rules and functionalities are:", black, -20, "small" )
        message_to_screen ( "The snake can move in four directions.",black, 10, "small")
        message_to_screen("When the snake eats food its tail becomes longer." , black, 30, "small")
        message_to_screen("Food appears in random places.", black, 50, "small")
        message_to_screen("The game is over when the snake bites itself." ,black, 70, "small"  )
        message_to_screen("Press C to play, P to pause or Q to quit", black, 150,"small")
        
        pygame.display.update()
        clock.tick(10)

         
def gameLoop():
    global direction
    segmentcounter=3
    
    gameExit = False
    gameOver = False

    snakeList =[[display_width/2,display_height/2]]
    
    snakeLenght = 2

    block_size=25
    #if snakeLenght < 5:
     #   FPS = 2
    #else:
     #   FPS = 20
        
    lead_x = display_width/2 
    lead_y = display_height/2 
    lead_x_change = block_size
    lead_y_change = 0
    
    
    applelocationx = []
    xapple = block_size
    while xapple<= display_width - block_size:
        applelocationx.append(xapple)
        xapple=xapple+block_size

    applelocationy = []
    yapple = block_size
    while yapple<= display_height - block_size:
        applelocationy.append(yapple)
        yapple=yapple+block_size

    randAppleX = random.choice(applelocationx)
    randAppleY = random.choice(applelocationy)
    
    
    
    while not gameExit:
        if gameOver == True:
            
            message_to_screen("GAME OVER",red, -100, size ="large")
            message_to_screen("Press C to play again or Q to quit",black, 50, size = "small")
            
            pygame.display.update()
        while gameOver == True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit==True
                    gameOver==False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        direction = "right"
                        gameLoop()
            
                
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0

                elif event.key == pygame.K_p:
                    pause()
        if lead_x>=display_width or lead_x<0 or lead_y>=display_height or lead_y<0:
           gameOver = True
                
        lead_x +=  lead_x_change
        lead_y +=  lead_y_change
        gameDisplay.fill(white)
        
        AppleThickness =25
        
        if snakeLenght == 2:
            appleimage = purplesquare
        gameDisplay.blit(appleimage, (randAppleX,randAppleY))
        snakeHead=[]
        
    
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
       
        if len(snakeList) > snakeLenght:
            del snakeList[0]
        

        for eachSegment in snakeList [:-1]:
            if eachSegment == snakeHead:
                gameOver=True
       
        score(snakeLenght - 2)
        snake(block_size,snakeList)
        pygame.display.update()

        if lead_x>randAppleX-AppleThickness and lead_x<randAppleX+ AppleThickness:
            if lead_y>randAppleY - AppleThickness and lead_y<randAppleY+AppleThickness:
               randAppleX=random.choice(applelocationx)
               randAppleY=random.choice(applelocationy)
               
               snakeLenght += 1
               segmentcounter=2
               for appleimage in snakeList[:-1]:
                   appleimage = segmentlist[segmentcounter]
                   
                   segmentcounter+=1
                   if segmentcounter == 5:
                       segmentcounter=0
        
        clock.tick(FPS)

    pygame.quit()
    quit()
start_menu()
gameLoop()

