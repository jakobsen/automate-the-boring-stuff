import math


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    most_digits = 0
    for v in inventory.values():
        digits = math.log10(v) + 1
        if digits > most_digits:
            most_digits = digits

    for k, v in inventory.items():
        print(str(v).ljust(int(most_digits) + 1) + str(k))
        item_total += v
    print("Total number of items: " + str(item_total))


def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


inv = {'gold coin': 101, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inv, dragonLoot)
displayInventory(inv)
