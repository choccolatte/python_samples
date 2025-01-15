import pygame as pg

class Ship():
    def __init__(self, screen):

        '''initialize the ship and set its starting position'''
        self.screen=screen

        #load the ship image and get its rect.
        self.image = pg.image.load('img/picture.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each  new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #movement flag
        self.moving_right = False


    def update(self):
        '''update ship's position based on movement flag'''
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        '''draw the ship at its curent location'''
        self.screen.blit(self.image, self.rect)