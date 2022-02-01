#     ____    __       ____       ___     ___    _     ____
#    /  __|  |  |     / __ \     /  _|   /  _|  | |   /  __|
#   |  /     |  |    / /  \ \   |  |    |  |    | |  |  /
#   |  \__   |  |_   | |  | |   _\  \   _\  \   | |  |  \__
#    \____|  |____|  |_|  |_|  |____/  |____/   |_|   \____|
#    ____     ___     _   _     ____
#   |    \   /   \   | \ | |   / ___|
#   |  __/  |     |  |  \| |  | /  _
#   | |     |     |  | |\| |  | \_| |
#   |_|      \___/   |_| \_|   \____|
#     ____     ____     _    _    ____
#    / ___|   / __ \   | \  / |  | ___|
#   | /  _   / /  \ \  | |\/| |  | |__
#   | \_| |  | |  | |  | |  | |  | |__
#    \____|  |_|  |_|  |_|  |_|  |____|
#
#  PROJECT NAME - CLASSIC PONG GAME 
#  MADE BY - SUSHANT GOLA
#  CLASS - XII-A
#  ROLL NUMBER - 40

# https://www.webucator.com/article/python-color-constants-module/ colour module website


# IMPORTING MODULES
try:import pygame
except:import os;os.system('cmd.exe /c pip install pygame');import pygame
import pickle
import random
from pygame import mixer
import sqlite3
import time
import sys

# INITIALISING PYGAME MODULE BECAUSE ITS A CINVINIENT WAY TO GET EVERYTHING STARTED
pygame.init()

# CREATING THE SCREENA AND SETTING WINDOW NAME AND ICON
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("PONG")
icon = pygame.image.load('Images\Pong icon.png')
pygame.display.set_icon(icon)

# CONNECTING TO MYSQL DATABASE
mydb = sqlite3.connect('Database.db')
mycursor = mydb.cursor()
try:mycursor.execute("CREATE TABLE classic_pong_game (Name VARCHAR(20), Password VARCHAR(15), High_score int(11), High_score_free int(11))")
except:pass

# COLOURS
light_green = (127, 220, 0)
off_white = (235, 235, 235)
light_pink = (255, 240, 245)
light_cyan = (224, 255, 255)
light_sand = (255, 239, 213)
light_peach = (255, 255, 224)
med_sand = (205, 205, 180)
med_peach = (238, 203, 173)
med_pink = (255, 201, 207)
med_cyan = (171, 248, 248)
dark_cyan = (30, 169, 169)
dark_peach = (185, 172, 156)
dark_pink = (200, 149, 158)
dark_sand = (139, 126, 102)
light_red = (255, 48, 48)

light_slategray = (198, 226, 255)
med_slategray = (151, 208, 228)
dark_slategray = (159, 182, 205)
light_mint = (199, 252, 221)
med_mint = (152, 251, 152)
dark_mint = (124, 205, 124)

key_color = (200, 0, 0)
white = (255, 255, 255)
grey = (70, 70, 70)
black = (0, 0, 0)

# SETTING THE FPS
clock = pygame.time.Clock() ; angle_x = 0

# CREATING THE MOUSE FUNCTION WHICH GETS THE MOUSE FUNCTON
def mouse_over(x, y, w, h, pos):
    if pos[0] >= x and pos[0] <= x + w:
        if pos[1] >= y and pos[1] <= y + h:
            return x, y, True

# CREATING THE FUNCTION TO SHOW THE TEXT ON THE SCREEN
def show_txt(text, r, g, b, size, x, y):
    global width
    score_font = pygame.font.Font("comicsansms.ttf", size)
    score_render = score_font.render(text, True, (r, g, b))
    screen.blit(score_render, (x, y))
    width = score_render.get_width()
    return width

# CREATING CLASS WHICH RESUMES OR PAUSES THE GAME
class Res:

    def __init__(self, resume):
        self.resume = resume

    def get_res(self):
        return self.resume # RETURNS THE VALUE OF RESUME VARIABLE

    def update(self, val):
        self.resume = val # UPDATES THE VALUE OF TRESUME FUNTION

game_obj = Res(False) # CREATING THE OBJECT OF Res CLASS

class Var:

    # DEFAULT VARIABLES\

    dafault_bg_color = (0, 154, 205)
    default_tile_color = (255, 255, 255)
    default_ball_color = (255, 255, 255)

    color_ball = white
    color_tile = white
    color_bg = pygame.Color('darkturquoise')
    image_name = None

    none_selected_bg = True
    none_selected_tile = True
    none_selected_ball = True

    image_clicked = None
    ball_hollow = False
    tile_hollow = True

    selecting_tile_hs = False
    selecting_ball_hs = False

    color_bg_selected = False
    selecting_bg_color = False
    selecting_bg_img = False
    color_ball_selected = False
    color_tile_clicked = None
    color_tile_selected = False
    color_ball_clicked = None
    color_selected = False

    img_sel_cor = None
    cor = None
    cor_tile = None
    cor_ball = None

    signed_in = False
    username = None

    run = True
    run_ai = True
    run_mul = True
    run_i_s = True
    run_menu_play_1 = True
    run_mul_name = True


    def return_var(): # PROCESSING THE VALUE OF VARIABLES AND RETURNING THEM AS A LIST

        if Var.selecting_bg_img == True and Var.image_clicked == True:
            Var.none_selected_bg = False
            Var.color_bg_selected = False

        elif Var.selecting_bg_color == True and Var.color_selected == True:
            Var.none_selected_bg = False
            Var.color_bg_selected = True
            Var.selecting_bg_img = False
            Var.image_clicked = False

        else:
            Var.none_selected_bg = True

        if Var.color_tile_clicked == True and Var.color_tile_selected == True:
            Var.none_selected_tile = False
        else:
            Var.none_selected_tile = True

        if Var.color_ball_selected == True and Var.color_ball_clicked == True:
            Var.none_selected_ball = False
        else:
            Var.none_selected_ball = True

        lst = [Var.dafault_bg_color, Var.default_tile_color, Var.default_ball_color, Var.color_ball, Var.color_tile,
               Var.color_bg, Var.image_name, Var.none_selected_bg, Var.none_selected_tile, Var.none_selected_ball,
               Var.selecting_bg_img, Var.color_bg_selected, Var.image_clicked, Var.tile_hollow, Var.selecting_tile_hs,
               Var.ball_hollow, Var.selecting_ball_hs]

        return lst

var_obj = Var # CREATING THE OBJECT OF Var CLASS

# THIS CLASS CONTAINS THE TEXT VALUE AND ITS OTHER ATTRIBUTES
class Text:
    text = ""
    show_pass = False
    width = 0
    cursor_present = False

# THIS CLASS CREATES THE BUTTON
class Button__:
    
    def __init__(self,x,y,w,h,light,med,dark,pos,click,text,text_size,curvature = 15): # CONSTRUCTOR
        self.x = x;self.y = y;self.w = w;self.h = h ; self.curvature = curvature
        self.click = click;self.light = light;self.med = med;self.dark = dark;self.pos = pos
        self.text = text;self.text_size = text_size
    
    def button_blit(self,quit_conf = False):
        # CHANGING THE COLOR OF THE BUTTON WHEN CLICKED OR HOWERING AND RETURNING THE COMMAND
        if mouse_over(self.x,self.y,self.w,self.h,self.pos) and quit_conf == False:
            if self.click == False:button_color = self.med ; command = False 
            else:button_color = self.dark ; command = True
        else:button_color = self.light ; command = False

        pygame.draw.rect(screen,button_color,(self.x,self.y,self.w,self.h),0,self.curvature) # DRAWING THE BUTTON
        
        score_font = pygame.font.Font("comicsansms.ttf", self.text_size) ; score_render = score_font.render(self.text, True, (20, 20, 20)) # LOADING AND RENDERING THE TEXT
        width = score_render.get_width() ; height = score_render.get_height() ; text_x = (self.x)+(self.w/2)-(width/2) ; text_y = (self.y)+(self.h/2)-(height/2) # SETTING THE CORDINATES OF THE TEXT
        screen.blit(score_render, (text_x, text_y)) # WRITING THE TEXT ON THE SCREEN
        return command

# CREATING FUNCTION TO RENDER THE IMAGE ON THE SCREEN
def bg_img(name, x, y):
    load = pygame.image.load(name).convert()
    screen.blit(load, (x, y))

# CREATING FUNCTION TO RENDER THE IMAGE ON THE SCREEN
def show_png_img(name, x, y):
    load = pygame.image.load(name).convert_alpha()
    screen.blit(load, (x, y))

# CREATING THE FUNCTION TO ROTATE THE MUSIC ICON AT THE BOTTOM
def icon_rot(angle_x):
    # LOADING AND ROTATING THE MUSIC ICON
    img = pygame.transform.rotate(pygame.image.load('Images\Music_icon.png').convert_alpha(), angle_x)
    # CENTER CORDINATES OF THE ICON --> (950,750)
    screen.blit(img, (950 - int(img.get_width() / 2),
                750 - int(img.get_height() / 2)))

