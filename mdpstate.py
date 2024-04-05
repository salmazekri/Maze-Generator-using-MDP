

class MDPState:

    def __init__(self, up, down, left, right, reward=-1, value=0):
        self.up = up
        self.down = down
        self.right = right
        self.left = left
        
        self.reward = reward
        self.value = value

    def __str__(self):
        return str(self.value)