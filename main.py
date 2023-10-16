import pgzrun

STATE_MAINMENU = 0
STATE_SCENE1 = 1
STATE_COURTROOM = 2


game_state = STATE_MAINMENU


slasher_placeholder = Actor('slasher_placeholder')
slasher_placeholder.pos = (100,56)

WIDTH = 1000
HEIGHT = slasher_placeholder.height + 20

def draw():
    screen.clear()
    slasher_placeholder.draw()


# ==============================================================================================================================
# ------REMILITARIZED-ZONE-REMILITARIZED-ZONE-REMILITARIZED-ZONE-REMILITARIZED-ZONE-REMILITARIZED-ZONE-REMILITARIZED-ZONE------
# ==============================================================================================================================

jury_credibility = 100


if game_state == STATE_COURTROOM:
    pass
    print("Courtroom time")
    


while game_state == 2:
    pass
    break



















def update(dt):
    pass


# Has to be the last line in the file
pgzrun.go()