# CREATING FUNCTION TO GET THE NAMES OF 2 PLAYERS WHEN MULTIPLAYER MODE IS BEING PLAYED
def mul_name(speed):
    global disk_rot
    global click_muted

    # VARIABLES
    angle_x = 0
    music_rotating_check = 1

    var_obj.run_mul_name = True 
    run_mul_name = True
    
    p1_empty, p2_empty = False, False
    click = False
    cursor_placement= None

    mulp1_obj = Text()
    mulp2_obj = Text()

    cursor_cordinates = {mulp1_obj : [365, 505], mulp2_obj : [365, 605]} # THIS DICT CONTAINS THE CORDINATES OF THE INPUT BOX

    while run_mul_name:

        # LOADING IMAGES
        bg_img('Images\stars.png', 0, 0)
        show_png_img('Images\Back button.png', 30, 720)

        mouse = pygame.mouse.get_pos()  # GETTING THE MOUSE CORDINATES
        # pygame.draw.rect(screen, c_ok, (700, 700, 110, 55))  # DRAWING THE OK BUTTON

        ok_command  = Button__(700, 700, 110, 55,light_pink,med_pink,dark_pink,mouse,click,'Next',40).button_blit()

        if ok_command == True:
            if len(mulp1_obj.text) != 0: # CHECKING IF THE NAME IS VALID OR NOT 
                if len(mulp2_obj.text) == 0:p1_empty = False; p2_empty = True
                else:p1_empty = False ; p2_empty = False ; multiplayer(speed, mulp1_obj.text, mulp2_obj.text)
            else:p1_empty = True ; p2_empty = False

        # CALLING show_text() TO DISPLAY THE TEXT ON WINDOW
        show_txt('Controls', 255, 255, 255, 50, 401, 55)
        show_txt('Player 1', 255, 255, 255, 40, 178, 150)
        show_txt('Player 2', 255, 255, 255, 40, 678, 150)
        show_txt('NOTE:- First person to reach 100 points will win the game.',
                 255, 64, 64, 30, 70, 430)

        # P-1 DRAWING KEYS AND LINES
        pygame.draw.rect(screen, key_color, (200, 240, 60, 60))
        show_txt('W', 255, 255, 255, 30, 210, 240)
        pygame.draw.rect(screen, white, (200, 240, 60, 60), 3)

        pygame.draw.rect(screen, key_color, (220, 310, 60, 60))
        show_txt('S', 255, 255, 255, 30, 230, 310)
        pygame.draw.rect(screen, white, (220, 310, 60, 60), 3)

        pygame.draw.rect(screen, grey, (150, 310, 60, 60))
        show_txt('A', 255, 255, 255, 30, 160, 310)
        pygame.draw.rect(screen, white, (150, 310, 60, 60), 3)

        pygame.draw.rect(screen, grey, (290, 310, 60, 60))
        show_txt('D', 255, 255, 255, 30, 300, 310)
        pygame.draw.rect(screen, white, (290, 310, 60, 60), 3)

        pygame.draw.line(screen, white, (245, 260), (345, 260), 3)
        show_txt('Move tile up', 255, 255, 255, 20, 355, 243)

        pygame.draw.line(screen, white, (265, 355), (265, 400), 3)
        pygame.draw.line(screen, white, (265, 400), (325, 400), 3)
        show_txt('Move tile down', 255, 255, 255, 20, 335, 383)

        # P-2 DRAWING KEYS AND LINES
        pygame.draw.rect(screen, key_color, (720, 240, 60, 60))
        pygame.draw.rect(screen, white, (720, 240, 60, 60), 3)
        pygame.draw.line(screen, white, (740, 260), (740, 280), 3)
        pygame.draw.polygon(
            screen, white, ((740, 255), (735, 265), (745, 265)))

        pygame.draw.rect(screen, key_color, (720, 310, 60, 60))
        pygame.draw.rect(screen, white, (720, 310, 60, 60), 3)
        pygame.draw.line(screen, white, (740, 325), (740, 340), 3)
        pygame.draw.polygon(
            screen, white, ((740, 350), (735, 340), (745, 340)))

        pygame.draw.rect(screen, grey, (650, 310, 60, 60))
        pygame.draw.rect(screen, white, (650, 310, 60, 60), 3)
        pygame.draw.line(screen, white, (675, 340), (690, 340), 3)
        pygame.draw.polygon(
            screen, white, ((665, 340), (675, 335), (675, 345)))

        pygame.draw.rect(screen, grey, (790, 310, 60, 60))
        pygame.draw.rect(screen, white, (790, 310, 60, 60), 3)
        pygame.draw.line(screen, white, (805, 340), (820, 340), 3)
        pygame.draw.polygon(
            screen, white, ((830, 340), (820, 335), (820, 345)))

        pygame.draw.line(screen, white, (765, 260), (835, 260), 3)
        pygame.draw.line(screen, white, (765, 355), (765, 400), 3)
        pygame.draw.line(screen, white, (765, 400), (815, 400), 3)

        show_txt('Move tile up', 255, 255, 255, 20, 845, 243)
        show_txt('Move tile down', 255, 255, 255, 20, 825, 383)

        # P1 BOX AND TEXT
        mulp1_obj.width = show_txt(mulp1_obj.text, 255, 255, 255, 30, 367.5, 510)
        pygame.draw.rect(screen, (255, 255, 255),
                         (360, 505, mulp1_obj.width + 42, 55), 2)

        # P2 BOX AND TEXT
        mulp2_obj.width = show_txt(mulp2_obj.text, 255, 255, 255, 30, 367.5, 610)
        pygame.draw.rect(screen, (255, 255, 255),
                         (360, 605, mulp2_obj.width + 42, 55), 2)

        show_txt('Player 1 name : ', 255, 255, 255, 40, 70, 500)
        show_txt('Player 2 name: ', 255, 255, 255, 40, 70, 600)

        # DISPLAYING THE MESSAGE IF THE INPUT IS EMPTY
        if p1_empty == True:
            show_txt('Enter player 1 name.', 200, 50, 50, 40, 200, 690)
        elif p2_empty == True:
            show_txt('Enter player 2 name.', 200, 50, 50, 40, 200, 690)

        for key,value in cursor_cordinates.items(): # DRAWING THE CURSOR AT THE END OF THE TEXT
            if key == cursor_placement:
                show_txt('_',255,255,255,30,value[0]+cursor_placement.width+5,value[1])


        # EVENT LOOP
        for event in pygame.event.get():
            if event.type == pygame.QUIT:sys.exit()

            # WHEN THE MOUSEBUTON IS PRESSED
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # PRESSING THE OK BUTTON
                if mouse_over(700, 700, 110, 55, mouse):click = True

                elif mouse_over(925, 725, 50, 50, mouse):  # MUTING/UNMUTING THE MUSIC
                    click = True
                    # IF ROTATOIN IS STOPPED, music_rotation_check WILL HAVE EVEN VALUE ELSE,IT WILL HAVE ODD VALUE
                    music_rotating_check += 1
                    if music_rotating_check % 2 == 0:  # ROTATION STOPPED
                        pygame.mixer.music.pause()
                        disk_rot = False
                    elif music_rotating_check % 2 != 0:  # ROTATION STARTED
                        mixer.music.unpause()
                        disk_rot = True

                elif mouse_over(30, 720, 50, 50, mouse):  # CLIKCING THE BACK BUTTON
                    click = True
                    run_mul_name = False
                    var_obj.run_mul_name = False

                # SELECTING THE 1ST PLAYER INPUT BOX
                if mouse_over(365.5, 505, mulp1_obj.width + 25, 55, mouse):
                    cursor_placement = mulp1_obj # CHANGING THE VALUE OF CURSOR_PLACEMENT
                    cursor_placement.cursor_present = True

                # SELECTING THE 2ND PLAYER INPUT BOX
                elif mouse_over(367.5, 605,mulp2_obj.width + 25, 55, mouse):
                    cursor_placement = mulp2_obj # CHANGING THE VALUE OF CURSOR_PLACEMENT
                    cursor_placement.cursor_present = True

                else:
                    mulp1_obj.cursor_present, mulp2_obj.cursor_present = False, False
                    cursor_placement = None

                if click == True and click_muted == False:
                    click_sound = mixer.Sound('Music\Click.wav')
                    click_sound.play()

            elif event.type == pygame.MOUSEBUTTONUP:  # MOUSEBUTTON RELEASED
                click = False

            if event.type == pygame.KEYDOWN:  # CHECKING IF ANY KEY IS PRESSED
                if event.key == pygame.K_BACKSPACE:
                    try:
                        if cursor_placement.cursor_present == True:  # BACKSPACE IS PRESSED
                            cursor_placement.text = cursor_placement.text[:-1] 
                    except:pass
                else: # ADDING TEXT TO THE NAME
                    try:
                        if len(cursor_placement.text) < 15 and cursor_placement.cursor_present: cursor_placement.text+=event.unicode # SETTING THE LIMIT FOR NUMBER OF WORDS
                    except:pass

        if disk_rot == False: # MUSIC MUTED
            show_png_img('Images\Music_icon.png', 925, 725)
            pygame.draw.line(screen, light_red, (925, 725), (975, 775), 5)
        elif disk_rot == True: # MUSIC RESUMED
            angle_x -= 2
            icon_rot(angle_x)

        run_mul_name = var_obj.run_mul_name

        pygame.display.update()  # UPDATING THE SCREEN

    return mulp1_obj.text, mulp2_obj.text

# CREATING FUNCTION WHICH DECLARES THE WINNER
def win_lose_screen(l1, l2, p1_name = None, p2_name = None):
    global disk_rot
    
    mixer.music.load('Music\Menu music.mp3')
    mixer.music.play(-1)
    if disk_rot == False:mixer.music.pause()

    click = False
    run_w_l = True
    quit_confirmation = False
    txt_x = 300
    music_rotating_check = 1
    angle_x = 0
    start = time.time()

    while run_w_l == True:

        load = pygame.image.load('Images\stars.png').convert()  # RENDERING BG IMAGE
        screen.blit(load, (0, 0))
        stop = time.time()
        mouse = pygame.mouse.get_pos() # GETTING MOUSE CORDINATES

        p_a_command = Button__(300, 300, 400, 60,light_pink,med_pink,dark_pink,mouse,click,'PLAY AGAIN',50).button_blit(quit_confirmation)
        settings_command = Button__(300, 400, 400, 60,light_cyan,med_cyan,dark_cyan,mouse,click,'SETTINGS',50).button_blit(quit_confirmation)
        main_menu_command = Button__(300, 500, 400, 60,light_mint,med_mint,dark_mint,mouse,click,'MAIN MENU',50).button_blit(quit_confirmation)
        quit_command = Button__(300, 600, 400, 60,light_peach,med_peach,dark_peach,mouse,click,'QUIT', 50).button_blit(quit_confirmation)

        if quit_confirmation == False and stop-start>2 and click == True:
            if p_a_command == True:run_w_l = False ; var_obj.run_menu_play_1 = True ; var_obj.run_mul_name = False ; var_obj.run_ai = False ; var_obj.run_mul = False 
            elif settings_command == True:settings()
            elif quit_command == True:quit_confirmation = True
            elif main_menu_command == True:run_w_l = False ; var_obj.run_ai = False ; var_obj.run_mul = False ; var_obj.run_i_s = False ; var_obj.run_menu_play_1 = False ; var_obj.run_mul_name = False
            click = False;start = stop

        # EVENT LOOP
        for event in pygame.event.get():
            if event.type == pygame.QUIT:sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if quit_confirmation == False: # IF QUIT CLICKED IS FALSE THEN RUN THIS
                    if mouse_over(300, 300, 400, 60,mouse) or mouse_over(300, 400, 400, 60,mouse) or  mouse_over(300, 500, 400, 60,mouse) or mouse_over(300, 600, 400, 60,mouse):click = True
                    
                elif quit_confirmation == True:
                    if mouse_over(370, 410, 100, 50, mouse) or mouse_over(520, 410, 100, 50, mouse):
                        click = True

                if mouse_over(925, 725, 50, 50, mouse):
                    click = True
                    music_rotating_check += 1
                    if music_rotating_check % 2 == 0:
                        # rotation stopped
                        pygame.mixer.music.pause()
                        disk_rot = False
                    elif music_rotating_check % 2 != 0:
                        mixer.music.unpause()
                        disk_rot = True

                if click == True and click_muted == False: # PLAYING CLICK SOUND IF click_muted = False
                    mixer.Sound('Music\Click.wav').play() 

            elif event.type == pygame.MOUSEBUTTONUP:
                click = False

        if quit_confirmation == True: # CONFIRMING IF THE PLAYER WANT TO QUIT THE GAME
            mouse = pygame.mouse.get_pos()
            pygame.draw.rect(screen, (50, 50, 50), (300, 300, 400, 200))
            pygame.draw.rect(screen, (255, 255, 255), (300, 300, 400, 200), 5)
            show_txt('Do you want to quit?', 230, 230, 230, 37, 330, 320)
            quit_yes = Button__(370,410,100,50,light_pink,med_pink,dark_pink,mouse,click,'YES',40).button_blit()
            quit_no = Button__(520,410,100,50,light_cyan,med_cyan,dark_cyan,mouse,click,'NO',40).button_blit()
            if quit_yes == True:sys.exit()
            elif quit_no == True:quit_confirmation = False
            click = False

        if a_i == True: # DECLARING THE WINNER
            if l1 < l2:
                show_txt('Congratulations', 255,255,255,80,210.5,40)
                show_txt('You won!!',255,255,255,70,352.5,150)
            else:
                show_txt('You lose!!',255,255,255,70,349.5,50)
                show_txt('Try again...',255,255,255,60,348.5,150)

        elif hum == True: # DECLARING THE WINNER
            show_txt('Congratulations', 255,255,255,80,210.5,40)
            if l1 < l2:
                txt_w = show_txt(p2_name+' won!!',255,255,255,60,txt_x,150)
                txt_x = 500-(txt_w/2)
            else:
                txt_w = show_txt(p1_name+' won!!',255,255,255,60,txt_x,150)
                txt_x = 500-(txt_w/2)


        if disk_rot == False: # ROTATION STOPPED
            show_png_img('Images\Music_icon.png', 925, 725)
            pygame.draw.line(screen, light_red, (925, 725), (975, 775), 5)
        elif disk_rot == True: # ROTATION CONTINUED
            angle_x -= 2
            icon_rot(angle_x)

        pygame.display.update()

# CREATING THE PAUSE SCREEN
def pause(username):
    global run_ai, run_mul, run, run_pause
    global high_score_ai_free
    global p_s
    global free_ai
    global disk_rot

    # VARIABLES
    run_pause = True
    click = False
    quit_confirmation = False
    angle_x = 0
    music_rotating_check = 1
    start = time.time()

    while run_pause:

        bg_img('Images\stars.png', 0, 0)  # BG IMAGE
        show_txt('GAME PAUSED', 255, 255, 255, 100, 150, 100)
        stop = time.time()

        mouse = pygame.mouse.get_pos()  # GETTING MOUSE CORDINATES

        # DRAWING BUTTONS ON SCREEN
        resume_command = Button__(300, 300, 400, 60,light_pink,med_pink,dark_pink,mouse,click,'RESUME',50).button_blit(quit_confirmation)
        settings_command = Button__(300, 400, 400, 60,light_cyan,med_cyan,dark_cyan,mouse,click,'SETTINGS',50).button_blit(quit_confirmation)
        main_menu_command = Button__(300, 500, 400, 60,light_mint,med_mint,dark_mint,mouse,click,'MAIN MENU',50).button_blit(quit_confirmation)
        quit_command = Button__(300, 600, 400, 60,light_peach,med_peach,dark_peach,mouse,click,'QUIT', 50).button_blit(quit_confirmation)

        if quit_confirmation == False and stop-start>1 and click == True:
            if resume_command == True:game_obj.update(True);run_pause = False
            elif settings_command == True:settings()
            elif quit_command == True:quit_confirmation = True
            elif main_menu_command == True:
                try:
                    if free_ai == True:  # UPDATING THE HIGH SCORE FOR FREEPLAY_AI
                        if p_s > high_score_ai_free:
                            high_score_ai_free = p_s
                            query = """update classic_pong_game set High_score_free = ? where Name = ?"""
                            value = (high_score_ai_free,username)
                            mycursor.execute(query,value);mydb.commit()
                except:pass
                run_pause = False;var_obj.run_ai = False;var_obj.run_mul = False;var_obj.run_i_s = False;var_obj.run_menu_play_1 = False;var_obj.run_mul_name = False
                mixer.music.load("Music\Menu music.mp3") ; mixer.music.play(-1) ; click = True
                if disk_rot == False:mixer.music.pause()
            click = False;start = stop
        
        # EVENT LOOP
        for event in pygame.event.get():
            if event.type == pygame.QUIT:sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_over(925, 725, 50, 50, mouse):
                    click = True
                    music_rotating_check += 1
                    if music_rotating_check % 2 == 0:
                        # rotation stopped
                        pygame.mixer.music.pause()
                        disk_rot = False
                    elif music_rotating_check % 2 != 0:
                        mixer.music.unpause()
                        disk_rot = True
                if quit_confirmation == False:
                    if mouse_over(300, 300, 400, 60, mouse) or mouse_over(300, 400, 400, 60, mouse) or mouse_over(300, 600, 400, 60, mouse) or mouse_over(300, 500, 400, 60, mouse):
                        click = True

                elif quit_confirmation == True:
                    if mouse_over(370, 410, 100, 50, mouse) or mouse_over(520, 410, 100, 50, mouse):
                        click = True

                if click_muted == False and click == True:  # PLAYING CLICK SOUND IF ITS ENABLED
                    click_sound = mixer.Sound('Music\Click.wav')
                    click_sound.play()

            if event.type == pygame.MOUSEBUTTONUP:
                click = False

        if quit_confirmation == True: # CONFIRMING IF THE PLAYER WANT TO QUIT THE GAME
            mouse = pygame.mouse.get_pos()
            pygame.draw.rect(screen, (50, 50, 50), (300, 300, 400, 200))
            pygame.draw.rect(screen, (255, 255, 255), (300, 300, 400, 200), 5)
            show_txt('Do you want to quit?', 230, 230, 230, 37, 330, 320)
            quit_yes = Button__(370,410,100,50,light_pink,med_pink,dark_pink,mouse,click,'YES',40).button_blit()
            quit_no = Button__(520,410,100,50,light_cyan,med_cyan,dark_cyan,mouse,click,'NO',40).button_blit()
            if quit_yes == True:
                click = True
                try:
                    if free_ai == True:  # UPDATING THE HIGH SCORE FOR FREEPLAY_AI
                        if p_s > high_score_ai_free:
                            high_score_ai_free = p_s
                            query = """update classic_pong_game set High_score_free =? where Name = ?"""
                            value = (high_score_ai_free,username)
                            mycursor.execute(query,value);mydb.commit()
                except:pass
                sys.exit()
            elif quit_no == True:quit_confirmation = False;click = True
            click = False


        if disk_rot == False: # rotation stopped
            show_png_img('Images\Music_icon.png', 925, 725)
            pygame.draw.line(screen, light_red, (925, 725), (975, 775), 5)
        elif disk_rot == True: # ROATION CONTINUED
            angle_x -= 2
            icon_rot(angle_x)

        pygame.display.update()

