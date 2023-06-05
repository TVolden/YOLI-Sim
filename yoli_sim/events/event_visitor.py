from abc import ABC, abstractmethod

class EventVisitor(ABC):
    def board_position(self, position:int) -> None:
        ...

    def game_id(self, id:int) -> None:
        ...

    def milliseconds(self, milliseconds) -> None:
        ...

    def variant_id(self, number) -> None:
        ...

    def picture(self, picture) -> None:
        ...

    def value(self, value) -> None:
        ...