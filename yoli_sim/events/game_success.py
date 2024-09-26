from yoli_sim.events import Event

class GameSuccessEvent(Event):
    def __init__(self) -> None:
        super().__init__(6)

    def __str__(self):
        return "Game success"