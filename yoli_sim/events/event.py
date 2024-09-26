from abc import ABC, abstractmethod

class Event(ABC):
    def __init__(self, event_number) -> None:
        super().__init__()
        self._event_number = event_number

    @property
    def event_number(self) -> int:
        return self._event_number

    @abstractmethod
    def __str__(self):
        ...