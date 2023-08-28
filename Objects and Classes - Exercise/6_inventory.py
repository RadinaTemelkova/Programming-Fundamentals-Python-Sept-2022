class Inventory:
    def __init__ (self, __capacity: int):
        self.__capacity = __capacity
        self.items = []

    def add_item(self, item: str):

        if len(self.items) < self.__capacity:
            self.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        capacity_left = self.__capacity - len(self.items)
        items = ", ".join(self.items)
        return f"Items: {items}.\nCapacity left: {capacity_left}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
