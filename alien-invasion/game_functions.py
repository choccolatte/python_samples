import sys

import pygame as pg

def check_events(ship):
    '''respond to user's keypresses and mouse evnts'''
    # taken from alien-invasion.py

    for event in pg.event.get():
            if event.type ==pg.QUIT:
                sys.exit()

            elif event.type == pg.KEYDOWN:
                 if event.key == pg.K_RIGHT:
                      #move ship to right
                      ship.moving_right = True

            elif event.type ==pg.KEYUP:
                 if event.key ==pg.K_RIGHT:
                      ship.moving_right = False



def update_screen(ai_settings, screen, ship):
    '''update images on the screen and flip to the new screen'''
    # taken from alien-invasion.py

    screen.fill(ai_settings.bg_color)
    ship.blitme()
        
    #make the most recently drawn screen visible.
    pg.display.flip()