# CREATING FUNCTION TO CHOOSE THE LEVEL
def menu_play_1(user_name):

    # GLOBAL VAIRABLES
    global click_muted
    global speed_level
    global a_i, hum, free_ai, free_hum
    global disk_rot

    # VARIABLES
    vs_x = 350
    speed_level = None
    run_menu_play_1 = True
    var_obj.run_menu_play_1 = True
    comp_reached, comp_starting, comp_back = False, False, False
    music_rotating_check = 1
    a_i, hum, free_ai, free_hum = False, False, False, False
    angle_x = 0 ; click_s = False ; user_width = 200
    
    user_name = var_obj.username # GETTING USERNAME OF THE PLAYER

    while run_menu_play_1:

        bg_img('Images\stars.png', 0, 0) # BG IMAGE
        show_txt('Select your mode :-', 240, 240, 240, 70, 200, 130)
        show_png_img('Images\Back button.png', 30, 720) # RENDERING BACK BUTTON

        mouse = pygame.mouse.get_pos() # GETTING MOUSE CORDINATES

        # SHOWING USERNAME OF THE PLAYER
        pygame.draw.rect(screen, (100, 100, 100), (0, 0, 195+(user_width), 75))
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, 195+(user_width), 75), 5)
        show_txt('Username - ', 255, 255, 255, 30, 15, 15)
        user_width = show_txt(user_name, 255, 255, 255, 30, 180, 15)

        # DRAWING THE BUTTONS
        free_hum_command = Button__(vs_x, 600, 300, 50,light_peach,med_peach,dark_peach,mouse,click_s,'Freeplay Human',40,15).button_blit()
        free_ai_command = Button__(vs_x, 500, 300, 50,light_sand,med_sand,dark_sand,mouse,click_s,'Freeplay AI',40,15).button_blit()
        ai_command = Button__(vs_x, 300, 300, 50,light_mint,med_mint,dark_mint,mouse,click_s,'vs AI',40,15).button_blit()
        hum_command = Button__(vs_x, 400, 300, 50,light_slategray,med_slategray,dark_slategray,mouse,click_s,'vs Human',40,15).button_blit()

        if ai_command == True:a_i, hum, free_ai, free_hum = True, False, False, False ; comp_starting = True 
        elif hum_command == True : a_i, hum, free_ai, free_hum = False, True, False, False ; comp_starting = True 
        elif free_ai_command == True: a_i, hum, free_ai, free_hum = False, False, True, False ; comp_starting = True 
        elif free_hum_command == True: a_i, hum, free_ai, free_hum = False, False, False, True ; comp_starting = True 

        sign_out_command = Button__(650,700,200,50,light_pink,med_pink,dark_pink,mouse,click_s,'Sign out',40).button_blit()
        if sign_out_command == True: 
            with open('User.bin','wb') as user_file:user_file.close()
            var_obj.signed_in = False ; run_menu_play_1 = False ; var_obj.run_menu_play_1 = False ; click_s = False

        if comp_starting == True:
            if vs_x > 130:vs_x -= 10 # STARTING THE TRANSITION

            elif vs_x < 140: # IF TRANSITION ENDED , DRAWING THE LEVEL CHOOSER

                pygame.draw.rect(screen, (100, 100, 100), (540, 300, 340, 380))
                pygame.draw.rect(screen, (230, 230, 230),(540, 300, 340, 380), 5)

                easy_command = Button__(610, 400, 200, 50 , light_peach,med_peach,dark_peach,mouse,click_s,'Easy',40).button_blit()
                med_command = Button__(610, 500, 200, 50 , light_pink,med_pink,dark_pink,mouse,click_s,'Medium',40).button_blit()
                hard_command = Button__(610, 600, 200, 50 , light_sand,med_sand,dark_sand,mouse,click_s,'Hard',40).button_blit()
                if click_s == True:
                    if easy_command == True: speed_level = 8
                    elif med_command == True: speed_level = 10
                    elif hard_command == True: speed_level = 12
                    if easy_command == True or med_command == True or hard_command == True:
                        if a_i == True:ai(speed_level, user_name)
                        elif hum == True:mul_name(speed_level)
                        elif free_ai == True:ai(speed_level, user_name)
                        elif free_hum == True:mul_name(speed_level)
                    click_s = False
                comp_reached = True

                # SELECTING THE FUNCTION
                if a_i == True:show_txt('Vs A.I.', 230, 230, 230, 40, 650, 320)
                elif hum == True:show_txt('Vs Human', 230, 230, 230, 40, 620, 320)
                elif free_ai == True:show_txt('Freeplay (A.I.)', 230, 230, 230, 40, 575, 320)
                elif free_hum == True:show_txt('Freeplay (Human)', 230, 230, 230, 40, 545, 320)

        # EVENT LOOP
        for event in pygame.event.get():
            if event.type == pygame.QUIT:sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if mouse_over(30, 725, 50, 50, mouse): # PRESSING BACK BUTTON
                    click_s = True ; click = True
                    # IF TRANSITION HAS TAKEN PLACE THEN REVERSING THE TRANSITION ELSE TERMINTATIN TH FUCNTION
                    if comp_reached == False: run_menu_play_1 = False ; var_obj.run_menu_play_1 = False ; var_obj.run_i_s = False
                    else:comp_starting = False ; comp_back = True

                if mouse_over(925, 725, 50, 50, mouse): # PAUSING / PLAYING THE MUSIC
                    click_s = True ; music_rotating_check += 1
                    if music_rotating_check % 2 == 0: pygame.mixer.music.pause() ; disk_rot = False
                    elif music_rotating_check % 2 != 0: mixer.music.unpause() ; disk_rot = True

                # PRESSING THE BUTTONS
                if mouse_over(vs_x, 300, 280, 50, mouse) or mouse_over(vs_x, 400, 280, 50, mouse) or  mouse_over(vs_x, 500, 280, 50, mouse) or  mouse_over(vs_x, 600, 280, 50, mouse) or mouse_over(650,700,200,50,mouse):click_s = True
                
                # CHOSING THE FUNCTIONA AND SETTING UP THE SPEED/LEVEL
                if comp_reached == True:
                    if mouse_over(610, 400, 200, 50, mouse) or mouse_over(610, 500, 200, 50, mouse) or mouse_over(610, 600, 200, 50, mouse):
                        click_s = True
                        
                if click_s == True and click_muted == False: # PLAYING THE CLICK SOUND
                    click_sound = mixer.Sound('Music\Click.wav') ; click_sound.play()

            if event.type == pygame.MOUSEBUTTONUP: click_s = False

        if comp_back == True: # TRANSITION
            if vs_x < 350:vs_x += 10
            if vs_x >= 340:comp_back = False ; comp_reached = False

        if disk_rot == False: # MUSIC PAUSED
            show_png_img('Images\Music_icon.png', 925, 725) ; pygame.draw.line(screen, light_red, (925, 725), (975, 775), 5)
        elif disk_rot == True: # MUSIC RESUME
            angle_x -= 2 ; icon_rot(angle_x)

        run_menu_play_1 = var_obj.run_menu_play_1 
        pygame.display.update() # UPDATING THE SCREEN

