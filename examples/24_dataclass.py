# https://docs.python.org/3/library/dataclasses.html
# https://www.youtube.com/watch?v=CvQ7e6yUtnw

from dataclasses import dataclass 

@dataclass 
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand

item = InventoryItem(name="Tardis", unit_price=42.0, quantity_on_hand=42)
print(item)
print(item.total_cost())

item2 = InventoryItem(name="Tardis", unit_price=42.0, quantity_on_hand=42)
print(item == item2) # True

item3 = InventoryItem(name="Tardis", unit_price=44.0, quantity_on_hand=2)
print(item == item3) # False
