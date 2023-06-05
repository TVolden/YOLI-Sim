from yoli_sim.events import Event, EventVisitor

class TileInsertedEvent(Event):
    def __init__(self, board_position: int, picture) -> None:
        super().__init__(0)
        self.board_position = board_position
        self.picture = picture

    def accept(self, visitor: EventVisitor):
        visitor.board_position(self.board_position)
        visitor.picture(self.picture)

    def __str__(self):
        return f"Tile inserted on position {self.board_position}"