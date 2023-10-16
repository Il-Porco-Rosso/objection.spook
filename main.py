import pgzrun


game_state = 1

if game_state == 1:
    pass
while game_state == 1:
    pass





# ==============================================================================================================================
# ------DEMILITARIZED-ZONE-DEMILITARIZED-ZONE-DEMILITARIZED-ZONE-DEMILITARIZED-ZONE-DEMILITARIZED-ZONE-DEMILITARIZED-ZONE------
# ==============================================================================================================================

if game_state == 2:
    pass
while game_state == 2:
    pass

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