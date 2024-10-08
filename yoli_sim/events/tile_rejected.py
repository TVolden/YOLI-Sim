from yoli_sim.events import Event

class TileRejectedEvent(Event):
    def __init__(self, board_position: int) -> None:
        super().__init__(3)
        self.board_position = board_position

    def __str__(self):
        return f"Tile rejected on position {self.board_position}"