import csv 
import random

def generate_nodes():
    fields = ['s_no', 'product', 'quantity']

    products = []
    product_set = []
    #generating random nodes with s_no from 0 to 9 and products from 'A' to 'J'
    for i in range(100):
        s_no = random.randint(0, 9)
        product = chr(ord('A')+random.randint(0, 9))
        product_set.append([s_no, product])
    #removing duplicates
    i=0
    while i<len(product_set):
        i+=1
        j = 0
        while(j<len(product_set)-1):
            j+=1
            if (product_set[i] == product_set[j]):
                product_set.remove(product_set[i])
    #generating random quantities for products
    for i in product_set:
        quantity = random.randint(1, 100)
        products.append([i[0], i[1], quantity])
    #writing to csv file
    filename = "digital_twin\\products.csv"
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(products)
    print("products generated")

generate_nodes()

