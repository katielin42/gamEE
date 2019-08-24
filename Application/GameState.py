
class GameState():
    state = 0
    def __init__(self):
        GameState.state = 0
    def get(self):
        return GameState.state
    def set(self, value = 0):
        GameState.state = value
gameState = GameState()