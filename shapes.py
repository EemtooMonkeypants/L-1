import pgzrun
WIDTH = 600
HEIGHT = 600
def draw():
    screen.fill((215, 252, 249))
    r1 = Rect(300, 200, 20, 50)
    #screen.draw.rect(r1, "purple")
    screen.draw.filled_rect(r1, "green")
    w = 210
    h = 210
    r = 210
    g = 12
    b = 251
    for i in range(20):
        r2 = Rect(0, 0, w, h)
        r2.center = 300, 300
        screen.draw.rect(r2, (r, g, b))
        w = w - 10
        h = h - 10
        r = r - 10
        g = g + 10
        b = b - 10
def update():
    pass
pgzrun.go()