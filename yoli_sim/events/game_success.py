from yoli_sim.events import Event, EventVisitor

class GameSuccessEvent(Event):
    def __init__(self) -> None:
        super().__init__(6)

    def accept(self, visitor: EventVisitor):
        ...

    def __str__(self):
        return "Game success"