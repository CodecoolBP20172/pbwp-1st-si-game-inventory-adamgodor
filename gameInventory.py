
def display_inventory(inventory):
    print("Invetory")
    for key,value in inventory.items():
        print (str(value)+" " + key)
    item_count = list(inventory.values())
    print("Total number of items: %d" % sum(item_count))



def add_to_inventory(inventory, added_items):
    for x in added_items:
        if x in inventory:
            a = inventory.get(x)
            a +=1
            inventory[x] = a
        else:
            inventory.update({x:1})
    return inventory



def print_table(inventory, order="unordered"):
    # make sure the table is organised, even if there is a high item number, like a million gold coin
    a = len(str(max(list(inventory))))
    b = len("count")
    if a <= b:
        bigest_number = b
    else:
        bigest_number = a
    # define variables
    longest_item = len(max(inventory.keys(), key =len))
    if order == "unordered":
        ordered_list= inventory.items()
    if order == "count,desc":
        ordered_list = sorted(inventory.items(), key= lambda inventory: inventory[1], reverse = 1)
    if order == "count,asc":
        ordered_list = sorted(inventory.items(), key= lambda inventory: inventory[1], reverse = 0)
    # make the ordered / unordered table
    def make_order(ordered_list):
        print("Inventory:")
        print("Count".rjust(bigest_number)+"   "+"Item name".rjust(longest_item))
        print('-'*(bigest_number+longest_item+3))
        for key,value in ordered_list:
            print(str(value).rjust(bigest_number)+"   "+key.rjust(longest_item))
        print('-'*(bigest_number+longest_item+3))
        item_count = list(inventory.values())
        print("Total number of items: %d" % sum(item_count))
    # the main program
    if order == "unordered":
        make_order(ordered_list)
    elif order == "count,desc":
        make_order(ordered_list)
    elif order == "count,asc":
        make_order(ordered_list)

def import_inventory(inventory, filename="import_inventory.csv"):
    pass

# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    pass
