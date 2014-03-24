import pygame
from pygame.locals import *

class GameEngine():
    """ Manages a stack of GameStates, runs game """
    def __init__(self):
        self.running = True
        self.states = []
        self.add_state(TitleState())
    
    def add_state(self, state):
        """ Adds state to the end of states """
        self.states.append(state)
        self.states[-1].engine = self
    
    def switch_state(self, state):
        """ Changes the top state to state """
        self.states[-1] = state
        self.states[-1].engine = self

    def pop_state(self):
        """ Pops the last state off """
        self.states.pop()

    def state(self):
        return self.states[-1]

class GameState(object):
    """ Base class for all game states """
    def __init__(self):
        print('... GameState created')
        #pass

    def render(self, screen):
        raise NotImplementedError

    def update(self, events):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError

class TitleState(GameState):
    """ Main Title """
    def __init__(self):
        super(GameState, self).__init__()
        print('... TitleState created')

    def render(self, screen):
        raise NotImplementedError
        
    def update(self, events):
        raise NotImplementedError

    def handle_events(self, events):
        """ Pressing any key moves to Menu State """
        for event in events:
            if event.type == KEYDOWN:
                self.engine.running = False
                print('moving to menu state')
                self.engine.switch_state(MenuState())

class MenuState(GameState):
    """ Main Menu """
    def __init__(self):
        super(GameState, self).__init__()
        print('...MenuState created')

    def render(self, screen):
        raise NotImplementedError
        
    def update(self, events):
        raise NotImplementedError

    def handle_events(self, events):
        self.engine.running = False