# CREATING FUNCTION TO SIGN IN OR LOGIN
def input_screen():

    global disk_rot
    global click_muted

    # VARIABLES
    music_rotating_check = 1
    login, signup = True, False    
    OK_clicked,pass_cp_not_match,OK_clicked_once = False, False, False
    inv_name, inv_pass = False, False
    name_exi = False
    angle_x = 0
    click = False
    cursor_placement = None
    show_pass_sign = False
    show_pass_login = False
    start = time.time()

    # MAKING OBJECTS FOR DIFFERENT TEXT FIELDS
    signin_name = Text()
    signin_pass = Text()
    signin_conf_pass = Text()
    loginn_name = Text()
    login_pass = Text()

    # THIS DICT CONTAINS THE CORDINATES OF THE CURSOR WHICH IS TO BE PLACED AT THE END OF EACH FIELD
    cursor_cordinates = {signin_name:[378, 374],signin_pass:[363,474],signin_conf_pass:[563,574],
                         loginn_name:[378,374],login_pass:[363,474]}

    if var_obj.signed_in == False:
        run_i_s = True
        var_obj.run_i_s = True
    else:run_i_s = False;var_obj.run_i_s = False

    while run_i_s:

        bg_img('Images\stars.png', 0, 0) # BG IMAGE

        mouse = pygame.mouse.get_pos()
        stop = time.time()
        show_png_img('Images\Back button.png', 30, 725) # BACK BUTTON

        if var_obj.signed_in == False:
            run_i_s = True
            var_obj.run_i_s = True
        else:run_i_s = False;var_obj.run_i_s = False

        mycursor.execute('select * from classic_pong_game') # GETTING DATA FROM DATABASE
        exist = mycursor.fetchall() 

        if OK_clicked == True:
            name_exi = False
            if signup == True: 

                # IF EACH COLUMN IS PROPERLY FILLED AND PASSWORD & CONFIRM PASSWOD MATCHES, THEN ADDING DATA INTO THE DATABASE

                if len(signin_name.text) != 0 and len(signin_pass.text) != 0 and len(signin_conf_pass.text) != 0:
                    if signin_pass.text == signin_conf_pass.text:
                        for data in exist:
                            if data[0] == signin_name.text:
                                name_exi = True
                                OK_clicked = False
                                break
                        if name_exi == False:
                            command = "insert into classic_pong_game(Name,Password,High_score,High_score_free) values('"+str(signin_name.text)+"','"+str(signin_pass.text)+"',0,0)"
                            mycursor.execute(command)
                            mydb.commit()
                            var_obj.username = signin_name.text
                            var_obj.signed_in = True 
                            with open('User.bin','wb') as user_file:pickle.dump([signin_name.text],user_file);user_file.close()
                            menu_play_1(signin_name.text)
                    else:pass_cp_not_match = True

                OK_clicked = False
                OK_clicked_once = True

            elif login == True:

                # IF SIMILAR USERNAME IS PRESENT IN THE DATABASE AND ITS PASSWORD IS SAME AS THE ONE FILLED BY THE USER THEN LOGIN

                if len(loginn_name.text) > 0 and len(login_pass.text) > 0:
                    if len(exist) > 0:
                        for data in exist:
                            if str(data[0]) == loginn_name.text:
                                if str(data[1]) == login_pass.text:
                                    var_obj.signed_in = True
                                    with open('User.bin','wb') as user_file:pickle.dump((loginn_name.text),user_file);user_file.close()
                                    var_obj.username = loginn_name.text ; menu_play_1(loginn_name.text) ; break ; OK_clicked_once = False 
                                else:inv_pass = True;OK_clicked_once = True
                            else:inv_name = True ; OK_clicked_once = True
                    else: inv_name = True ; OK_clicked_once = True
            OK_clicked = False          
        
        if login == True:
            # DRAWING DIFFERENT INPUT BOXES AND SHOWING THE TEXT

            show_txt('Username : ', 255, 255, 255, 50, 100, 350)
            show_txt('Password : ', 255, 255, 255, 50, 100, 450)
            
            loginn_name.width = show_txt(loginn_name.text, 255, 255, 255, 40, 382.5, 363)
            pygame.draw.rect(screen, (255, 255, 255),
                             (375, 359, loginn_name.width + 38, 65), 2)
            login_pass.width = show_txt(login_pass.text if show_pass_login == True else len(login_pass.text)*'*', 255, 255, 255, 40, 367.5, 463)
            pygame.draw.rect(screen, (255, 255, 255),
                             (360, 459, login_pass.width + 38, 65), 2)

            show_png_img('Images\hide_icon.png' if show_pass_login == True else 'Images\show_pass.png', 430+login_pass.width,475 if show_pass_login == True else 469)

            if OK_clicked_once == True:
                if len(loginn_name.text) == 0: # CHACKING LENGTH OF NAME
                    show_txt('Enter your name', 255, 40, 40, 40, 350, 260)
                    OK_clicked = False

                elif len(login_pass.text) == 0: # CHECKING LENGTH OF PASSWORD
                    show_txt('Enter password', 255, 40, 40, 40, 355, 260)
                    OK_clicked = False
                if len(loginn_name.text) != 0 and len(login_pass.text)!=0:
                    if inv_name == True or inv_pass == True: # IF PASSWORD OR NAME IS INCORRECT WHEN LOGING IN, SHOW ERROR 
                        show_txt('Invalid username or password',
                                255, 40, 40, 40, 225, 260)
                    OK_clicked = False


        elif signup == True:

            # DRAWING VARIOUS INPUT BOXES AND SHOWING TEXT

            signin_name.width = show_txt(signin_name.text, 255, 255, 255, 40, 382.5, 363)
            pygame.draw.rect(screen, (255, 255, 255),
                             (375, 359, signin_name.width + 38, 65), 2)
            signin_pass.width = show_txt(signin_pass.text if show_pass_sign == True else len(signin_pass.text)*'*', 255, 255, 255, 40, 367.5, 463)
            pygame.draw.rect(screen, (255, 255, 255),
                             (360, 459, signin_pass.width + 38, 65), 2)
            signin_conf_pass.width = show_txt(signin_conf_pass.text if show_pass_sign == True else len(signin_conf_pass.text)*'*', 255, 255, 255, 40, 567.5, 563)
            pygame.draw.rect(screen, (255, 255, 255),
                             (560, 559, signin_conf_pass.width + 38, 65), 2)

            show_png_img('Images\hide_icon.png' if show_pass_sign == True else 'Images\show_pass.png', 430+signin_pass.width,475 if show_pass_sign == True else 469)

            show_txt('Username : ', 255, 255, 255, 50, 100, 350)
            show_txt('Password : ', 255, 255, 255, 50, 100, 450)
            show_txt('Confirm password : ', 255, 255, 255, 50, 100, 550)

            if OK_clicked_once == True: # SHOWING ERROR MESSAGE
                if len(signin_name.text) == 0: #
                    show_txt('Enter your name', 255, 40, 40, 40, 350, 260)
                    OK_clicked = False
                elif len(signin_pass.text) == 0:
                    show_txt('Enter password', 255, 40, 40, 40, 355, 260)
                    OK_clicked = False
                elif len(signin_conf_pass.text) == 0:
                    show_txt('Confirm your password', 255, 40, 40, 40, 280, 260)
                    OK_clicked = False
                elif pass_cp_not_match == True:
                    show_txt('Password and confirm password do not match',
                            255, 40, 40, 40, 90, 260)
                OK_clicked = False

                if name_exi == True: # CHECKING IF THE USERNAME ALREADY EXISTS
                    show_txt('This username already exists',
                            255, 40, 40, 40, 230, 260)

        # DRAWING BUTTONS
        login_command = Button__(200, 150, 200, 65,light_pink,med_pink,dark_pink,mouse,click,'LOGIN',41).button_blit()
        sign_up_command = Button__(600, 150, 200, 65,light_cyan,med_cyan,dark_cyan,mouse,click,'SIGN UP',41).button_blit()
        next_command = Button__(700, 700, 115, 55,light_peach,med_peach,dark_peach,mouse,click,'NEXT',32).button_blit()

        if login_command == True and stop-start>1:login = True;signup = False;OK_clicked_once = False ; start = stop
        elif sign_up_command == True and stop-start>1:signup = True;login = False;OK_clicked_once = False ; start = stop
        elif next_command == True and click == True and stop-start>1:
            OK_clicked_once = True ; start = stop
            if signup == True:OK_clicked, pass_cp_not_match = True, False
            if login == True:OK_clicked = True


        # PLACING THE CURSOR        
        for key,value in cursor_cordinates.items():
            if key == cursor_placement:show_txt('_',255,255,255,30,value[0]+cursor_placement.width+5,value[1])

        # EVENT LOOP
        for event in pygame.event.get():
            if event.type == pygame.QUIT:sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                cursor_placement = None

                if mouse_over(200, 150, 200, 65, mouse) or mouse_over(600, 150, 200, 65, mouse) or mouse_over(700, 700, 100, 65, mouse):click = True

                elif mouse_over(925, 725, 50, 50, mouse): # MUTING OR RESUMING MUSIC
                    click = True
                    music_rotating_check += 1
                    if music_rotating_check % 2 == 0: # ROTATION STOPPED
                        pygame.mixer.music.pause()
                        disk_rot = False
                    elif music_rotating_check % 2 != 0: # ROTATION CONTINUED
                        mixer.music.unpause()
                        disk_rot = True

                if mouse_over(30, 725, 50, 50, mouse):
                    click = True
                    run_i_s = False
                    var_obj.run_i_s = False

                if login == True:

                    # HIDING OR SHOWING PASSWORD
                    if mouse_over(420+login_pass.width,475,60,40,mouse) and show_pass_login == True:show_pass_login = False;click = True
                    elif mouse_over(420+login_pass.width,475,60,40,mouse) and show_pass_login == False:show_pass_login = True;click = True

                    # SELECTING THE FIELD
                    if mouse_over(375, 369, loginn_name.width+25, 65, mouse):
                        loginn_name.cursor_present = True
                        login_pass.cursor_present, signin_name.cursor_present, signin_pass.cursor_present, signin_conf_pass.cursor_present = False, False, False, False
                        cursor_placement = loginn_name
                    elif mouse_over(365, 469, login_pass.width+25, 65, mouse):
                        login_pass.cursor_present = True
                        loginn_name.cursor_present, signin_name.cursor_present, signin_pass.cursor_present, signin_conf_pass.cursor_present = False, False, False, False
                        cursor_placement = login_pass
                    else:
                        loginn_name.cursor_present, login_pass.cursor_present, signin_name.cursor_present, signin_pass.cursor_present, signin_conf_pass.cursor_present = False, False, False, False, False
                        cursor_placement = None
                elif signup == True:

                    # HIDING OR SHOWING PASSWORD
                    if mouse_over(410+signin_pass.width,455,50,40,mouse) and show_pass_sign == True:show_pass_sign = False;click = True
                    elif mouse_over(410+signin_pass.width,455,50,40,mouse) and show_pass_sign == False: show_pass_sign = True;click = True

                    # SELECTING THE FIELD
                    if mouse_over(375, 369, signin_name.width+25, 65, mouse):
                        signin_name.cursor_present = True
                        loginn_name.cursor_present, login_pass.cursor_present, signin_pass.cursor_present, signin_conf_pass.cursor_present = False, False, False, False
                        cursor_placement = signin_name
                    elif mouse_over(365, 469, signin_pass.width+25, 65, mouse):
                        signin_pass.cursor_present = True
                        loginn_name.cursor_present, login_pass.cursor_present, signin_name.cursor_present, signin_conf_pass.cursor_present = False, False, False, False
                        cursor_placement = signin_pass
                    elif mouse_over(565, 569, signin_conf_pass.width+25, 65, mouse):
                        signin_conf_pass.cursor_present = True
                        loginn_name.cursor_present, login_pass.cursor_present, signin_name.cursor_present, signin_pass.cursor_present = False, False, False, False
                        cursor_placement = signin_conf_pass
                    else:
                        loginn_name.cursor_present, login_pass.cursor_present, signin_name.cursor_present, signin_pass.cursor_present, signin_conf_pass.cursor_present = False, False, False, False, False
                        cursor_placement = None

                if click == True and click_muted == False: # PLAYING CLICK SSOUND
                    click_sound = mixer.Sound('Music\Click.wav')
                    click_sound.play()

            elif event.type == pygame.MOUSEBUTTONUP:
                click = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE: # PRESSING BACKSPACE
                    OK_clicked_once = False
                    try:
                        if cursor_placement.cursor_present == True:cursor_placement.text = cursor_placement.text[:-1]
                    except:pass
                else: # PRESSING ANY KEY
                    OK_clicked_once = False
                    try:
                        if cursor_placement == loginn_name or cursor_placement == signin_name:
                            if cursor_placement.cursor_present == True and len(cursor_placement.text)<20:
                                cursor_placement.text += event.unicode
                        elif cursor_placement == login_pass or cursor_placement == signin_pass or cursor_placement == signin_conf_pass:
                            if cursor_placement.cursor_present == True and len(cursor_placement.text)<15:
                                cursor_placement.text += event.unicode
                    except:pass

        if disk_rot == False:
            show_png_img('Images\Music_icon.png', 925, 725)
            pygame.draw.line(screen, light_red, (925, 725), (975, 775), 5)

        elif disk_rot == True:
            angle_x -= 2
            icon_rot(angle_x)

        run_i_s = var_obj.run_i_s

        pygame.display.update() # UPDATING THE SCREEN ON EVERY ITERATION

# CREATING FUNCTION TO GIVE INFO ABOUT THE GAME AND THE DEVELOPER
def about():
    global disk_rot
    global click_muted

    # VARIALBLES
    music_rotating_check = 1
    run_about = True
    angle_x = 0
    click = False

    while run_about:

        bg_img('Images\stars.png', 0, 0)
        show_png_img('Images\Back button.png', 30, 720)

        pygame.draw.rect(screen, grey, (50, 50, 900, 650))
        pygame.draw.rect(screen, white, (50, 50, 900, 650), 10)

        show_txt('About the Game and Developer - ', 255, 255, 255, 50, 100, 80)
        show_txt('Classic pong game is developed by Sushant G. as a part of',
                 255, 255, 255, 30, 100, 170)
        show_txt("his Computer Science project under the guidance of ",
                 255, 255, 255, 30, 100, 210)
        show_txt("Mrs. Niti Arora Ma'am. This game is built using python",
                 255, 255, 255, 30, 100, 250)
        show_txt("programming language. Pygame, random and time modules ",
                 255, 255, 255, 30, 100, 290)
        show_txt("have been used during coding this game. This game uses ",
                 255, 255, 255, 30, 100, 330)
        show_txt("MySQL database to store data of the game on the local",
                 255, 255, 255, 30, 100, 370)
        show_txt("computer. This is an offline game and does not use any ",
                 255, 255, 255, 30, 100, 410)
        show_txt("type of online transactions. All the objects in this game ",
                 255, 255, 255, 30, 100, 450)
        show_txt("are free of cost.", 255, 255, 255, 30, 100, 490)
        show_txt("Hope you enjoy it!!!", 255, 255, 255, 30, 100, 530)
        show_txt("Developer's contact number - +91 7827189481",
                 255, 255, 255, 35, 100, 580)
        show_txt("Developer's email ID - sushantsg29@gmail.com",
                 255, 255, 255, 35, 100, 630)

        mouse = pygame.mouse.get_pos()

        if disk_rot == False:
            # rotation stopped
            show_png_img('Images\Music_icon.png', 925, 725)
            pygame.draw.line(screen, light_red, (925, 725), (975, 775), 5)

        elif disk_rot == True:
            angle_x -= 2
            icon_rot(angle_x)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if mouse_over(925, 725, 50, 50, mouse): # PAUSING OR RESUMING THE FUCNTION
                    click = True
                    music_rotating_check += 1
                    if music_rotating_check % 2 == 0: 
                        pygame.mixer.music.pause()
                        disk_rot = False
                    elif music_rotating_check % 2 != 0:
                        mixer.music.unpause()
                        disk_rot = True

                elif mouse_over(30, 720, 50, 50, mouse): # CLICKING BACK BUTTON
                    click = True
                    run_about = False
                if click == True and click_muted == False:
                    click_sound = mixer.Sound('Music\Click.wav')
                    click_sound.play()
            if event.type == pygame.MOUSEBUTTONUP:
                click = False

        pygame.display.update() # UPDATING THE DISPLAY

# CREATING THE FUNCTION TO TRANSFORM THE IMAGE
def transform_image(img_name, i_x, i_y):
    screen.blit(pygame.transform.scale(pygame.image.load(
        img_name).convert(), (125, 100)), (i_x, i_y))

