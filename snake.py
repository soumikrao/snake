import pygame as pg, sys, random
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

        self.head_up = pg.image.load('Snake Game/assets/head_up.png').convert_alpha()
        self.head_down = pg.image.load('Snake Game/assets/head_down.png').convert_alpha()
        self.head_right = pg.image.load('Snake Game/assets/head_right.png').convert_alpha()
        self.head_left = pg.image.load('Snake Game/assets/head_left.png').convert_alpha()

        self.tail_up = pg.image.load('Snake Game/assets/tail_up.png').convert_alpha()
        self.tail_down = pg.image.load('Snake Game/assets/tail_down.png').convert_alpha()
        self.tail_right = pg.image.load('Snake Game/assets/tail_right.png').convert_alpha()
        self.tail_left = pg.image.load('Snake Game/assets/tail_left.png').convert_alpha()

        self.body_vertical = pg.image.load('Snake Game/assets/body_vertical.png').convert_alpha()
        self.body_horizontal = pg.image.load('Snake Game/assets/body_horizontal.png').convert_alpha()

        self.body_tr = pg.image.load('Snake Game/assets/body_tr.png').convert_alpha()
        self.body_tl = pg.image.load('Snake Game/assets/body_tl.png').convert_alpha()
        self.body_br = pg.image.load('Snake Game/assets/body_br.png').convert_alpha()
        self.body_bl = pg.image.load('Snake Game/assets/body_bl.png').convert_alpha()

        self.crunch_sound = pg.mixer.Sound('Snake Game/assets/Sound_crunch.wav')

    def draw_snake(self):
        self.update_head_graphics()  # updating head graphic every frame
        self.update_tail_graphics() # updating tail graphic every frame

        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pg.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:  # direction of head
                screen.blit(self.head, block_rect)

            elif index == len(self.body)-1:  # index of the tail
                screen.blit(self.tail, block_rect)

            else:  # for the body
                previous_block = self.body[index-1] - block
                next_block = self.body[index+1] - block
                if previous_block.x == next_block.x:  # if both x coordinates are same then snake moving in vertical direction
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:  # if both y coordinates are same then snake moving in horizontal direction
                    screen.blit(self.body_horizontal, block_rect)
                else:  # for the corners
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)


    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]  # subtracting head coordinate from first body block coordinate to know direction of the body
        if head_relation == Vector2(1, 0):  # if coordinates are (1, 0) head is facing left side
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]  # subtracting head coordinate from first body block coordinate to know direction of the body
        if tail_relation == Vector2(1, 0):  # if coordinates are (1, 0) head is facing left side
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down


        #  for block in self.body:
        #      x_pos = int(block.x * cell_size)
        #      y_pos = int(block.y * cell_size)
        #      block_rect = pg.Rect(x_pos, y_pos, cell_size, cell_size)
        #      pg.draw.rect(screen, (183, 111, 122), block_rect)

    def move_snake(self):

        if self.new_block == True:  # if collision happens block is added
            body_copy = self.body[:]  # copying body only up to last block
            body_copy.insert(0, body_copy[0] + self.direction)  # inserting head
            self.body = body_copy  # giving self.body a new list
            self.new_block = False  # making it False for next frame
        else:
            body_copy = self.body[:-1]  # copying body only up to last second block
            body_copy.insert(0, body_copy[0] + self.direction)  # inserting head
            self.body = body_copy  # giving self.body a new list

    def add_block(self):  # adds a block to the snake body when it eats a fruit
        self.new_block = True

    def play_crunch_sounds(self):
        self.crunch_sound.play()


class FRUIT:  # making a fruit
    def __init__(self):  # creating a grid
        self.x = random.randint(0, cell_number-1)  # -1 so that we don't go outside screen
        self.y = random.randint(0, cell_number-1)
        self.pos = Vector2(self.x, self.y)  # creating a random position for the fruit

    def draw_fruit(self):
        fruit_rect = pg.Rect(int(self.pos.x*cell_size), int(self.pos.y*cell_size), cell_size, cell_size)  # creating a fruit as rect
        screen.blit(apple, fruit_rect)  # puts apple and a rectangle around it ono screen
        #  pg.draw.rect(screen, (126, 166, 114), fruit_rect)  # drawing it and putting on screen

    def randomize(self):  # for the random position update
        self.x = random.randint(0, cell_number - 1)  # -1 so that we don't go outside screen
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)  # creating a random position for the fruit


class MAIN:  # main game logic
    def __init__(self):
        self.snake = SNAKE()  # creates a snake object
        self.fruit = FRUIT()  # creates a fruit object

    def update(self):
        self.snake.move_snake()  # updates the screen
        self.check_collision()  # checks collision of fruit and snake every frame
        self.check_fail()

    def draw_element(self):
        self.draw_grass()  # draws grass
        self.fruit.draw_fruit()  # draws the fruit on screen
        self.snake.draw_snake()  # draws the snake on screen
        self.draw_score()  # draws score

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:  # if position of fruit and head it same
            self.fruit.randomize()  # put fruit at different random position
            self.snake.add_block()
            self.snake.play_crunch_sounds()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()  # if apple is under the snake it randomises again

    def check_fail(self):  # checks when snake dies
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:  # if snake hits the walls
            self.game_over()
        for block in self.snake.body[1:]:  # checking if snake hits itself
            if block == self.snake.body[0]:  # if head hits body
                self.game_over()

    def game_over(self):
        pg.quit()
        sys.exit()  # makes sure game closes totally

    def draw_grass(self):
        grass_color = (167, 209, 61)  # dark green
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pg.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pg.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pg.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pg.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x_pos = int(cell_size * cell_number - 60)
        score_y_pos = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center=(score_x_pos, score_y_pos))
        apple_rect = apple.get_rect(midright=(score_rect.left, score_rect.centery))

        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)

pg.mixer.pre_init(44100,-16,2,512)
pg.init()  # initiation
cell_size = 40
cell_number = 20
screen = pg.display.set_mode((cell_number*cell_size, cell_number*cell_size))  # setting display like an invisible grid of 80x80 cells and 800x800 pixels
clock = pg.time.Clock()  # influences time
apple = pg.image.load('Snake Game/assets/apple.png').convert_alpha()
game_font = pg.font.Font('Snake Game/assets/PoetsenOne-Regular.ttf', 25)

main_game = MAIN()

SCREEN_UPDATE = pg.USEREVENT  # making a user event
pg.time.set_timer(SCREEN_UPDATE, 150)  # setting timer of 150 ms

while True:  # game loop
    for event in pg.event.get():  # event loop which tells what action user does
        if event.type == pg.QUIT:  # cross button pressed then close window
            pg.quit()
            sys.exit()  # makes sure game closes totally
        if event.type == SCREEN_UPDATE:  # after every 150 ms move snake
            main_game.update()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP or event.key == pg.K_w:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pg.K_DOWN or event.key == pg.K_s:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pg.K_LEFT or event.key == pg.K_a:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pg.K_RIGHT or event.key == pg.K_d:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)

    screen.fill((175, 215, 70))  # sets screen background color to green
    main_game.draw_element()  # calling the draw function from main_game
    pg.display.update()  # updates the screen after every cycle
    clock.tick(60)  # setting fps here it is 60 fps
