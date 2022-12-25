from tkinter.font import BOLD
import pygame
from pygame.locals import *
from tkinter import *
import tkinter as tk
import math
import os

length = 50

pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 450

def change_pendulam_length(var):
    global length
    length = int(length_slider.get()) * 50
    length_label.config(text=str(length/500) + "m")

def change_gravity(var):
    global GRAVITY
    GRAVITY = int(gravity_slider.get())/1000000

root = Tk()
embed = Frame(root, width=640, height=480)
embed.grid(row=0,column=2)

length_title = Label(embed, text="Length", font='Helvetica 15 bold', relief='solid', padx=10, pady=5).pack()

x = globals()["length"]
length_label = Label(embed, text=str(x/500) + "m", font=("Helvetica", 10), bd=5, relief="sunken")
length_label.pack()

length_slider = Scale(embed, from_=1, to=10, orient=HORIZONTAL, command=change_pendulam_length)
length_slider.pack()


gravity_title = Label(embed, text="Gravity", font='Helvetica 15 bold', relief='solid', padx=10, pady=5).pack(pady=50)


gravity_slider = Scale(embed, from_=0, to=50, orient=HORIZONTAL, command=change_gravity)
gravity_slider.pack()
gravity_slider.set(10)

os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'


pygame.display.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Simple Pendulam")
pygame.display.flip()

PI = 3.14159
GRAVITY = 0.000001

origin = [WINDOW_WIDTH//2, 0]
bob = [WINDOW_WIDTH//2, length]
angle = PI/5
aVel = 0.0
aAcc = 0.0

while True:
    is_doublecliked = False
    mouse_x, mouse_y = pygame.mouse.get_pos()
    window.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                is_doublecliked = True
        if event.type == pygame.MOUSEBUTTONUP:
            is_doublecliked = False

    bob[0] = origin[0] + length * math.sin(angle)
    bob[1] = origin[1] + length * math.cos(angle)
        
    pygame.draw.line(window, (0, 0, 0), (origin[0], origin[1]), (bob[0], bob[1]))
    pygame.draw.circle(window, (0, 0, 0), (bob[0], bob[1]), 20)

    force = (GRAVITY * math.sin(angle) * -1)/(length/50)
    aAcc = force

    aVel += aAcc
    angle += aVel

    root.update()
    pygame.display.flip()