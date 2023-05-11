import pygame
import random


# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
score_num = 0

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

speed_times = 0

# Set colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

game = False
main = True

clock =pygame.time.Clock()
# Load images
back = pygame.image.load('background.png')
start = pygame.image.load('start.png')
multi = pygame.image.load('multi.png')
multi_t = False
add = pygame.image.load('add.png')
add_t = False
sub = pygame.image.load('sub.png')
sub_t = False
click_op = False
easy = pygame.image.load('easy.png')
med = pygame.image.load('medium.png')
hard = pygame.image.load('hard.png')
click_lev = False
# Load the custom cursor image
cursor_size = (40, 40)
cour =  pygame.image.load("normal-bear.png")
screenc = (SCREEN_WIDTH,SCREEN_HEIGHT)
# Set the cursor data
game_surface = pygame.Surface(screenc)

# Blit the game surface to the window

cursor_size = (40, 40)
cour =  pygame.image.load("normal-bear.png")
hard_t = False
easy_t = False
med_t = False
pygame.display.set_caption("Bear Blocks")

hb = False
sb =  False
# Start screen loop
while game == False and main:
    
    screen.fill(WHITE)
    screen.blit(back, (0, 0))
    
    screen.blit(add, (100, 50))
    screen.blit(sub, (325, 50))
    screen.blit(multi, (550, 50))
    screen.blit(easy, (300, 225))
    screen.blit(med, (300, 300))
    screen.blit(hard, (300, 375))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # left mouse button
            mouse_pos = pygame.mouse.get_pos()
            if start.get_rect(topleft=(282, 475)).collidepoint(mouse_pos):
                game = True
            if multi.get_rect(topleft=(550, 50)).collidepoint(mouse_pos):
                multi_t = True
                add_t = False
                add = pygame.image.load('add.png')
                multi = pygame.image.load('multi_selected.png')
                sub = pygame.image.load('sub.png')
                sub_t = False
                click_op = True
                
                
            if add.get_rect(topleft=(100, 50)).collidepoint(mouse_pos):
                multi_t = False
                add_t = True
                add = pygame.image.load('add_selected.png')
                multi = pygame.image.load('multi.png')
                sub = pygame.image.load('sub.png')
                sub_t = False
                click_op = True
                
            if sub.get_rect(topleft=(325, 50)).collidepoint(mouse_pos):
                multi_t = False
                add_t = False
                add = pygame.image.load('add.png')
                multi = pygame.image.load('multi.png')
                sub = pygame.image.load('sub_selected.png')
                sub_t = True
                click_op = True
            if easy.get_rect(topleft=(300, 225)).collidepoint(mouse_pos):
                life_num = 15
                
                hard_t = False
                easy_t = True
                med_t = False
                easy = pygame.image.load('easy_selected.png')
                med = pygame.image.load('medium.png')
                hard = pygame.image.load('hard.png')
                click_lev = True
            if med.get_rect(topleft=(300, 300)).collidepoint(mouse_pos):
                life_num = 10
                
                hard_t = False
                easy_t = False
                med_t = True
                easy = pygame.image.load('easy.png')
                med = pygame.image.load('medium_selected.png')
                hard = pygame.image.load('hard.png')
                click_lev = True
            if hard.get_rect(topleft=(300, 375)).collidepoint(mouse_pos):
                life_num = 5
                
                hard_t = True
                easy_t = False
                med_t = False
                easy = pygame.image.load('easy.png')
                med = pygame.image.load('medium.png')
                hard = pygame.image.load('hard_selected.png')
                click_lev = True

        # Get the position of the mouse cursor
    mouse_pos = pygame.mouse.get_pos()

    if click_op and click_lev:
        screen.blit(start, (282, 475)) 
    screen.blit(cour, (mouse_pos[0]-cursor_size[0]//2, mouse_pos[1]-cursor_size[1]//2))
    pygame.mouse.set_visible(False)       
                
    pygame.time.Clock().tick(60)           
    pygame.display.flip()
    pygame.display.update()


if game:
    running = True

    # Define Box class
    class Box(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.image.load('fish-block.png')
            self.image = pygame.transform.scale(self.image, (200, 70))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            
            # Generate a random calculation for this box
            if hard_t:
                if sub_t:
                    num = random.randint(1,19)
                    num1  = random.randint(10,50)
                if multi_t:
                    num = random.randint(0,12)
                    num1  = random.randint(0,12)
                if add_t:
                    num = random.randint(0,49)
                    num1  = random.randint(0,50)
                neg = random.randint(5,10)
            if easy_t:
                if sub_t:
                    num = random.randint(1,5)
                    num1  = random.randint(5,9)
                if multi_t:
                    num = random.randint(0,3)
                    num1  = random.randint(0,3)
                if add_t:
                    num = random.randint(0,9)
                    num1  = random.randint(0,9)
                neg = random.randint(1,5)
            if med_t:
                if sub_t:
                    num = random.randint(1,9)
                    num1  = random.randint(10,30)
                if multi_t:
                    num = random.randint(0,6)
                    num1  = random.randint(0,6)
                if add_t:
                    num = random.randint(0,30)
                    num1  = random.randint(0,30)
                neg = random.randint(6,16)
            if add_t:
                ans = num1 + num
            if multi_t:
                ans = num1 * num
            if sub_t:
                ans = num1 - num
            
            ansf = ans - neg
            ansi = ans + neg
            ran = random.randint(0,1)
            if add_t:
                if ran == 1:
                    self.calculation = (str(num1)+" + "+ str(num)+ " = " + str(ans))
                    self.is_ans = True
                else:
                    self.calculation = (str(num1)+" + "+ str(num)+ " = " + str(ansf or ansi))
                    self.is_ans = False
            if multi_t:
                if ran == 1:
                    self.calculation = (str(num1)+" X "+ str(num)+ " = " + str(ans))
                    self.is_ans = True
                else:
                    self.calculation = (str(num1)+" X "+ str(num)+ " = " + str(ansf or ansi))
                    self.is_ans = False
        
            if sub_t:
                if ran == 1:
                    self.calculation = (str(num1)+" - "+ str(num)+ " = " + str(ans))
                    self.is_ans = True
                else:
                    self.calculation = (str(num1)+" - "+ str(num)+ " = " + str(ansf or ansi))
                    self.is_ans = False
                    
            self.clicked = False
            self.click_count = 0
           
            if easy:
                self.speed = 0.5
            if med:
                self.speed = 1
            if hard:
                self.speed = 2
            
        
        def update(self):
            
            click_count =  0
            self.rect.y += self.speed

            # Check if box has left the screen
            if self.rect.y >= 510:
                # If box contains the correct answer, subtract from the score_num variable
                if self.is_ans and not self.clicked:
                    global score_num
                    score_num -= 1 
                
                # Remove the box sprite from the group
                self.kill()
                if self.rect.y == 510:
                    self.kill()
            # Check for mouse click event
            pygame.image.load('fish-block-green.png')
            if pygame.mouse.get_pressed()[0] and not self.clicked:  # left mouse button
                mouse_pos = pygame.mouse.get_pos()
                if self.rect.collidepoint(mouse_pos):
                    self.clicked = True
                    
                    if self.is_ans:
                        self.image = pygame.image.load('fish-block-green.png')
                        self.image = pygame.transform.scale(self.image, (200, 70))
                        score_num += 1
                        click_count += 1
                        global hb
                        hb = True
                        
                        if easy_t:   
                            if click_count == 1:
                                for box in boxes:
                                    box.speed += 0.5
                                    click_count =  0
                                
                        if med_t:   
                            if click_count ==1:
                                for box in boxes:
                                    box.speed += 0.5
                                    click_count =  0
                                
                        if hard_t:   
                            if click_count == 1:
                                for box in boxes:
                                    box.speed += 1
                                    click_count =  0                   
                    
                    else:
                        self.image = pygame.image.load('fish-block-red.png')
                        self.image = pygame.transform.scale(self.image, (200, 70))
                        global life_num
                        global sb
                        sb = True
                        life_num -= 1 
            
    all_sprites = pygame.sprite.Group()
    boxes = pygame.sprite.Group()
    
    clock = pygame.time.Clock()
    for i in range(30):
        x = random.randint(0, SCREEN_WIDTH - 200)
        y = i * -100
        box = Box(x, y)
        all_sprites.add(box)
        boxes.add(box)
    while running:
        
        back = pygame.image.load('background.png')
        screen.blit(back,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        screen.blit(back, (0, 0))
        
        # Render the score
        score_holder = pygame.image.load('speed.png')
        screen.blit(score_holder, (0, 530)) 
        score_ft = pygame.font.Font('freesansbold.ttf',32)
        score_num_str = "Score: "+str(score_num)
        score = score_ft.render(score_num_str, True, (0, 0, 0))
        screen.blit(score, (50, 550))
        life_holder = pygame.image.load('life.png')
        screen.blit(life_holder, (570, 530))        
        life_ft = pygame.font.Font('freesansbold.ttf',32)
        life_num_str = "Life: "+str(life_num)
        life = life_ft.render(life_num_str, True, (0, 0, 0))
        screen.blit(life, (650, 550))

        if life_num == 0:
        
            game = False
            main = True
            running = False
      
        # Get the position of the mouse cursor
        all_sprites.update()
        for box in boxes:
            
            # Render the calculation stored in this box instance
            ft = pygame.font.SysFont('Showcard Gothic', 24)
            ftforc = ft.render(box.calculation, True, (200, 0, 0))
            
            # Draw the box sprite
            screen.blit(box.image, box.rect)

            # Get the position of the box sprite and adjust it for the text
            text_x = box.rect.x + 60
            text_y = box.rect.y + 25

            # Draw the text surface at the adjusted position
            screen.blit(ftforc, (text_x, text_y))
        mouse_pos = pygame.mouse.get_pos()

    # Draw the cursor and trail effect onto the game surface
        screen.blit(cour, (mouse_pos[0]-cursor_size[0]//2, mouse_pos[1]-cursor_size[1]//2))
        pygame.mouse.set_visible(False)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)
pygame.quit()
