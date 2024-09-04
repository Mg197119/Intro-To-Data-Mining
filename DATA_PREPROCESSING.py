import matplotlib.pyplot as plt
from functions import mutationPerSample, samplesPerMutations


def samplesOverMutaions():
    mutations = []
    samples = []

    for sample in range(110):
        mutations.append(mutationPerSample(sample))
        samples.append(sample + 1)

    plt.scatter(samples,mutations)
    plt.xlabel('Samples') 
    plt.ylabel('Number of Mutations')
    plt.show()

def mutationsOverSamples():
    mutations = []
    samplePerMutation =[]

    for mutation in range(1148):
        samplePerMutation.append(samplesPerMutations(mutation))
        mutations.append(mutation)

    plt.scatter(mutations,samplePerMutation)
    plt.xlabel('Mutation') 
    plt.ylabel('number of samples per mutation')
    plt.show()

samplesOverMutaions()
mutationsOverSamples()


