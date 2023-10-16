import pgzrun

STATE_MAINMENU = 0
STATE_SCENE1 = 1
STATE_COURTROOM = 2


game_state = STATE_MAINMENU







# ==============================================================================================================================
# ------DEMILITARIZED-ZONE-DEMILITARIZED-ZONE-DEMILITARIZED-ZONE-DEMILITARIZED-ZONE-DEMILITARIZED-ZONE-DEMILITARIZED-ZONE------
# ==============================================================================================================================

jury_credibility = 100


if game_state == STATE_COURTROOM:
    pass
    print("Courtroom time")
    


while game_state == 2:
    pass
    break


















saul = Actor('saul')

WIDTH = 1000
HEIGHT = saul.height + 20

def draw():
    screen.clear()
    saul.draw()

def update(dt):
    pass


# Has to be the last line in the file
pgzrun.go()