# CREATING FUNCTION TO CHECK IF ANY BOX IS CLICKED IN THE SETTING. iF CLICKED RETRUNING ITS CORDINATES AND COLORS
def return_color_block_x_y(x, y, mouse):
    #global color_clicked
    color_clicked = False
    if mouse_over(x, y, 30, 30, mouse):
        cordinates = mouse_over(x, y, 30, 30, mouse)
        x, y = cordinates[0], cordinates[1]
        color = black
        color_clicked = True
    elif mouse_over(x, y+40, 30, 30, mouse):
        cordinates = mouse_over(x, y+40, 30, 30, mouse)
        x, y = cordinates[0], cordinates[1]
        color = light_red
        color_clicked = True
    elif mouse_over(x, y+80, 30, 30, mouse):
        cordinates = mouse_over(x, y+80, 30, 30, mouse)
        x, y = cordinates[0], cordinates[1]
        color = pygame.Color('deepskyblue3')
        color = (color[0], color[1], color[2])
        color_clicked = True
    elif mouse_over(x, y+120, 30, 30, mouse):
        cordinates = mouse_over(x, y+120, 30, 30, mouse)
        x, y = cordinates[0], cordinates[1]
        color = (0, 128, 55)
        color_clicked = True
    elif mouse_over(x+70, y, 30, 30, mouse):
        cordinates = mouse_over(x+70, y, 30, 30, mouse)
        x, y = cordinates[0], cordinates[1]
        color = pygame.Color('gray24')
        color = (color[0], color[1], color[2])
        color_clicked = True
    elif mouse_over(x+70, y+40, 30, 30, mouse):
        cordinates = mouse_over(x+70, y+40, 30, 30, mouse)
        x, y = cordinates[0], cordinates[1]
        color = (255, 87, 87)
        color_clicked = True
    elif mouse_over(x+70, y+80, 30, 30, mouse):
        cordinates = mouse_over(x+70, y+80, 30, 30, mouse)
        x, y = cordinates[0], cordinates[1]
        color = pygame.Color('darkturquoise')
        color = (color[0], color[1], color[2])
        color_clicked = True
    elif mouse_over(x+70, y+120, 30, 30, mouse):
        cordinates = mouse_over(x+70, y+120, 30, 30, mouse)
        x, y = cordinates[0], cordinates[1]
        color = (126, 217, 87)
        color_clicked = True
    elif mouse_over(x+140, y, 30, 30, mouse):
        cordinates = mouse_over(x+140, y, 30, 30, mouse)
        x, y = cordinates[0], cordinates[1]
        color = pygame.Color('grey57')
        color = (color[0], color[1], color[2])
        color_clicked = True
    elif mouse_over(x+140, y+40, 30, 30, mouse):
        cordinates = mouse_over(x+140, y+40, 30, 30, mouse)
        x, y = cordinates[0], cordinates[1]
        color = (255, 102, 196)
        color_clicked = True
    elif mouse_over(x+140, y+80, 30, 30, mouse):
        cordinates = mouse_over(x+140, y+80, 30, 30, mouse)
        x, y = cordinates[0], cordinates[1]
        color = pygame.Color('aquamarine1')
        color = (color[0], color[1], color[2])
        color_clicked = True
    elif mouse_over(x+140, y+120, 30, 30, mouse):
        cordinates = mouse_over(x+140, y+120, 30, 30, mouse)
        x, y = cordinates[0], cordinates[1]
        color = (201, 226, 101)
        color_clicked = True
    elif mouse_over(x+210, y, 30, 30, mouse):
        cordinates = mouse_over(x+210, y, 30, 30, mouse)
        x, y = cordinates[0], cordinates[1]
        color = pygame.Color('grey74')
        color = (color[0], color[1], color[2])
        color_clicked = True
    elif mouse_over(x+210, y+40, 30, 30, mouse):
        cordinates = mouse_over(x+210, y+40, 30, 30, mouse)
        x, y = cordinates[0], cordinates[1]
        color = (140, 82, 255)
        color_clicked = True
    elif mouse_over(x+210, y+80, 30, 30, mouse):
        cordinates = mouse_over(x+210, y+80, 30, 30, mouse)
        x, y = cordinates[0], cordinates[1]
        color = (82, 113, 255)
        color_clicked = True
    elif mouse_over(x+210, y+120, 30, 30, mouse):
        cordinates = mouse_over(x+210, y+120, 30, 30, mouse)
        x, y = cordinates[0], cordinates[1]
        color = (255, 222, 89)
        color_clicked = True
    elif mouse_over(x+280, y, 30, 30, mouse):
        cordinates = mouse_over(x+280, y, 30, 30, mouse)
        x, y = cordinates[0], cordinates[1]
        color = (255, 255, 255)
        color_clicked = True
    elif mouse_over(x+280, y+40, 30, 30, mouse):
        cordinates = mouse_over(x+280, y+40, 30, 30, mouse)
        x, y = cordinates[0], cordinates[1]
        color = (94, 23, 235)
        color_clicked = True
    elif mouse_over(x+280, y+80, 30, 30, mouse):
        cordinates = mouse_over(x+280, y+80, 30, 30, mouse)
        x, y = cordinates[0], cordinates[1]
        color = (0, 74, 173)
        color_clicked = True
    elif mouse_over(x+280, y+120, 30, 30, mouse):
        cordinates = mouse_over(x+280, y+120, 30, 30, mouse)
        x, y = cordinates[0], cordinates[1]
        color = (255, 145, 77)
        color_clicked = True

    else:
        color_clicked = False

    if color_clicked == True:
        return x, y, color_clicked, color
    elif color_clicked == False:
        return x, y, color_clicked

# CREATING FUNCTION TO RETURN THE IMAGE CORDINATES
def return_image_cord(mouse):

    if 45 < mouse[1] < 435:
        var_obj.image_clicked = False
    if mouse_over(400, 140, 125, 100, mouse):
        ix, iy = 400, 140
        var_obj.image_clicked = True
        bg_image = 'Images\digital.png'
    elif mouse_over(600, 140, 125, 100, mouse):
        ix, iy = 600, 140
        var_obj.image_clicked = True
        bg_image = 'Images\greenland.png'
    elif mouse_over(800, 140, 125, 100, mouse):
        ix, iy = 800, 140
        var_obj.image_clicked = True
        bg_image = 'Images\pink city.png'
    elif mouse_over(400, 270, 125, 100, mouse):
        ix, iy = 400, 270
        var_obj.image_clicked = True
        bg_image = 'Images\space desert.png'
    elif mouse_over(600, 270, 125, 100, mouse):
        ix, iy = 600, 270
        var_obj.image_clicked = True
        bg_image = 'Images\space.png'
    if var_obj.image_clicked == True:
        return ix, iy, bg_image

# CREATING FUNCTION TO SHORTEN THE IMAGES BY TRANSFORMING THEM 
def customize_bg_images(x, y):
    transform_image('Images\digital.png', x, y)
    transform_image('Images\greenland.png', x+200, y)
    transform_image('Images\pink city.png', x+400, y)
    transform_image('Images\space desert.png', x, y+130)
    transform_image('Images\space.png', x+200, y+130)

# CREATING FUNCTION TO DISPLAY THE COLOURED BOXES ON THE SCREEN
def customize_color(x, y):

    pygame.draw.rect(screen, black, (x, y, 30, 30))
    pygame.draw.rect(screen, light_red, (x, y+40, 30, 30))
    pygame.draw.rect(screen, pygame.Color('deepskyblue3'), (x, y+80, 30, 30))
    pygame.draw.rect(screen, (0, 128, 55), (x, y+120, 30, 30))
    pygame.draw.rect(screen, pygame.Color('gray24'), (x+70, y, 30, 30))
    pygame.draw.rect(screen, (255, 87, 87), (x+70, y+40, 30, 30))
    pygame.draw.rect(screen, pygame.Color(
        'darkturquoise'), (x+70, y+80, 30, 30))
    pygame.draw.rect(screen, (126, 217, 87), (x+70, y+120, 30, 30))
    pygame.draw.rect(screen, pygame.Color('grey57'), (x+140, y, 30, 30))
    pygame.draw.rect(screen, (255, 102, 196), (x+140, y+40, 30, 30))
    pygame.draw.rect(screen, pygame.Color(
        'aquamarine1'), (x+140, y+80, 30, 30))
    pygame.draw.rect(screen, (201, 226, 101), (x+140, y+120, 30, 30))
    pygame.draw.rect(screen, pygame.Color('grey74'), (x+210, y, 30, 30))
    pygame.draw.rect(screen, (140, 82, 255), (x+210, y+40, 30, 30))
    pygame.draw.rect(screen, (82, 113, 255), (x+210, y+80, 30, 30))
    pygame.draw.rect(screen, (255, 222, 89), (x+210, y+120, 30, 30))
    pygame.draw.rect(screen, (255, 255, 255), (x+280, y, 30, 30))
    pygame.draw.rect(screen, (94, 23, 235), (x+280, y+40, 30, 30))
    pygame.draw.rect(screen, (0, 74, 173), (x+280, y+80, 30, 30))
    pygame.draw.rect(screen, (255, 145, 77), (x+280, y+120, 30, 30))

