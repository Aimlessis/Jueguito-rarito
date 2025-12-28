import pygame as pgame
import playerclass as player

pgame.init()
sprite = ""
playerpos_X = 0 
playerpos_y = 0
collisionsize = {50, 50}
pepito = player()
displayres_w = 500
displayres_h = 800

background_color = 66, 141, 245

running = True


display = pgame.display.set_mode((displayres_w, displayres_h))



while running:
    for event in pgame.event.get():
        if event == pgame.QUIT:
            running = False


    display.fill(background_color)
    pgame.display.flip()

pgame.quit()

print("hola pe!")