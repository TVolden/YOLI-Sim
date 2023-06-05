from abc import ABC, abstractmethod
from yoli_sim.events import Event

class EventLogger(ABC):
    @abstractmethod
    def log(self, event:Event) -> None:
        ...

class EventLogRepository(EventLogger):
    def __init__(self) -> None:
        self.events = []

    def log(self, event: Event) -> None:
        self.events.append(event)