# CREATING FUNCTION TO CHANGE THE SETTINGS OF THE GAME
def settings():

    global click_muted, music_muted, disk_rot

    # VARIABLES
    run_settings = True
    music_rotating_check = 1
    app_selected, help_selected, audio_selected = True, False, False
    button_pressed = False
    customise_bg, customize_tile = True, False
    ball_selected, tile_selected = False, False
    click = False
    angle_x = 0
    vol_x = 400 + int((100 * pygame.mixer.music.get_volume()) * 4)

    while run_settings:

        mouse = pygame.mouse.get_pos() # GETTING THE MOUSE CORDINATES

        bg_img('Images\stars.png', 0, 0) # BG IMAGE

        # DRAWING THE OBJECT ON THE SCREEN
        pygame.draw.rect(screen, (130, 130, 130), (0, 0, 300, 800))
        pygame.draw.rect(screen, grey, (0, 0, 298, 200))

        appearance_command = Button__(0, 200, 298, 100,light_pink,med_pink,dark_pink,mouse,click,'APPEARANCE', 40,0).button_blit()
        audio_command = Button__(0, 300, 298, 100,light_cyan,med_cyan,dark_cyan,mouse,click,'AUDIO', 40,0).button_blit()
        help_command = Button__(0, 400, 298, 100,light_mint,med_mint,dark_mint,mouse,click,'HELP',40,0).button_blit()
        done_command = Button__(30,725,110,50,light_peach,med_peach,dark_peach,mouse,click,'DONE',30,0).button_blit()
        pygame.draw.rect(screen, black, (30,725,110,50),3)

        pygame.draw.line(screen, white, (300, 0), (300, 800), 5)
        pygame.draw.line(screen, black, (0, 200), (297, 200), 6)
        pygame.draw.line(screen, black, (0, 300), (297, 300), 6)
        pygame.draw.line(screen, black, (0, 400), (297, 400), 6)
        pygame.draw.line(screen, black, (0, 500), (297, 500), 6)

        # SHOWIG THE TEXT ON  THE SCREEN
        show_txt('Settings', 255, 255, 255, 50, 45, 60)

        if appearance_command == True:app_selected, audio_selected, help_selected = True, False, False
        elif audio_command == True:app_selected, audio_selected, help_selected = False, True, False
        elif help_command == True:app_selected, audio_selected, help_selected = False, False, True
        elif done_command == True:click = True ; run_settings = False

        # EVENT LOOP
        for event in pygame.event.get():
            if event.type == pygame.QUIT:sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                button_pressed = True

                if mouse_over(925, 725, 50, 50, mouse):
                    click = True
                    music_rotating_check += 1
                    if music_rotating_check % 2 == 0: # PLAYING/PAUSING THE MUSIC
                        pygame.mixer.music.pause()
                        disk_rot = False
                        music_muted = True
                    elif music_rotating_check % 2 != 0:
                        pygame.mixer.music.unpause()
                        disk_rot = True
                        music_muted = False

                elif mouse_over(30,725,110,50, mouse) or mouse_over(0, 200, 300, 100, mouse) or mouse_over(0, 300, 300, 100, mouse) or mouse_over(0, 400, 300, 100, mouse):click = True

                if app_selected == True: # APPEARANCE SELECTED

                    if mouse_over(355, 700, 380, 30, mouse):
                        customise_bg = True
                        customize_tile = False
                        click = True
                    elif mouse_over(355, 740, 380, 30, mouse):
                        customize_tile = True
                        customise_bg = False
                        click = True

                    if customise_bg == True: # CUSTOMIZING THE BG

                        if 50 < mouse[1] < 435: # SELECTING THE IMAGE
                            
                            var_obj.selecting_bg_img = True
                            var_obj.selecting_bg_color = False
                            if mouse_over(400,140,125,100,mouse) or mouse_over(600,140,125,100,mouse) or mouse_over(800,140,125,100,mouse) or mouse_over(400,270,125,100,mouse) or mouse_over(600,270,125,100,mouse):
                                var_obj.img_sel_cord = return_image_cord(mouse) # LIST OF RETURNED VARIABLES

                                if var_obj.image_clicked == True:
                                    var_obj.image_name = var_obj.img_sel_cord[2] # IMAGE NAME
                                    click = True

                        elif 400 < mouse[1] < 660: # SELECTING THE BG COLOR

                            var_obj.selecting_bg_color = True
                            var_obj.selecting_bg_img = False
                            if mouse_over(490,470,310,150,mouse):
                                var_obj.cor = return_color_block_x_y(
                                    490, 470, mouse)
                                color_clicked = var_obj.cor[2] # LIST OF RETURNED VARIABLES
                                if color_clicked == True:
                                    click = True
                                    var_obj.color_bg = var_obj.cor[3] # SETING THE BG COLOR 
                                    var_obj.color_selected = True # SELECTING / DESELECTING THE COLOR
                                else:
                                    var_obj.color_selected = False

                    elif customize_tile == True: # CUSTOMIZING THE TILE / BALL

                        if 50 < mouse[1] < 435:
                            tile_selected = True
                            ball_selected = False
                            click = True
                        elif 400 < mouse[1] < 660:
                            ball_selected = True
                            tile_selected = False
                            click = True
                        else:
                            ball_selected, tile_selected = False, False

                        if tile_selected == True: # CUSOMIZING THE TILE
                            if mouse_over(440,110,310,150,mouse):
                                var_obj.cor_tile = return_color_block_x_y(
                                    440, 110, mouse)
                                var_obj.color_tile_clicked = var_obj.cor_tile[2] # SELECTING / DESELECTING THE COLOR

                                if var_obj.color_tile_clicked == True:
                                    click = True
                                    var_obj.color_tile = var_obj.cor_tile[3] # CHOSING COLOR OF TILE
                                    var_obj.color_tile_selected = True
                                else:
                                    var_obj.color_tile_selected = False

                            # CHOSING HOLLOW / SOLID TILE
                            if mouse_over(412.5, 285, 142.5, 55, mouse):
                                click = True
                                var_obj.selecting_tile_hs = True 
                                var_obj.tile_hollow = False
                            elif mouse_over(612.5, 285, 160, 55, mouse):
                                click = True
                                var_obj.selecting_tile_hs = True
                                var_obj.tile_hollow = True

                        elif ball_selected == True:
                            if mouse_over(440,430,310,150,mouse):
                                var_obj.cor_ball = return_color_block_x_y(
                                    440, 435, mouse)
                                var_obj.color_ball_clicked = var_obj.cor_ball[2]  # CHECKING IF THE USE IS SELECCTING THE BALL

                                if var_obj.color_ball_clicked == True:
                                    click = True
                                    var_obj.color_ball = var_obj.cor_ball[3] # CHOOSING THE COLOR OF THE BALL
                                    var_obj.color_ball_selected = True 
                                else:
                                    var_obj.color_ball_selected = False
                            if mouse_over(412.5, 600, 142.5, 55, mouse): # CHOSING HOLLOW/SOLDI BALL
                                click = True
                                var_obj.ball_hollow = False
                                var_obj.selecting_ball_hs = True
                            elif mouse_over(612.5, 600, 160, 55, mouse):
                                click = True
                                var_obj.ball_hollow = True
                                var_obj.selecting_ball_hs = True

                elif audio_selected == True: # AUDIO TAB SELECTED
                    # MUTING / UNMUTING THE CLICK SOUND
                    if mouse_over(670, 295, 245, 50, mouse): 
                        click = True
                        click_muted = False
                    elif mouse_over(390, 295, 215, 50, mouse):
                        click_muted = True
                    # MUTING / UNMUTING THE MUSIC
                    elif mouse_over(390, 460, 295, 50, mouse):
                        click = True
                        music_muted = True
                    elif mouse_over(390, 525, 310, 50, mouse):
                        click = True
                        music_muted = False

                if click_muted == False and click == True: # PLAYING THE CLICK SOUND
                    click_sound = mixer.Sound('Music\Click.wav')
                    click_sound.play()

            elif event.type == pygame.MOUSEBUTTONUP: # MOUSE BUTOON RELEASED
                button_pressed = False
                click = False

        if app_selected == True: # APPEARANCE TAB SELECTED

            # DRAWING THE ONJECTS ONT HE SCRENN
            pygame.draw.rect(screen, light_red, (0, 203, 297, 100), 5)
            pygame.draw.rect(screen, grey, (330, 20, 640, 650))
            pygame.draw.rect(screen, white, (330, 20, 640, 650), 5)
            pygame.draw.circle(screen, white, (370, 722), 10)
            pygame.draw.circle(screen, white, (370, 762), 10)

            show_txt('Customize Background',
                     white[0], white[0], white[0], 30, 400, 700)
            show_txt('Customize Objects',
                     white[0], white[0], white[0], 30, 400, 740)

            if customise_bg == True: # CUSTOMIZING THE BG
                pygame.draw.circle(screen, black, (370, 722), 6)
                pygame.draw.circle(screen, white, (370, 80), 13)
                pygame.draw.circle(screen, white, (370, 430), 13)

                show_txt('Choose background image', 255, 255, 255, 40, 400, 50)
                show_txt('Choose background color',
                         255, 255, 255, 40, 400, 400)

                customize_bg_images(400, 140) # DRAWING THE IMAGES TO BE SELECTED
                customize_color(490, 470) # DRAWING THE COLOURED TILES

                if var_obj.selecting_bg_img == True: # SELECTING THE BG IMAGE
                    pygame.draw.circle(screen, black, (370, 80), 9)
                    if var_obj.image_clicked == True:
                        pygame.draw.rect(
                            screen, light_red, (var_obj.img_sel_cord[0], var_obj.img_sel_cord[1], 125, 100), 5)

                elif var_obj.selecting_bg_color == True: # SELECYTING THE BG COLOR
                    pygame.draw.circle(screen, black, (370, 430), 9)
                    if var_obj.color_selected == True:
                        pygame.draw.rect(screen, (255, 0, 0),
                                         (var_obj.cor[0], var_obj.cor[1], 30, 30), 5)

            elif customize_tile == True: # CUSTOMIZING BALL / TILE 

                # DRAWING THE OBJECTS ON THE SCREEN
                pygame.draw.circle(screen, white, (370, 60), 13)
                pygame.draw.circle(screen, white, (370, 385), 13)
                pygame.draw.circle(screen, black, (370, 762), 6)

                customize_color(440, 110) # DRAWING THE COLOURED TILES FOR THE TILES
                customize_color(440, 435) # DRAWING THE COLOURED TILES FOR THE BALL

                show_txt('Customize tile', 255, 255, 255, 40, 400, 30)
                show_txt('Customize ball', 255, 255, 255, 40, 400, 355)

                show_txt('Solid tile', white[0],
                         white[0], white[0], 30, 420, 290)
                show_txt('Hollow tile', white[0],
                         white[0], white[0], 30, 620, 290)

                show_txt('Solid ball', white[0],
                         white[0], white[0], 30, 420, 605)
                show_txt('Hollow ball', white[0],
                         white[0], white[0], 30, 620, 605)

                # FIGURING BALL/TILE SELECTED
                if var_obj.color_tile_selected == True:
                    pygame.draw.rect(screen, light_red,
                                     (var_obj.cor_tile[0], var_obj.cor_tile[1], 30, 30), 5)
                if var_obj.color_ball_selected == True:
                    pygame.draw.rect(screen, light_red,
                                     (var_obj.cor_ball[0], var_obj.cor_ball[1], 30, 30), 5)

                if tile_selected == True:
                    pygame.draw.circle(screen, black, (370, 60), 9)
                elif ball_selected == True:
                    pygame.draw.circle(screen, black, (370, 385), 9)

                # DRAWING THE MODEL OF THE TILE
                if var_obj.tile_hollow == True:
                    pygame.draw.rect(screen, var_obj.color_tile,
                                      (850, 150, 20, 80), 5)
                    pygame.draw.rect(screen, light_red,
                                      (612.5, 285, 160, 55), 3)
                else:
                    pygame.draw.rect(screen, var_obj.color_tile, (850, 150, 20, 80))
                    pygame.draw.rect(screen, light_red,
                                    (412.5, 285, 142.5, 55), 3)

                # DRAWING THE MODEL OF THE BALL
                if var_obj.ball_hollow == True:
                    pygame.draw.circle(
                        screen, var_obj.color_ball, (850, 500), 25, 5)
                    pygame.draw.rect(screen, light_red,
                                     (612.5, 600, 160, 55), 3)
                else:
                    pygame.draw.circle(
                        screen, var_obj.color_ball, (850, 500), 25)
                    pygame.draw.rect(screen, light_red,
                                     (412.5, 600, 142.5, 55), 3)

        elif audio_selected == True: # AUDIO TAB SELECTED

            # DRAWING THE OBJECTS ON THE SCREEN
            pygame.draw.rect(screen, light_red, (0, 303, 297, 100), 5)
            pygame.draw.rect(screen, grey, (330, 20, 640, 750))
            pygame.draw.rect(screen, white, (330, 20, 640, 750), 5)
            pygame.draw.circle(screen, white, (370, 80), 13)
            pygame.draw.circle(screen, white, (370, 230), 13)
            pygame.draw.circle(screen, white, (370, 410), 13)

            show_txt('Set music volume',
                     white[0], white[0], white[0], 40, 400, 50)
            show_txt('Click sound', white[0], white[0], white[0], 40, 400, 200)
            show_txt('Mute click sound',
                     white[0], white[0], white[0], 25, 400, 300)
            show_txt('Unmute click sound',
                     white[0], white[0], white[0], 25, 680, 300)
            show_txt('Background Music',
                     white[0], white[0], white[0], 40, 400, 380)
            show_txt('Mute background music ',
                     white[0], white[0], white[0], 25, 400, 465)
            show_txt('Unmute backgound music',
                     white[0], white[0], white[0], 25, 400, 530)

            # DRAWING THE VOLUME SLIDER 
            pygame.draw.line(screen, (0, 0, 0), (400, 150), (800, 150), 5)
            pygame.draw.line(screen, pygame.Color(
                'darkturquoise'), (400, 150), (vol_x, 150), 5)
            pygame.draw.circle(screen, (255, 255, 255), (vol_x, 150), 10)

            volume_level = 1 - ((800 - vol_x) / 400) # SETTING UP THE VOLUME
            pygame.mixer.music.set_volume(volume_level)

            show_txt(str(int(volume_level * 100)), 255, 255, 255, 40, 830, 120) # SHOWING THE VOLUME LEVEL

            if button_pressed == True: # CHANGING THE VOLUME LEVEL
                if 400 < mouse[0] < 804 and 130 < mouse[1] < 170:vol_x = mouse[0]

            # MUTING / UNMUTING THE CLICK
            if click_muted == True:
                pygame.draw.rect(screen, light_red, (390, 295, 215, 50), 3)
                pygame.mixer.music.pause()
            elif click_muted == False:
                pygame.draw.rect(screen, light_red, (670, 295, 245, 50), 3)
                pygame.mixer.music.unpause()

            # MUTING / UNMUTING THE MUSIC
            if music_muted == True :
                pygame.draw.rect(screen, light_red, (390, 460, 295, 50), 3)
                disk_rot = False
            elif music_muted == False :
                pygame.draw.rect(screen, light_red, (390, 525, 310, 50), 3)
                disk_rot = True

        elif help_selected == True: # SELECTING THE HELP TAB
            pygame.draw.rect(screen, light_red, (0, 403, 297, 100), 5)
            pygame.draw.circle(screen, white, (370, 100), 13)
            pygame.draw.circle(screen, white, (370, 180), 8)
            pygame.draw.circle(screen, white, (370, 480), 8)

            show_txt('Controls', 255, 255, 255, 50, 401, 45)
            show_txt('Player 1', 255, 255, 255, 40, 418, 150)
            show_txt('Player 2 / Vs A.I.', 255, 255, 255, 40, 418, 450)
            show_txt('For more info email at sushantsg29@gmail.com',
                     255, 255, 255, 25, 358, 750)

            # P-1 DRAWING KEYS AND LINES
            pygame.draw.rect(screen, key_color, (450, 240, 60, 60))
            show_txt('W', 255, 255, 255, 30, 460, 240)
            pygame.draw.rect(screen, white, (450, 240, 60, 60), 3)

            pygame.draw.rect(screen, key_color, (470, 310, 60, 60))
            show_txt('S', 255, 255, 255, 30, 480, 310)
            pygame.draw.rect(screen, white, (470, 310, 60, 60), 3)

            pygame.draw.rect(screen, grey, (400, 310, 60, 60))
            show_txt('A', 255, 255, 255, 30, 410, 310)
            pygame.draw.rect(screen, white, (400, 310, 60, 60), 3)

            pygame.draw.rect(screen, grey, (540, 310, 60, 60))
            show_txt('D', 255, 255, 255, 30, 550, 310)
            pygame.draw.rect(screen, white, (540, 310, 60, 60), 3)

            pygame.draw.line(screen, white, (495, 260), (595, 260), 3)
            show_txt('Move tile up', 255, 255, 255, 20, 615, 243)

            pygame.draw.line(screen, white, (515, 355), (515, 400), 3)
            pygame.draw.line(screen, white, (515, 400), (575, 400), 3)
            show_txt('Move tile down', 255, 255, 255, 20, 585, 383)

            # P-2 DRAWING KEYS AND LINES
            pygame.draw.rect(screen, key_color, (470, 540, 60, 60))
            pygame.draw.rect(screen, white, (470, 540, 60, 60), 3)
            pygame.draw.line(screen, white, (490, 560), (490, 580), 3)
            pygame.draw.polygon(
                screen, white, ((490, 555), (485, 565), (495, 565)))

            pygame.draw.rect(screen, key_color, (470, 610, 60, 60))
            pygame.draw.rect(screen, white, (470, 610, 60, 60), 3)
            pygame.draw.line(screen, white, (490, 625), (490, 640), 3)
            pygame.draw.polygon(
                screen, white, ((490, 650), (485, 640), (495, 640)))

            pygame.draw.rect(screen, grey, (400, 610, 60, 60))
            pygame.draw.rect(screen, white, (400, 610, 60, 60), 3)
            pygame.draw.line(screen, white, (425, 640), (440, 640), 3)
            pygame.draw.polygon(
                screen, white, ((415, 640), (425, 635), (425, 645)))

            pygame.draw.rect(screen, grey, (540, 610, 60, 60))
            pygame.draw.rect(screen, white, (540, 610, 60, 60), 3)
            pygame.draw.line(screen, white, (555, 640), (570, 640), 3)
            pygame.draw.polygon(
                screen, white, ((580, 640), (570, 635), (570, 645)))

            pygame.draw.line(screen, white, (515, 560), (575, 560), 3)
            show_txt('Move tile up', 255, 255, 255, 20, 595, 543)

            pygame.draw.line(screen, white, (515, 655), (515, 700), 3)
            pygame.draw.line(screen, white, (515, 700), (565, 700), 3)
            show_txt('Move tile down', 255, 255, 255, 20, 575, 683)


        if disk_rot == False: # rotation stopped
            music_muted = True
            show_png_img('Images\Music_icon.png', 925, 725)
            pygame.draw.line(screen, light_red, (925, 725), (975, 775), 5)
            pygame.mixer.music.pause()

        elif disk_rot == True: # ROTATION RESUMED
            music_muted = False
            angle_x -= 2
            icon_rot(angle_x)
            pygame.mixer.music.unpause()

        pygame.time.Clock().tick(100) # SETTING UP THE FPS
        pygame.display.update() # UPDATING THE SCREEN

