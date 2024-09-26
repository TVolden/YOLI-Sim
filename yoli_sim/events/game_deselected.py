from yoli_sim.events import Event

class GameDeselectedEvent(Event):
    def __init__(self) -> None:
        super().__init__(5)

    def __str__(self):
        return "Game deselected"