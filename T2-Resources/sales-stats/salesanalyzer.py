# Created by Aidan Lalonde-Novales and Jonathan Pasco-Arnone
# Created Sept 15th 2023
# This program analyzes sales in a seperate file.

import linecache # this library helps me read lines in files

''' PROBLEM 1 FUNCTIONS '''

# opens a salesinfo file, sorts through names, returns number of names
def get_number_purchases(filename):
    name_count = 0
    name_line = 1
    while linecache.getline(filename, name_line) != "":
        linecache.getline(filename, name_line)
        name_line += 6
        name_count += 1
    return name_count

# opens salesinfo file, sorts through costs, returns total cost
def get_total_purchases(filename):
    total_cost = 0
    cost_line = 6
    while linecache.getline(filename, cost_line) != "":
        current_cost = int(linecache.getline(filename, cost_line))
        cost_line += 6
        total_cost += current_cost
    return total_cost

# calls total purchases and number purchases functions to find the average
def get_average_purchases(filename):
    return get_total_purchases(filename) / get_number_purchases(filename)

''' PROBLEM 2 FUNCTIONS '''

# opens salesinfo file, returns amount of customers with the same name
def get_number_customer_purchases(filename, customer):
    name_line = 1
    name_count = 0
    while linecache.getline(filename, name_line) != "":
        if linecache.getline(filename, name_line) == (customer + "\n"):
            name_count += 1
        name_line += 6
    return name_count

# opens salesinfo file, returns the 
def get_total_customer_purchases(filename, customer):
    name_total_cost = 0
    name_line = 1
    while linecache.getline(filename, name_line) != "":
        if linecache.getline(filename, name_line) == (customer + "\n"):
            name_line += 5
            name_total_cost += int(linecache.getline(filename, name_line))
            name_line += 1
        else:
            name_line += 6
    return name_total_cost

# calls number customer purchases and total customer purchases to
# find the average cost of a certain name
def get_average_customer_purchases(filename, customer):
    total_names = get_total_customer_purchases(filename, customer)
    total_cost = get_number_customer_purchases(filename, customer)
    if (total_cost != 0):
        return total_names / total_cost
    else:
        return 0

''' PROBLEM 3 FUNCTIONS '''

# looks into saleinfo file to see which product is the most popular
def get_most_popular_product(filename):
    desktops = 0
    laptops = 0
    tablets = 0
    toasters = 0
    product_line = 2
    while linecache.getline(filename, product_line) != "":
        desktops += int(linecache.getline(filename, product_line))
        product_line += 1
        laptops += int(linecache.getline(filename, product_line))
        product_line += 1
        tablets += int(linecache.getline(filename, product_line))
        product_line += 1
        toasters += int(linecache.getline(filename, product_line))
        product_line += 3
    if desktops == max(desktops, laptops, tablets, toasters):
        return "Desktop"
    elif laptops == max(desktops, laptops, tablets, toasters):
        return "Laptop"
    elif tablets == max(desktops, laptops, tablets, toasters):
        return "Tablet"
    elif toasters == max(desktops, laptops, tablets, toasters):
        return "Toaster"
    else:
        return "Error"