import pygame
from pygame.locals import *
pygame.init() # 初始化 pygame

awindow = pygame.displayer.set_mode((400, 300)) # 新建窗口并设置高和宽

pygame.displayer.set_caption('Hello Pygame') # 设置窗口的标题

import sys # 正确设置关闭按钮
while True:
    for event in pygame.event.get():
        if event.type == quit:
            pygame.quit()
            quit()