from yoli_sim.events import Event

class GameSelectedEvent(Event):
    def __init__(self, game_id: int) -> None:
        super().__init__(4)
        self.game_id = game_id

    def __str__(self):
        return f"Game selected, game id {self.game_id}"