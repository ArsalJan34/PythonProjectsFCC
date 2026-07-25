inventory = ["Laptop", "mouse", "keyboard", "monitor"]
new_shipment = ["headset","webcam"]
# using extend() to add multipele items from another list
inventory.extend(new_shipment)

# here using insert() to add high priority item at the top (index 0)
inventory.insert(0,"server_rack")

# using append to add single item at end
inventory.append("docking_station")

# usign copy() to keep a backup befroe modifying further
backup_inventory = inventory.copy()

# pop() and remove() using them to process item removals
sold_item = inventory.pop(2) #removes item at index 2
inventory.remove("keyboard")

# using sort() and reverse() - reorder stock alphabatically tehn reverse it
inventory.sort()
print("Reversed inventory:", inventory)

inventory.clear()
print("Cleared inventory:", inventory)
print("Backup remains safe: ", backup_inventory)
