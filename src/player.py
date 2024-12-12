import pyxel
from config import *

class Player:
    def __init__(self):
        self.vaisseau = [60, 60]
        self.vies = INITIAL_PLAYER_HEALTH
        self.vies_max = MAX_PLAYER_HEALTH
        self.mun = INITIAL_PLAYER_MUN
        self.mun_max = MAX_PLAYER_MUN
        self.speed = INITIAL_PLAYER_SPEED  
        self.timer = 0
        self.t = FIRE_RATE
        self.current_direction = "up"
        

    def deplacement(self):
        keys = [pyxel.KEY_UP, pyxel.KEY_DOWN, pyxel.KEY_LEFT, pyxel.KEY_RIGHT]
        self.pressed_keys = [key for key in keys if pyxel.btn(key)]
        if pyxel.btn(pyxel.KEY_RIGHT) and self.vaisseau[0] < 120 and len(self.pressed_keys) == 1:
            self.vaisseau[0] += self.speed
            self.current_direction = "right"
        if pyxel.btn(pyxel.KEY_LEFT) and self.vaisseau[0] > 0 and len(self.pressed_keys) == 1:
            self.vaisseau[0] -= self.speed
            self.current_direction = "left"
        if pyxel.btn(pyxel.KEY_DOWN) and self.vaisseau[1] < 120 and len(self.pressed_keys) == 1:
            self.vaisseau[1] += self.speed
            self.current_direction = "down"
        if pyxel.btn(pyxel.KEY_UP) and self.vaisseau[1] > 0 and len(self.pressed_keys) == 1:
            self.vaisseau[1] -= self.speed
            self.current_direction = "up"
        else :
            if pyxel.btn(pyxel.KEY_RIGHT) and self.vaisseau[0] < 120 and len(self.pressed_keys) >= 2:
                self.vaisseau[0] += self.speed / 1.5
                self.current_direction = "right"
            if pyxel.btn(pyxel.KEY_LEFT) and self.vaisseau[0] > 0 and len(self.pressed_keys) >= 2:
                self.vaisseau[0] -= self.speed / 1.5
                self.current_direction = "left"
            if pyxel.btn(pyxel.KEY_DOWN) and self.vaisseau[1] < 120 and len(self.pressed_keys) >= 2:
                self.vaisseau[1] += self.speed / 1.5
                self.current_direction = "down"
            if pyxel.btn(pyxel.KEY_UP) and self.vaisseau[1] > 0 and len(self.pressed_keys) >= 2:
                self.vaisseau[1] -= self.speed / 1.5
                self.current_direction = "up"


    def tirs_creation(self, projectile_manager):
        self.timer -= 1
        if self.timer <= 0 and self.mun > 0:
            if pyxel.btnr(pyxel.KEY_Z):
                projectile_manager.tirs_liste[0].append([self.vaisseau[0] + 3, self.vaisseau[1] - 4])
                self.timer += self.t
                self.mun -= 1
            elif pyxel.btnr(pyxel.KEY_S):
                projectile_manager.tirs_liste[1].append([self.vaisseau[0] + 3, self.vaisseau[1] + 8])
                self.timer += self.t
                self.mun -= 1
            elif pyxel.btnr(pyxel.KEY_Q):
                projectile_manager.tirs_liste[2].append([self.vaisseau[0] - 4, self.vaisseau[1] + 3])
                self.timer += self.t
                self.mun -= 1
            elif pyxel.btnr(pyxel.KEY_D):
                projectile_manager.tirs_liste[3].append([self.vaisseau[0] + 8, self.vaisseau[1] + 3])
                self.timer += self.t
                self.mun -= 1

    def draw(self):
        if self.vies > 0:
            sprite_x, sprite_y = SPRITES["vaisseau"][self.current_direction]
            pyxel.blt(self.vaisseau[0], self.vaisseau[1], 0, sprite_x, sprite_y, 15, 15, 5)