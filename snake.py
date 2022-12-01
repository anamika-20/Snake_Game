import pygame
import random
pygame.init()
pygame.mixer.init()

#colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
MAROON=(153, 3, 31)
DGREEN=(24, 99, 26)


screen_width=800
screen_height=500


#creating window
gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("PYTHONSNAKE GAME")
pygame.display.update()

bgimg=pygame.image.load("fgh.jpg")
bgimg=pygame.transform.scale(bgimg, (screen_width,screen_height)).convert_alpha()
#convertaplha helps not to disturb the speed of game when we load the game loop again and again

bgimg1=pygame.image.load("def.jpg")
bgimg1=pygame.transform.scale(bgimg1, (screen_width,screen_height)).convert_alpha()

bgimg2=pygame.image.load("game.jpg")
bgimg2=pygame.transform.scale(bgimg2, (screen_width,screen_height)).convert_alpha()

clock=pygame.time.Clock()
font=pygame.font.SysFont('rockwell',30,bold=True)
font2=pygame.font.SysFont('comicsansms',30,bold=True)

a=pygame.font.get_fonts()
#print(a)

def welcome():
    exit_game=False
    while not exit_game:
        #gameWindow.fill(WHITE)
        gameWindow.blit(bgimg1,(0,0))
        text_screen("WELCOME TO PYTHON ON PYTHON",MAROON,100,200)
        text_screen("Press space bar to play!!",MAROON,200,250)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load('theme.mp3')
                    pygame.mixer.music.play(5)
                    gameloop()
        
        pygame.display.update()
        clock.tick(60)

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color) 
    gameWindow.blit(screen_text,[x,y])  #screen update

def text_screen2(text,color,x,y):
    screen_text=font2.render(text,True,color) 
    gameWindow.blit(screen_text,[x,y])  #screen update

#plots all the coordinates the snake traveerses
def plot_snake(gameWindow,color,s_list, s_size):
    for x,y in s_list:
        pygame.draw.rect(gameWindow,color,[x,y,s_size, s_size])



#gameloop
def gameloop():
    #game specification variable
    exit_game=False
    game_over=False
    s_x=45
    s_y=45
    s_size=20
    fps=30
    vel_x=0
    vel_y=0
    food_x=random.randint(20,screen_width)
    food_y=random.randint(20,screen_height)
    score=0
    init_velocity=5
    s_len=1
    s_list=[]
    with open("Highscore.txt","r") as f:
        Highscore = f.read()

    while not exit_game:
        if game_over:
            
            with open("Highscore.txt","w") as f:
                f.write(str(Highscore))

            #gameWindow.fill(WHITE)
            gameWindow.blit(bgimg2,(0,0))
           
            text_screen2("PRESS ENTER TO CONTINUE!",BLACK,170,300)
            
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game=True
                    
                    #if enter is pressed after the player losses the game restarts
                    if event.type == pygame.KEYDOWN:
                        if event.key==pygame.K_RETURN:
                            welcome()
        
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        vel_x=init_velocity
                        vel_y=0

                    if event.key == pygame.K_LEFT:
                        vel_x=-init_velocity
                        vel_y=0

                    if event.key == pygame.K_UP:
                        vel_y=-init_velocity
                        vel_x=0

                    if event.key == pygame.K_DOWN:
                        vel_y=init_velocity
                        vel_x=0


            s_x=s_x+vel_x
            s_y=s_y+vel_y

            if abs(s_x-food_x)<8 and abs(s_y-food_y)<8:
                score+=10
                food_x=random.randint(20,screen_width/2)
                food_y=random.randint(20,screen_height/2)
                s_len+=5
                if score>int(Highscore):
                    Highscore=score


            #gameWindow.fill(WHITE)
            gameWindow.blit(bgimg,(0,0))
            text_screen2("Score= "+str(score) +"Highscore=  "+str(Highscore),MAROON,5,5)
            pygame.draw.rect(gameWindow,RED,[food_x,food_y, s_size , s_size])
            
            #to start the game
            head=[]
            head.append(s_x)
            head.append(s_y)
            s_list.append(head)

            #to increase snake size after every gain in points
            if len(s_list)>s_len:
                del s_list[0]

            #if coordinate of head is same as any other coordinates in the list except the last coordinate since it the head itself...the game will be over
            if head in s_list[:-1]:
                game_over=True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            #game over when the snake collides with the walls
            if s_x<0 or s_x>screen_width or s_y<0 or s_y>screen_height:
                game_over=True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            #pygame.draw.rect(gameWindow,BLACK,[s_x , s_y , s_size , s_size])  
            plot_snake(gameWindow,DGREEN, s_list , s_size) 
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()