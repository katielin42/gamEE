
class GameState():
    #All states
    stateList = {
        "Main Menu": 0,
        "Level 1 OverWorld": 1,
        "Level 1 UnderWorld": 2,
        "Death Screen": 3,
        "Win Screen": 4
    }

    #States which player has control
    playerHasControlStateList = {
        "Level 1 OverWorld": 1,
        "Level 1 UnderWorld": 2
    }

    #state that indicates if player has control
    playerHasControl = None

    #Current State
    currentState = None

    #state to indicate if the game is running
    isRunning = True

    def __init__(self):
        GameState.currentState = GameState.stateList["Main Menu"]
        playerHasControl = False

    #Get current state
    def get(self):
        return GameState.currentState

    #Set the current state
    def set(self, value = 0):
        #Set the current state
        GameState.currentState = value
        #Find out if the current state implies that the player has control
        playerHasControl = self.doesPlayerHaveControl()

    #Find out if the player has control
    def doesPlayerHaveControl(self):
        for playerControlledState in GameState.playerHasControlStateList:
            if GameState.currentState == playerControlledState:
                return True
        return False

gameState = GameState()