#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  Main Game

import pygame as pg
import sys, os, random
from settings import *


class Game:
	def __init__(self):
		#  Initialize game window, etc
		pg.init()
		pg.mixer.init()
		self.screen = pg.display.set_mode((WIDTH, HEIGHT))
		pg.display.set_caption('The Game')
		self.clock = pg.time.Clock()
		self.running = True
		
	def new(self):
		#  Start a new game
		self.all_sprites = pg.sprite.Group()
		self.run()
		
	def run(self):
		#  Game loop
		self.playing = True
		while self.playing:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()
		
	def events(self):
		#  Game loop - Events
		for event in pg.event.get():
			#  Check for closing the window
			if event.type == pg.QUIT:
				if self.playing:
					self.playing = False
				self.running = False
		
	def update(self):
		#  Game loop - Update
		self.all_sprites.update()
		
	def draw(self):
		#  Game loop -Draw
		self.screen.fill(BLACK)
		self.all_sprites.draw(self.screen)
		#  *after* drawing everything, flip the display
		pg.display.flip()
		
	def show_start_screen(self):
		#  Start screen
		pass
		
	def show_go_screen(self):
		#  Game Over screen
		pass
		

g = Game()
g.show_start_screen()
while g.running:
	g.new()
	g.show_go_screen()
	
pg.quit()
sys.exit()

