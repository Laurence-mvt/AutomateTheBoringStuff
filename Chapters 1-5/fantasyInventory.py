# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f'{k}: {v}')
    print("Total number of items: " + str(item_total))

# displayInventory(stuff)

# add inventory
def addToInventory(inventory, addedItems):
    # iterate over list of addedItems
    for item in addedItems:
        # if item already in inventory, add one to its value
        if item in inventory.keys():
            inventory[item] +=1
        # otherwise, add it to inventory
        else:
            inventory[item] = 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)