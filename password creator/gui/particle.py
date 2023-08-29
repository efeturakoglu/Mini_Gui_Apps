import pygame as pg
import random



def circle_surf(radius, color):
    surf = pg.Surface((radius * 2, radius * 2))
    pg.draw.circle(surf, color, (radius, radius), radius)
    surf.set_colorkey((0, 0, 0))
    return surf

def add_particle(screen,counter,color = (255,255,255),color2 = (20, 20, 60),moving = True,volume = 20,particles = [],scroll = (0,0),backrad = 2):
    if counter >= volume:
        particles.append([[random.randint(0,1000),random.randint(0,500)], [random.randint(0, 2) / 1.5 - 1, -5], random.randint(1, 2)])
        counter = 0
    

    for particle in particles:
        if moving:
            particle[0][0] -= 1 
            particle[0][1] += 1
            particle[2] -= 0.008
            particle[1][1] += 0

        pg.draw.circle(screen, color, [int(particle[0][0])-scroll[0], int(particle[0][1])-scroll[1]], int(particle[2]))

        radius = particle[2] * backrad
        screen.blit(circle_surf(radius, color2), (int(particle[0][0] - radius)-scroll[0], int(particle[0][1] - radius)-scroll[1]), special_flags=pg.BLEND_RGB_ADD)

        if particle[2] <= 0:
            particles.remove(particle)


