from yoli_sim.events import Event

class GameDelayedEvent(Event):
    def __init__(self, milliseconds) -> None:
        super().__init__(7)
        self.milliseconds = milliseconds

    def __str__(self):
        return f"Game delayed for {self.milliseconds} ms."