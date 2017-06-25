import csv
import os

# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification

# Displays the inventory.
def display_inventory(inventory):
    inv_items = 0
    print("Inventory:")
    for i in inventory:
        print (str(inventory[i]) + " " + i)
        inv_items += inventory[i]
    print('Total number of items: ' + str(inv_items))



# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory:
            inventory[i] +=1
        else:
            inventory.update({i: 1})
    return inventory


def find_longest_str(list_of_tuples):
    len_key = 0
    for item in list_of_tuples:
        if len(item[1])> len_key:
            len_key=len(item[1]) 
    return len_key


# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    inv_items = 0
    if order is None:
        display_inventory(inv)
    if order == "count,asc":
        sorted_inv_list = sorted([(value, key) for (key, value) in inv.items()])
        print(sorted_inv_list)
        longest_str = find_longest_str(sorted_inv_list)
        print("Inventory")
        print("Count  {:>8s}".format("Item name")) 
        print("-------" + '-' * longest_str)
        for i in sorted_inv_list:
            print(str(i[0]).rjust(5) + " " + str(i[1]).rjust(find_longest_str(sorted_inv_list)))
            inv_items += i[0]
        print('Total number of items: ' + str(inv_items))
    if order == "count,desc":
        sorted_inv_list = sorted([(value, key) for (key, value) in inv.items()])
        reversed_inv_list = list(reversed(sorted_inv_list))
        print(reversed_inv_list)
        longest_str = find_longest_str(reversed_inv_list)
        print("Inventory")
        print("Count  {:>8s}".format("Item name")) 
        print("-------" + '-' * longest_str)
        for i in reversed_inv_list:
            print(str(i[0]).rjust(5) + " " + str(i[1]).rjust(find_longest_str(reversed_inv_list)))
            inv_items += i[0]
        print("-------" + '-' * longest_str)
        print('Total number of items: ' + str(inv_items)) 


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    with open(filename, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            from_csv = (','.join(row))
            list_csv= from_csv.split(',')
            print(list_csv)
            inventory = add_to_inventory(inventory, list_csv)
    return inventory

    

# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    list_to_csv = []
    for i in inventory:
        for j in range(inventory[i]):
            list_to_csv.append(i)
    with open (filename, "w") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter =',')
        spamwriter.writerow(list_to_csv)

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
display_inventory(inv)

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)

print_table(inv, "count,desc")

import_inventory(inv)

print_table(inv, "count,asc")

export_inventory(inv)

import_inventory(inv)

print_table(inv, "count,desc")


