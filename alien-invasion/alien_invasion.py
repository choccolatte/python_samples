import pygame as pg
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #initialize game, settings and create a screen object

    pg.init()
    ai_settings=Settings()
    screen = pg.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pg.display.set_caption('Alien Invasion')

    #make a ship using degined ship
    ship = Ship(ai_settings, screen)

    #setting background color
    bg_color= (94, 104, 109)

    #Start the main loop for the game
    while True:
        # Watch for keyboard and mouse events

        gf.check_events(ship)

        #call update function on each pass through
        ship.update()
        
        #redraw the screen during each pass through the loop
        gf.update_screen(ai_settings, screen, ship)      

run_game()
