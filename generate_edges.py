import csv 
import random

def generate_edges():
    fields = ['start', 'end', 'distance']

    paths = []
    path_set = []
    #generating random edges with vertices from 0 to 9
    for i in range(100):
        start = random.randint(0, 9)
        end = start
        while(start==end):
            end = random.randint(0, 9)
        path_set.append([start, end])
    #removing duplicate edges
    i=0
    while i<len(path_set):
        i+=1
        j = 0
        while(j<len(path_set)-1):
            j+=1
            if (path_set[i] == path_set[j]):
                path_set.remove(path_set[i])
    #generating random weights for edges
    for i in path_set:
        distance = random.randint(1, 100)
        paths.append([i[0], i[1], distance])
    #writing to csv file
    filename = "digital_twin\\paths.csv"
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(paths)
    print("paths generated")

generate_edges()

