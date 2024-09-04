import csv
import re

filename = 'mutations.csv'

fields =[]
rows =[]

csvFile = open(filename ,'r')

csvreader = csv.DictReader(csvFile)

data_list = []

    
for row in csvreader:
    data_list.append(row)


print("Total number of genes: %d" % (len(data_list[0]) - 1))

print("Total number of samples: %d" % (len(data_list)))


def mutationPerSample (sample):
    mutationCount = 0
    for key in data_list[sample]:
        value = data_list[sample][key]
        if value == '1':
            mutationCount += 1
    return mutationCount

print(f"Number of mutations for individual C1: {mutationPerSample(0)}")
mutationCount = 0    

for key in data_list[4]:
    value = data_list[4][key]
    if value == '1':
        mutationCount += 1

print(f"Number of mutations for individual NC1: {mutationCount}")


for individual in range(len(data_list)):
    for key in data_list[individual]:
        value = data_list[individual][key]
        if value == '1':
            mutationCount += 1
average_mutation_count = mutationCount / (len(data_list))

print(f"Average number of mutations: {average_mutation_count}")

mutationCount = 0

BRAF = r'^BRAF'
KRAS = r'^KRAS'

for individual in range(len(data_list)):
    for key in data_list[individual]:
        value = data_list[individual][key]
        if re.match(BRAF,key) and value == '1':
            mutationCount +=1
mutationCount = 0
print(f"Number of individuals who have a mutation in the ‘BRAF’ gene: {mutationCount}")

for individual in range(len(data_list)):
    for key in data_list[individual]:
        value = data_list[individual][key]
        if re.match(KRAS,key) and value == '1':
            mutationCount +=1

mutationCount = 0

print(f"Number of individuals who have a mutation in the ‘KRAS’ gene: {mutationCount}")


for individual in range(len(data_list)):
    for key in data_list[individual]:
        value = data_list[individual][key]
        if value == '1':
            mutationCount += 1

average_number_of_individuals_per_mutation =  mutationCount / len(data_list[0])
print (f"Number of mutations total: {average_number_of_individuals_per_mutation}")


def samplesPerMutations(mutationIndex):
    mutationCount = 0
    for individual in range(len(data_list)):
        value = data_list[individual][mutationIndex]
        if value == '1':
            mutationCount +=1
    return mutationCount
    
