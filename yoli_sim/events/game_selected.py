from yoli_sim.events import Event, EventVisitor

class GameSelectedEvent(Event):
    def __init__(self, game_id: int) -> None:
        super().__init__(4)
        self.game_id = game_id

    def accept(self, visitor: EventVisitor):
        visitor.game_id(self.game_id)

    def __str__(self):
        return f"Game selected, game id {self.game_id}"