# CREATING FUNCTION TO PLAY AGAINST THE COMPUTER
def ai(speed, username):
    global run_ai,p_s,high_score_ai_free

    # variables
    lst = var_obj.return_var()  # GETTING BG AND OBJECT COLOR
    none_selected_bg = lst[7];none_selected_tile = lst[8];none_selected_ball = lst[9]
    selecting_bg_img = lst[10];color_selected_bg = lst[11]
    hollow_tile = lst[13];hollow_ball = lst[15]
    tile_hs = lst[14];ball_hs = lst[16];image_clicked = lst[12]
    if none_selected_bg == True:color_of_bg = lst[0]
    else:color_of_bg = lst[5];img_name = lst[6]
    if none_selected_tile == True:color_of_tile = lst[1]
    else:color_of_tile = lst[4]
    if none_selected_ball == True:color_of_ball = lst[2]
    else:color_of_ball = lst[3]

    c = False;start = True;lst = [['d', 'u'], ['r', 'l']];score_increase = False

    speed_var = speed
    if speed_var == 8:speed_var_x = 13
    elif speed_var == 10:speed_var_x = 15
    elif speed_var == 12:speed_var_x = 20

    # PLAYING THE MUSIC
    mixer.music.load('Music\Play music.mp3');mixer.music.play(-1)
    if disk_rot == False:pygame.mixer.music.pause()  # IF DISK_ROT = FALSE PAUSING THE MUSIC

    # Creating player
    p_x = 960;p_y = 360;p_w = 20;p_h = 80;p_y_change = 0

    # Second player (computer)
    c_x = 40;c_y = 360;c_w = 20;c_h = 80;c_y_change = 5

    # creating ball:
    b_x = 500;b_y = 400;b_y_change = speed;b_x_change = speed

    # scores
    p_s = 0;lives = 5;c_lives = 5
    clock = pygame.time.Clock()

    run_ai = True;var_obj.run_ai = True
    timer = [1, 2, 3];p_s_x = 600;c_s_x = 100

    # FETCHING THE DATA FROM THE DATABASE
    mycursor.execute('select * from classic_pong_game')
    for data in mycursor:
        if data[0] == username:high_score_ai = data[2];high_score_ai_free = data[3]

    while run_ai == True:

        # BG FILL
        if color_selected_bg == True:
            screen.fill(color_of_bg)  # BACKGROUND COLOR FILL
            clock.tick(60)
            speed = speed_var
            if b_y_change < 0:b_y_change = -speed_var
            if b_y_change > 0:b_y_change = speed_var
            if b_x_change < 0:b_x_change = -speed_var
            if b_x_change > 0:b_x_change = speed_var
        elif selecting_bg_img == True and image_clicked == True:
            bg_img(img_name,0,0)

            # IF BG IMAGE IS SELECTING, I'M INCERASING THE SPEED TO NEUTRALIZE THE LAG DUE TO RENDERING OF BG IMAGE
            speed = speed_var_x
            clock.tick(100)
            if b_y_change < 0:b_y_change = -speed
            if b_y_change > 0:b_y_change = speed
            if b_x_change < 0:b_x_change = -speed
            if b_x_change > 0:b_x_change = speed

        else:
            screen.fill(color_of_bg)
            clock.tick(60)
            speed = speed_var
            if b_y_change < 0:b_y_change = -speed_var
            if b_y_change > 0:b_y_change = speed_var
            if b_x_change < 0:b_x_change = -speed_var
            if b_x_change > 0:b_x_change = speed_var

        c_y_change = speed

        if game_obj.get_res() == True:  # RESUME TIMER
            # ANALIZING THE CHANGE IF ANY

            lst = var_obj.return_var()
            none_selected_bg = lst[7];none_selected_tile = lst[8];none_selected_ball = lst[9]
            selecting_bg_img = lst[10];color_selected_bg = lst[11]
            hollow_tile = lst[13];hollow_ball = lst[15]
            tile_hs = lst[14];ball_hs = lst[16];image_clicked = lst[12]
            if none_selected_bg == True:color_of_bg = lst[0]
            else:color_of_bg = lst[5];img_name = lst[6]
            if none_selected_tile == True:color_of_tile = lst[1]
            else:color_of_tile = lst[4]
            if none_selected_ball == True:color_of_ball = lst[2]
            else:color_of_ball = lst[3]

            speed = 0;sec = timer[index]

            show_txt(str(sec), 255, 255, 255, 200, 450, 400)
            # SETTING TIMER SPEED BY PAUSING THE SCREEN FOR EVERY 1 SEC
            time.sleep(1)
            index -= 1  # IF INDEX IS -1 THE TIMER WILL NOT SHOW NUMBER '1' ON THE SCREEN
            if index == -2:game_obj.update(False)

        elif game_obj.get_res() == False:index = 2

        show_png_img('Images\pause_button.png', 50, 50)

        # DRAWING THE OBJECT ON THE SCREEN
        if hollow_tile == False and tile_hs == True:
            player_tile = pygame.draw.rect(screen, color_of_tile, (p_x, p_y, p_w, p_h))
            comp_tile = pygame.draw.rect(screen, color_of_tile, (c_x, c_y, c_w, c_h))
        else:
            player_tile = pygame.draw.rect(screen, color_of_tile, (p_x, p_y, p_w, p_h), 5)
            comp_tile = pygame.draw.rect(screen, color_of_tile, (c_x, c_y, c_w, c_h), 5)
        if hollow_ball == False :
            pygame.draw.circle(screen, color_of_ball, (b_x, b_y), 10)
        else:
            pygame.draw.circle(screen, color_of_ball, (b_x, b_y), 10, 3)
        pygame.draw.line(screen, light_red, (0, 150), (1000, 150), 2)
        pygame.draw.line(screen, light_red, (0, 790), (1000, 790), 2)

        mouse = pygame.mouse.get_pos()

        # IF BALL TOUCHES ANY END, CHOSING THE DIRECTION
        if start == True:
            choice_vert = random.choice(lst[0]);choice_hori = random.choice(lst[1])
            c = True
            # CHOSING RANDOM DIRECTIONS
            if choice_vert == 'u':b_y_change = -speed
            elif choice_vert == 'd':b_y_change = speed
            if choice_hori == 'l':b_x_change = -speed
            elif choice_hori == 'r':b_x_change = speed

            b_x += b_x_change ; b_y += b_y_change # BALL MOVEMENT
            

            if score_increase == True:time.sleep(1);score_increase = False
            start = False
            if lives != 0 and free_ai == False: time.sleep(1) # PAUSING THE SCREEN

        elif start == False:
            b_x += b_x_change;b_y += b_y_change
            # CHANGING THE SCORE
            if b_x >= 988:
                score_increase = True
                if free_ai == False:lives -= 1
                else:p_s -= 20
            elif b_x <= 12:
                score_increase = True
                if free_ai == False:c_lives -= 1
                else:p_s += 50
            if free_ai == False:
                if lives == 0 or c_lives == 0:
                    run_ai = False;time.sleep(1)
                    win_lose_screen(c_lives,lives)
                    

        # DISPLAYING THER TEXT ON THE SCREEN
        if free_ai == True:
            show_txt("Highest score : " + str(high_score_ai_free),
                     255, 255, 255, 40, 150, 10)
            show_txt("Score : " + str(p_s), 255, 255, 255, 40, 150, 60)
        else:
            p_width = show_txt(username,255,255,255,40,p_s_x,20)
            p_s_x = 745-(p_width/2)
            p_width = show_txt('Computer',255,255,255,40,c_s_x,20)
            c_s_x = 350-(p_width/2)

        if free_ai == False:
            for life in range(lives):show_png_img('Images\heart.png', 620+(55*life), 90)  # DISPLAYING THE LIFE
                
            for life in range(c_lives): show_png_img('Images\heart.png', 220+(55*life), 90) # DISPLAYING THE LIFE
                

        # EVENT LOOP
        for event in pygame.event.get():
            if event.type == pygame.QUIT:sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_over(50, 50, 50, 50, mouse):  # PAUSE BUTTON
                    pause(username)

            # PRESSING THE KEY
            if event.type == pygame.KEYDOWN:
                # IF BUTTON IS PRESSED A SPECIFIC VALUE IS ADDED OR SUBTEACTED FROM MOVEMENT SPEED TO MOVE THE TILE
                if event.key == pygame.K_UP:
                    if p_y >= 160:p_y_change -= speed
                elif event.key == pygame.K_DOWN:
                    if p_y <= 710:p_y_change += speed
                elif event.key == pygame.K_ESCAPE:pause(username)

            if event.type == pygame.KEYUP:p_y_change = 0

        # PLAYER MOVEMENT
        p_y += p_y_change
        if p_y <= 160:p_y_change = 0
        elif p_y >= 710:p_y_change = 0

        # AI MOVEMENT
        if c == True:  # MOVING THE COMPUTER TILE ACCORDING TO THE CORDINATED OF THE BALL
            if b_y <= 160:c_y_change = 0
            if b_y >= 710:c_y_change = 0

            if b_y < c_y and b_y_change << 0:c_y -= c_y_change
            elif b_y <= c_x and b_y_change >> 0:c_y += c_y_change
            elif b_y >= c_x and b_y_change >> 0:c_y += c_y_change
            elif b_y >= c_x and b_y_change << 0:c_y -= c_y_change

        if b_x >= 988:  # IF BALL PASSES THE PLAYER'S TILE, IT REAPPEARS AT THE CENTER
            b_x = 500;b_y = 400;start = True
        elif b_x <= 12:  # IF BALL PASSES THE COMPUTER'S TILE, IT REAPPEARS AT THE CENTER
            c = False;b_x = 500;b_y = 400;start = True

        # IF BALL GOES BEYOND THE SPECIFIED Y-CORDINATE, IT REVERSES ITS DIRECTIONON Y AXIS
        if b_y >= 780 or b_y <= 160:b_y_change = -b_y_change

        # BALL COLLIDING WITH THE TILES
        if player_tile.collidepoint(b_x,b_y) :
            b_x_change = -b_x_change;c = True 
            if disk_rot == True:mixer.Sound('Music\Collide.wav').play()
        elif comp_tile.collidepoint(b_x,b_y) :
            b_x_change = -b_x_change;c = False
            if disk_rot == True:mixer.Sound('Music\Collide.wav').play()

        run_ai = var_obj.run_ai
        pygame.display.update()  # UPDATING THE SCREEN

