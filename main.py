import pgzrun


WIDTH = 800
HEIGHT = 600


def draw():
    screen.clear()
    screen.draw.circle((400, 300), 30, "white")
    screen.draw.circle((300, 300), 50, "red")
    screen.draw.circle((200, 300), 40, "green")


def update(dt):
    pass


# Has to be the last line in the file
pgzrun.go()
