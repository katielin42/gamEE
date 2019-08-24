
class GameState():
    #All states
    stateDict = {
        "Main Menu": 0,
        "Level 1 OverWorld": 1,
        "Level 1 UnderWorld": 2,
        "Death Screen": 3,
        "Win Screen": 4
    }

    stateListArr = [
        "Main Menu",
        "Level 1 OverWorld",
        "Level 1 UnderWorld",
        "Death Screen",
        "Win Screen"
    ]

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

    #Get current state as a dictionary lookup (string type)
    def getDict(self):
        return GameState.stateList[GameState.currentState]

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