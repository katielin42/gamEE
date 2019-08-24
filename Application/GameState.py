
class GameState():
    value = 0
    def __init__(self):
        GameState.value = 0
    def get(self):
        return GameState.value
    def set(self, value = 0):
        GameState.value = value
gameState = GameState()