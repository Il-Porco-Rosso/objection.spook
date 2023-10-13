import pgzrun


WIDTH = 800
HEIGHT = 600

saul = Actor('saul')
WIDTH = 500
HEIGHT = saul.height + 20

def draw():
    screen.clear()
    saul.draw()

def update(dt):
    pass


# Has to be the last line in the file
pgzrun.go()
