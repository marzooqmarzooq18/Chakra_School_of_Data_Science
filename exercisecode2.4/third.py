# Function to update inventory after sales
def update_inventory(inventory, sold):
    for item in sold:                       # go through each sold item
        if item in inventory:               # check if it exists in inventory
            inventory[item] = inventory[item] - sold[item]  # reduce stock
    return inventory                        # return updated inventory


# Example
inventory = {'pen': 120, 'notebook': 80, 'bottle': 50, 'bag': 30, 'box': 190}
sold = {'pen': 24, 'notebook': 10, 'bottle': 12, 'box': 60}

print(update_inventory(inventory, sold))