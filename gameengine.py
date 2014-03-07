import pygame
from pygame.locals import *

class GameEngine(object):
""" Manages a stack of GameStates, runs game """
	def __init__():
		self.running = True
		self.states = []
		self.add_state(TitleState())
	
	def add_state(self, state):
		""" Adds state to the end of states """
		self.states.append(state):
		self.states[-1].engine = self
	
	def switch_state(self, state):
		""" Changes the top state to state """
		self.states[-1] = state
		self.states[-1] = self

	def pop_state(self):
		""" Pops the last state off """
		self.states.pop()

	def state(self):
		return self.states[-1]

class GameState(object):
	""" Base class for all game states """
	def __init__(self):
		pass

	def render(self, screen):
		raise NotImplementedError

	def update(self, events):
		raise NotImplementedError

	def handle_events(self, events):s
		raise NotImplementedError

	
