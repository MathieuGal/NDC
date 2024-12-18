import pyxel
import sys

# Configurations globales
WINDOW_WIDTH = 128
WINDOW_HEIGHT = 128

ENEMY_BASE_SPEED = 0.4
PLAYER_SPEED_INCREMENT = 0.5

# Probabilités des drops
PROBA_DROP_LIFE = 97  # 3% de chance
PROBA_DROP_MUN = 75   # 25% de chance

# Gameplay
larg_sprite = 8
longeur_sprite = 8
Temps_avant_pick = 150
BULLET_SPEED = 2
INITIAL_PLAYER_SPEED = 1
INITIAL_PLAYER_HEALTH = 5
INITIAL_PLAYER_MUN = 60
MAX_PLAYER_MUN = 60
MAX_PLAYER_HEALTH = 5
FIRE_RATE = 20
WAVE_ENEMY_INCREMENT = 5
ENEMY_SPAWN_DELAY = 30
POWER_UP_SPAWN_TIME = 99999999

# Gestion du mode QWERTY via une option de ligne de commande
QWERTY = '-qw' in sys.argv

#COMMANDES
 ##tirs
TIR_GAUCHE =  pyxel.KEY_A if QWERTY else pyxel.KEY_Q
TIR_DROIT = pyxel.KEY_D
TIR_HAUT = pyxel.KEY_W if QWERTY else pyxel.KEY_Z
TIR_BAS = pyxel.KEY_S
##DEPLACEMENTS
DEPLACEMENT_GAUCHE = pyxel.KEY_LEFT
DEPLACEMENT_DROIT = pyxel.KEY_RIGHT
DEPLACEMENT_HAUT = pyxel.KEY_UP
DEPLACEMENT_BAS = pyxel.KEY_DOWN

#SPRITE
SPRITES = {
    "vaisseau": {"up": (17, 24), "down": (1, 24), "left": (17, 8), "right": (1, 8)},
    "tir": {"up": (48, 8), "down": (48, 8), "left": (48, 8), "right": (48, 8)},
    "ennemis": [(0, 120), (16, 120), (16, 136)],
    "life": (50, 202),
    "mun": (2, 202),
    "life_up": (50,185),
    "mun_up": (2,185),
    "fire_rate_up": (18,185),
    "speed_up": (34,185)
}