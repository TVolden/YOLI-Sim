from yoli_sim.events import Event

class TileRemovedEvent(Event):
    def __init__(self, board_position: int) -> None:
        super().__init__(1)
        self.board_position = board_position

    def __str__(self):
        return f"Tile removed from position {self.board_position}"