import random as rand
import string

class Individual:
    def Get_Genes(self):
        return self.genes

    def Get_Fitness(self):
        return self.fitness

    def Fitness(self, target):
        score = 0
        for char_genes, char_target in zip(self.genes, target):
            if (char_genes == char_target):
                score += 1
        
        self.fitness = score / self.length

    def Crossover(self, partnerA, partnerB, midPoint):
        mid_point = midPoint
        genes_a = partnerA.Get_Genes()
        genes_b = partnerB.Get_Genes()
        which_child = rand.randint(0,1)
        self.genes = genes_a[:mid_point] + genes_b[mid_point:]
        # if which_child == 1:
        #     self.genes = genes_a[:mid_point] + genes_b[mid_point:]
        # elif which_child == 2:
        #     self.genes = genes_b[:mid_point] + genes_a[mid_point:]

    def Mutation(self, mutation_rate):
        for item in self.genes:
            if rand.uniform(0.00, 1.00) < mutation_rate:
                item = self.get_char()

    def get_char(self):
        return rand.choice(string.ascii_letters + ' ' + '.')

    def __init__(self, length):
        self.length = length
        self.genes = ''.join(self.get_char() for _ in range(self.length))
        self.fitness = 0


# individual = Individual(6)
# print(individual.Get_Genes())
# individual.Fitness("ASdasa")
# print(individual.Get_Fitness())
