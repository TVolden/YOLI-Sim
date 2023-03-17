import numpy as np

class Rewarder:
    action_illegal = "Illegal"
    action_add = "Add"
    action_remove = "Remove"
    actions = [action_add, action_remove, action_illegal]
    
    def reward(self, action:str, position:int, indications: np.array, terminated: bool, steps:int) -> float:
        pass