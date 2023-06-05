from yoli_sim.events import Event, EventVisitor

class VariantSelectedEvent(Event):
    def __init__(self, variant_number) -> None:
        super().__init__(8)
        self.variant_number = variant_number

    def accept(self, visitor: EventVisitor):
        visitor.variant_id(self.variant_number)

    def __str__(self):
        return f"Variant selected {self.variant_number}"