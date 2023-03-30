"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    setitems = set(items)
    inventory = {}
    for item in setitems:
        inventory[item] = items.count(item)
    return inventory


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    # iterate over items
    # if item is in inventory, increment
    # else add item to inventory
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    # iterate over items
    # if item is in inventory, decrement if value > 0
    # else do nothing
    for item in items:
        if item in inventory:
            if inventory[item] > 0:
                inventory[item] -= 1
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    # if item is in inventory, remove it
    # else do nothing
    if item in inventory:
        inventory.pop(item)
    return inventory

def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    # create empty list
    # iterate over inventory
    # append (key, value) to list if value > 0
    # return list
    inventory_list = []
    for key, value in inventory.items():
        if value > 0:
            inventory_list.append((key, value))
    return inventory_list
