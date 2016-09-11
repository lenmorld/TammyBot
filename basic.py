from rrb3 import *
import pygame
import sys
import time
from pygame import mixer
from pygame.locals import *
import RPi.GPIO as GPIO


# setup rrb3 with 6 * 1.5 V
rr = RRB3(9, 6)


pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('TammyBot v2')
pygame.mouse.set_visible(0)

while True:
    for event in pygame.event.get():
        if (event.type == QUIT):
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_e:
                rr.forward()
                rr.set_led1(True)
                rr.set_led2(True)
            elif event.key == K_d:
                rr.set_led1(True)
                rr.set_led2(True)
                rr.reverse()
            elif event.key == K_f:
                rr.set_led1(False)
                rr.set_led2(True)
                rr.right()
            elif event.key == K_s:
                rr.set_led1(False)
                rr.set_led2(True)
                rr.left()
            elif event.key == K_SPACE:
                rr.stop()
                rr.set_led1(False)
                rr.set_led2(False)
