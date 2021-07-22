import pygame, sys, time, random

#initial game variables

# Window size
frame_size_x = 720
frame_size_y = 480

#Parameters for Snake
snake_pos = [100, 50]
snake_body =[[100,50] , [100-10, 50], [100-(2*10), 50]] 
direc = 'RIGHT'
change_to = direc
direction = [10 , 0]

#Parameters for food
food_pos = [0,0]
food_spawn = False
food_shape = pygame.Surface([10, 10])
food_shape.fill((255,255,255))
score = 0

# Initialise game window
pygame.init()
pygame.display.set_caption('Snake Eater')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

# FPS (frames per second) controller to set the speed of the game
fps_controller = pygame.time.Clock()

def check_for_events():
    global direction
    global direc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if direc != 'DOWN':
                    direction[0] = 0
                    direction[1] = -10
                    direc = 'UP'
            elif event.key == pygame.K_DOWN:
                if direc != 'UP':
                    direction[0] = 0
                    direction[1] = 10
                    direc = 'DOWN'
            elif event.key == pygame.K_RIGHT:
                if direc != 'LEFT':
                    direction[0] = 10
                    direction[1] = 0
                    direc = 'RIGHT'
            elif event.key == pygame.K_LEFT:
                if direc != 'RIGHT':
                    direction[0] = -10
                    direction[1] = 0
                    direc = 'LEFT'

def update_snake():
    """
    This should contain the code for snake to move, grow, detect walls etc.
    """
    # Code for making the snake move in the expected direction
    global snake_body
    global food_spawn
    global score
    snake_body_head = [snake_body[0][0] + direction[0], snake_body[0][1] + direction[1]]
    
    if snake_body_head == food_pos:
        score = score +1
        food_spawn = False
        snake_body_update = snake_body[:]
    elif snake_body_head != food_pos:
        snake_body_update = snake_body[:-1]
    if snake_body_head[0] >= 720 or snake_body_head[0] <0 :
        game_over()
    if snake_body_head[1] < 0 or snake_body_head[1] >= 480:
        game_over()
    for head in snake_body:
        if snake_body_head == head:
            game_over()
    snake_body_update.insert(0, snake_body_head)
    snake_body = snake_body_update
    

    # Make the snake's body respond after the head moves. The responses will be different if it eats the food.
    # Note you cannot directly use the functions for detecting collisions 
    # since we have not made snake and food as a specific sprite or surface.
    # End the game if the snake collides with the wall or with itself. 
 
def create_food():
    """ 
    This function should set coordinates of food if not there on the screen. You can use randrange() to generate
    the location of the food.
    """
    global food_spawn
    global food_pos
    if food_spawn == False:
        food_pos[0] = 10*random.randint(0,frame_size_x/10-1)
        food_pos[1] = 10*random.randint(0,frame_size_y/10-1)
        game_window.blit(food_shape,food_pos)
        food_spawn = True
    elif food_spawn == True:
        game_window.blit(food_shape, food_pos)
        
def show_score(pos, color, font, size):
    """
    It takes in the above arguements and shows the score at the given pos according to the color, font and size.
    """
    global score
    font_1 = pygame.font.Font(font, size)
    Text = "Score :" + str(score)
    text = font_1.render(Text , True, color)
    
    game_window.blit(text, pos)

def update_screen():
    """
    Draw the snake, food, background, score on the screen
    """
    for blocks in snake_body:
        snake_surface = pygame.Surface((10,10))
        snake_surface.fill((0,255,0))
        game_window.blit(snake_surface,blocks)

def game_over():
    """ 
    Write the function to call in the end. 
    It should write game over on the screen, show your score, wait for 3 seconds and then exit
    """
    font_2 = pygame.font.Font(None, 75)
    font_3= pygame.font.Font(None, 35)
    text_1 = font_2.render("GAME OVER", True, (255,0,0,))
    text_2 = font_3.render("Score : " + str(score), True, (255,255,255)) 
    game_window.blit(text_2, (275,300))
    game_window.blit(text_1, (220,100))
    pygame.display.flip()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()
    
# Main loop
while True:
    # Make appropriate calls to the above functions so that the game could finally run
    check_for_events()
    game_window.fill((0,0,0))
    create_food()
    update_screen()
    update_snake()
    show_score([10,10], (255,255,255), None, 32)
    
    
    pygame.display.flip()
    # To set the speed of the screen
    fps_controller.tick(20)