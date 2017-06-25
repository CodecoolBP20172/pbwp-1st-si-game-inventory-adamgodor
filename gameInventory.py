# -*- coding: UTF-8 -*-
def display_inventory(inventory):
    print("Invetory")
    for key, value in inventory.items():
        print (str(value) + " " + key)
    item_count = list(inventory.values())
    print("Total number of items: %d" % sum(item_count))


def add_to_inventory(inventory, added_items):
    # if the key exist, add one to the value
    for x in added_items:
        if x in inventory:
            a = inventory.get(x)
            a += 1
            inventory[x] = a
    # if the key not exist create the key
        else:
            inventory.update({x: 1})
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
    longest_item = len(max(inventory.keys(), key=len))
    if order == "unordered":
        ordered_list = inventory.items()
    if order == "count,desc":
        ordered_list = sorted(inventory.items(), key=lambda inventory: inventory[1], reverse=1)
    if order == "count,asc":
        ordered_list = sorted(inventory.items(), key=lambda inventory: inventory[1], reverse=0)
    # make the ordered / unordered table

    def make_order(ordered_list):
        print("Inventory:")
        print("Count".rjust(bigest_number) + "   " + "Item name".rjust(longest_item))
        print('-' * (bigest_number + longest_item + 3))
        for key, value in ordered_list:
            print(str(value).rjust(bigest_number) + "   " + key.rjust(longest_item))
        print('-' * (bigest_number + longest_item + 3))
        item_count = list(inventory.values())
        print("Total number of items: %d" % sum(item_count))
    # the main program
    if order == "unordered":
        make_order(ordered_list)
    elif order == "count,desc":
        make_order(ordered_list)
    elif order == "count,asc":
        make_order(ordered_list)


def import_inventory(inventory, file_name="test_inventory.csv"):
    # open a file
    additional_loot = open(file_name), "r")
    cont=additional_loot.read().strip().rstrip(",").split(",")  # remove \n, remove trailing coma
    cont=[x.strip(' ')for x in cont]  # remove whitespaces
    cont=[x.strip('\t')for x in cont]  # remove tabs
    added_items=cont
    # run the add_to_inventory function
    add_to_inventory(inventory, added_items)
    additional_loot.close()
    return inventory

def export_inventory(inventory, filename = "test_inventory_export.csv"):
    file=open(file_name, "w")
    # make a list of list out of the inventory
    raw_item_list=[]
    for key, value in inventory.items():
        raw_item_list.append(key.split(",") * value)
    # convert the list of list into a single list
    single_list=[]
    for item in raw_item_list:
        for l in item:
            single_list.append(l)
    # convert the single list into a string separated by comas
    items_in_string=",".join(single_list)
    file.write(items_in_string)
    file.close()
