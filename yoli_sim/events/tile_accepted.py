from yoli_sim.events import Event, EventVisitor

class TileAcceptedEvent(Event):
    def __init__(self, board_position: int, value) -> None:
        super().__init__(2)
        self.board_position = board_position
        self.value = value

    def accept(self, visitor: EventVisitor):
        visitor.board_position(self.board_position)
        visitor.value(self.value)

    def __str__(self):
        return f"Tile accepted on position {self.board_position}"