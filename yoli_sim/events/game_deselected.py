from yoli_sim.events import Event, EventVisitor

class GameDeselectedEvent(Event):
    def __init__(self) -> None:
        super().__init__(5)

    def accept(self, visitor: EventVisitor):
        ...

    def __str__(self):
        return "Game deselected"