# CREATING FUNCTION FOR HUMAN VS HUMAN
def multiplayer(speed, p1_name, p2_name):
    global run_mul, run

    # variables
    lst = var_obj.return_var()  # GETTING BG AND OBJECT COLOR
    none_selected_bg = lst[7];none_selected_tile = lst[8];none_selected_ball = lst[9]
    selecting_bg_img = lst[10];color_selected_bg = lst[11]
    hollow_tile = lst[13];hollow_ball = lst[15]
    tile_hs = lst[14];ball_hs = lst[16];image_clicked = lst[12]
    if none_selected_bg == True:color_of_bg = lst[0]
    else:color_of_bg = lst[5];img_name = lst[6]
    if none_selected_tile == True:color_of_tile = lst[1]
    else:color_of_tile = lst[4]
    if none_selected_ball == True:color_of_ball = lst[2]
    else:color_of_ball = lst[3]

    speed_var = speed
    if speed_var == 8:speed_var_x = 13
    elif speed_var == 10:speed_var_x = 15
    elif speed_var == 12:speed_var_x = 20

    start = True;lst = [['d', 'u'], ['r', 'l']];score_increase = True

    mixer.music.load('Music\Play music.mp3');mixer.music.play(-1)
    if disk_rot == False:pygame.mixer.music.pause()

    # Creating player
    p1_x = 960;p1_y = 360;p1_w = 20;p1_h = 80;p1_y_change = 0

    # Second player (computer)
    p2_x = 40;p2_y = 360;p2_w = 20;p2_h = 80;p2_y_change = 0

    # creating ball:
    b_x = 490;b_y = 390;b_x_change = speed;b_y_change = speed

    # scores
    if free_hum == False:p1_s = 5;p2_s = 5
    else:p1_s = 0;p2_s = 0

    p1_sc_width = 200;p2_sc_width = 600;timer = [1, 2, 3]
    clock = pygame.time.Clock();var_obj.run_mul = True;run_mul = True

    while run_mul == True:

        # BG FILL
        if color_selected_bg == True:
            screen.fill(color_of_bg);clock.tick(60);speed = speed_var
            if b_y_change < 0:b_y_change = -speed_var
            if b_y_change > 0:b_y_change = speed_var
            if b_x_change < 0:b_x_change = -speed_var
            if b_x_change > 0:b_x_change = speed_var
        elif selecting_bg_img == True and image_clicked == True:
            bg_img(img_name,0,0)
            # IF BG IMAGE IS SELECTING, I'M INCERASING THE SPEED TO NEUTRALIZE THE LAG DUE TO RENDERING OF BG IMAGE
            speed = speed_var_x;clock.tick(100)
            if b_y_change < 0:b_y_change = -speed
            if b_y_change > 0:b_y_change = speed
            if b_x_change < 0:b_x_change = -speed
            if b_x_change > 0:b_x_change = speed

        else:
            screen.fill(color_of_bg);speed = speed_var
            if b_y_change < 0:b_y_change = -speed_var
            if b_y_change > 0:b_y_change = speed_var
            if b_x_change < 0:b_x_change = -speed_var
            if b_x_change > 0:b_x_change = speed_var
            clock.tick(60)

        if game_obj.get_res() == True:  # RESUME TIMER
            # ANALIZING THE CHANGE IF ANY

            lst = var_obj.return_var()
            none_selected_bg = lst[7];none_selected_tile = lst[8];none_selected_ball = lst[9]
            selecting_bg_img = lst[10];color_selected_bg = lst[11]
            hollow_tile = lst[13];hollow_ball = lst[15]
            tile_hs = lst[14];ball_hs = lst[16];image_clicked = lst[12]
            if none_selected_bg == True:color_of_bg = lst[0]
            else:color_of_bg = lst[5];img_name = lst[6]
            if none_selected_tile == True:color_of_tile = lst[1]
            else:color_of_tile = lst[4]
            if none_selected_ball == True:color_of_ball = lst[2]
            else:color_of_ball = lst[3]

            speed = 0;sec = timer[index]
            show_txt(str(sec), 255, 255, 255, 200, 450, 400)
            # SETTING TIMER SPEED BY PAUSING THE SCREEN FOR EVERY 1 SEC
            time.sleep(1)
            index -= 1  # IF INDEX IS -1 THE TIMER WILL NOT SHOW NUMBER '1' ON THE SCREEN

            if index == -2:game_obj.update(False)

        elif game_obj.get_res() == False:index = 2

        show_png_img('Images\pause_button.png', 50, 50)

        # DRAWING THE OBJECT ON THE SCREEN
        if hollow_tile == False and tile_hs == True:
            p1_tile = pygame.draw.rect(screen, color_of_tile, (p1_x, p1_y, p1_w, p1_h))
            p2_tile = pygame.draw.rect(screen, color_of_tile, (p2_x, p2_y, p2_w, p2_h))
        else:
            p1_tile = pygame.draw.rect(screen, color_of_tile,(p1_x, p1_y, p1_w, p1_h), 5)
            p2_tile = pygame.draw.rect(screen, color_of_tile,(p2_x, p2_y, p2_w, p2_h), 5)
        if hollow_ball == False :
            pygame.draw.circle(screen, color_of_ball, (b_x, b_y), 10)
        else:
            pygame.draw.circle(screen, color_of_ball, (b_x, b_y), 10, 3)
        pygame.draw.line(screen, light_red, (0, 150), (1000, 150), 2)
        pygame.draw.line(screen, light_red, (0, 790), (1000, 790), 2)

        if free_hum == False:
            if p1_s == 0 or p2_s == 0:  # BREAKING THE FUNCTION
                run_mul = False
                win_lose_screen(p1_s,p2_s,p1_name,p2_name)
                time.sleep(1)
                
        # IF BALL TOUCHES ANY END, CHOSING THE DIRECTION
        if start == True:
            # CHOOSING RANDOM DIRECTION WHEN BALL HITS ANY EXTREME ENDS ON X-AXIS
            choice_vert = random.choice(lst[0]);choice_hori = random.choice(lst[1])
            if choice_vert == 'u':b_y_change = -speed
            elif choice_vert == 'd':b_y_change == speed
            if choice_hori == 'l':b_x_change = -speed
            elif choice_hori == 'r':b_x_change = speed
            b_x += b_x_change;b_y += b_y_change
            score_increase = True
            start = False
            time.sleep(1)  # PAUSING THE SCREEN

        elif start == False:
            b_x += b_x_change;b_y += b_y_change  # BALL MOVEMENT IN X AND Y DIRECTION
            
            if score_increase == True:  # CHANGING THE SCORE
                if b_x >= 988:  # CHECKING IF THE SCORE HAS TO BE CHANGED
                    if free_hum == False:p2_s -= 1  # IF FREE_HUM = FALSE, DECREASE THE LIFE
                    else:p1_s += 20  # ELSE INCREASE THE SCORE
                    score_increase = False
                elif b_x <= 12:  # CHECKING IF THE SCORE HAS TO BE CHANGED
                    if free_hum == False:p1_s -= 1
                    else:p2_s += 20
                    score_increase = False

        # score change
        p1_width = show_txt(p1_name, 255, 255, 255, 40, 200, 20)
        p2_width = show_txt(p2_name, 255, 255, 255, 40, 600, 20)

        if free_hum == False:
            # DISPLAYING THE LIFE REAMINING
            for life_1 in range(p1_s):show_png_img('Images\heart.png', 200+(50*life_1), 90)

            for life_2 in range(p2_s):show_png_img('Images\heart.png', 600+(50*life_2), 90)

        else:
            # DSIPLAYING THE SCROE
            p1_s_width = show_txt(str(p1_s), 255, 255,
                                  255, 40, p1_sc_width, 90)
            p2_s_width = show_txt(str(p2_s), 255, 255,
                                  255, 40, p2_sc_width, 90)
            p1_sc_width = 200+(p1_width/2)-(p1_s_width/2)
            p2_sc_width = 600+(p2_width/2)-(p2_s_width/2)

        mouse = pygame.mouse.get_pos()  # GETTING MOUSE CORDINATE

        # EVENT LOOP
        for event in pygame.event.get():
            if event.type == pygame.QUIT:sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_over(50, 50, 50, 50, mouse): pause('s') # CLICKING PAUSE BUTTON

            # PRESSING THE KEY
            if event.type == pygame.KEYDOWN:
                # IF BUTTON IS PRESSED A SPECIFIC VALUE IS ADDED OR SUBTEACTED FROM MOVEMENT SPEED TO MOVE THE TILE
                if event.key == pygame.K_UP:  # MOVING P_1 ON Y-CORDINATE
                    if p1_y >= 170:p1_y_change -= speed
                elif event.key == pygame.K_DOWN:
                    if p1_y <= 710:p1_y_change += speed
                elif event.key == pygame.K_w:  # MOVING P_2 ON Y-CORDINATE
                    if p2_y >= 170:p2_y_change -= speed
                elif event.key == pygame.K_s:
                    if p2_y <= 710:p2_y_change += speed
                elif event.key == pygame.K_ESCAPE:pause(var_obj.username)

            if event.type == pygame.KEYUP:  # RELEASING THE KEY
                p1_y_change = 0;p2_y_change = 0

        # player movement
        p1_y += p1_y_change ; p2_y += p2_y_change # MOVING THE TILE
        if p1_y <= 170 or p1_y >= 710:p1_y_change = 0
        if p2_y <= 170 or p2_y >= 710:p2_y_change = 0

        # Ball movement
        if b_x >= 988:b_x = 500;b_y = 400;start = True
        elif b_x <= 12:b_x = 500;b_y = 400;start = True

        if b_y >= 770 or b_y <= 170:b_y_change = -b_y_change  # REVERSING BALL'S DIRECTION ON Y-AXIS

        # CHEKING WHETHER THE BALL HAS COLLIDED WITH THE TILE
        if p1_tile.collidepoint(b_x,b_y) or p2_tile.collidepoint(b_x,b_y) :
            b_x_change = -b_x_change;c = True 
            if disk_rot == True:mixer.Sound('Music\Collide.wav').play()

        run_mul = var_obj.run_mul
        pygame.display.update()  # UPDATING THE SCREEN

# CREATING THE MENU
def menu():

    global run
    global disk_rot
    global click_muted

    # VARIABLES
    run = True
    font_y, font_vel = 600, 15
    play_y, settings_y, about_y, quit_y = 800, 890, 980, 1070
    r, g, b = 0, 0, 0
    b_img_x = -150 ;t_img_x = 1050
    pong_reached = False
    click = False
    disk_rot = True ; click_muted = False

    mixer.music.load('Music\Menu music.mp3')
    mixer.music.play(-1)
    if disk_rot == False : mixer.music.pause() 

    import os
    try:
        if os.path.getsize('User.bin') > 0:
            with open('User.bin','rb') as file:var_obj.username = pickle.load(file)[0] ; file.close() ; var_obj.signed_in = True
    except:pass

    music_rotating_check = 1
    quit_confirmation = False
    count = 1
    final_b_img_x, final_play_y, final_settings_y, final_about_y, final_quit_y = 0, 0, 0, 0, 0
    angle_x = 0
    click_muted = False
    start = time.time() ; start_o = time.time()
    ball_choice = 'Images\Objects\Ball1.png' ; tile_choice = 'Images\Objects\Tile11.png'
    ball_lst = ['Images\Objects\Ball1.png','Images\Objects\Ball2.png', 'Images\Objects\Ball3.png', 'Images\Objects\Ball4.png']
    tile_lst = ['Images\Objects\Tile11.png','Images\Objects\Tile12.png','Images\Objects\Tile21.png','Images\Objects\Tile22.png','Images\Objects\Tile31.png','Images\Objects\Tile32.png','Images\Objects\Tile41.png','Images\Objects\Tile42.png']
    while run:

        mouse = pygame.mouse.get_pos() # GETTING THE MOUSE CORDINATES
        stop = time.time() ; stop_o = time.time()
        bg_img('Images\stars.png', 0, 0) # BG IMAGE
        if stop_o-start_o > 2:
            ball_choice = random.choice(ball_lst)
            tile_choice = random.choice(tile_lst)
            start_o = stop_o

        show_txt('PONG', r, g, b, 150, 300, font_y) # SHOWING THE LOGO

        if count != 1: # SETTING THE TRANSITION FOR THE BALL IMAGE
            play_y, settings_y, about_y, quit_y = final_play_y, final_settings_y, final_about_y, final_quit_y
            show_png_img(ball_choice, final_b_img_x, 350)
            show_png_img(tile_choice, final_t_img_x, 300)

        if disk_rot == False: # ROTATION STOPPED
            show_png_img('Images\Music_icon.png', 925, 725)
            pygame.draw.line(screen, light_red, (925, 725), (975, 775), 5)
        elif disk_rot == True: # ROTATION CONTINUED
            angle_x -= 2
            icon_rot(angle_x)

        # SHOWING THE OBJECTS
        play_command = Button__(360,play_y,280,50,light_pink,med_pink,dark_pink,mouse,click,'PLAY',50).button_blit(quit_confirmation)
        setting_command = Button__(360,settings_y,280,50,light_cyan,med_cyan,dark_cyan,mouse,click,'SETTINGS',50).button_blit(quit_confirmation)
        about_command = Button__(360,about_y,280,50,light_sand,med_sand,dark_sand,mouse,click,'ABOUT',50).button_blit(quit_confirmation)
        quit_command = Button__(360,quit_y,280,50,light_peach,med_peach,dark_peach,mouse,click,'QUIT',50).button_blit(quit_confirmation)

        if quit_confirmation == False and stop-start>2 and click == True:
            if play_command == True:
                if var_obj.signed_in == False:input_screen() # IF THE PLAYER HAS ALREADY SIGNED IN THEN SKIPPING THE LOGIN SCREEN
                else:menu_play_1(var_obj.username) 
            elif setting_command == True:settings()
            elif about_command == True:about()
            elif quit_command == True:quit_confirmation = True
            click = False;start = stop

        # EVENT LOOP
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN: # PRESSING THE MOUSE BUTTON
                # click = True
                if mouse_over(925, 725, 50, 50, mouse):
                    music_rotating_check += 1 ; click = True
                    if music_rotating_check % 2 == 0:pygame.mixer.music.pause();disk_rot = False # MUSIC PAUSED
                    elif music_rotating_check % 2 != 0:mixer.music.unpause();disk_rot = True # MUSIC PLAYED
                        
                elif mouse_over(360, play_y, 280, 50, mouse) or mouse_over(360, settings_y, 280, 50, mouse) or mouse_over(360, about_y, 280, 50, mouse) or mouse_over(360, quit_y, 280, 50, mouse):click = True

                if click == True and click_muted == False: mixer.Sound('Music\Click.wav').play()# PLAYING THE CLICK SOUND

            if event.type == pygame.MOUSEBUTTONUP:click = False

        if quit_confirmation == True: # CONFIRMING IF THE PLAYER WANT TO QUIT THE GAME
            mouse = pygame.mouse.get_pos()
            pygame.draw.rect(screen, (50, 50, 50), (300, 300, 400, 200))
            pygame.draw.rect(screen, (255, 255, 255), (300, 300, 400, 200), 5)
            show_txt('Do you want to quit?', 230, 230, 230, 37, 330, 320)
            quit_yes = Button__(370,410,100,50,light_pink,med_pink,dark_pink,mouse,click,'YES',40).button_blit()
            quit_no = Button__(520,410,100,50,light_cyan,med_cyan,dark_cyan,mouse,click,'NO',40).button_blit()
            if quit_yes == True:sys.exit()
            elif quit_no == True:quit_confirmation = False

        if (r, g, b) <= (220, 220, 220):# FADING IN THE PONG TEXT
                if r <= 255:r += 3
                if g <= 255:g += 3
                if b <= 255:b += 3

        if count == 1:
            # RISING PONG
            if font_y >= 50:
                font_y -= font_vel
                if font_y <= 70:pong_reached = True

            # TRANSITION FOR THE BALL IMAGE
            if pong_reached == True:
                screen.blit(pygame.image.load(ball_choice).convert_alpha(), (b_img_x, 350)) 
                if b_img_x <= 60:b_img_x += 10;final_b_img_x = b_img_x
                screen.blit(pygame.image.load(tile_choice).convert_alpha(), (t_img_x, 300)) 
                if t_img_x >= 600:t_img_x -= 10;final_t_img_x = t_img_x

            # RISING THE BUTTONS
            if pong_reached == True:
                if play_y >= 330:play_y -= 15;final_play_y = play_y
                if settings_y >= 420:settings_y -= 15;final_settings_y = settings_y
                if about_y >= 510:about_y -= 15;final_about_y = about_y
                if quit_y >= 600:quit_y -= 15;final_quit_y = quit_y
                else:count += 1

        run = var_obj.run

        pygame.display.update()

menu()
