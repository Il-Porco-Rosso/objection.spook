import pgzrun

STATE_MAINMENU = 0
STATE_SCENE1 = 1
STATE_COURTROOM = 2


game_state = STATE_MAINMENU
game_state = input("devtoolgamestatechangerthingythingthing: ")
if game_state != "1" or game_state != "2":
    pass
else:
    game_state = int(game_state)


slasher_placeholder = Actor('slasher_placeholder')
slasher_placeholder.pos = (100,56)

WIDTH = 250
HEIGHT = 250

def draw():
    screen.clear()
    slasher_placeholder.draw()


# ==============================================================================================================================
# ------REMILITARIZED-ZONE-REMILITARIZED-ZONE-REMILITARIZED-ZONE-REMILITARIZED-ZONE-REMILITARIZED-ZONE-REMILITARIZED-ZONE------
# ==============================================================================================================================

jury_credibility = 100
objection = 0


if game_state == STATE_COURTROOM:
    pass
    print("Courtroom time")
    


while game_state == STATE_COURTROOM:
    pass
    break



















def update(dt):
    pass


# Has to be the last line in the file
pgzrun.go()