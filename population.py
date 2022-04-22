import random as rand
from individual import Individual


class Population:
    def Calc_Fitness(self):
        self.population_fitness.clear()
        for individual in self.population:
            individual.Fitness(self.target)
            self.population_fitness.append(individual.Get_Fitness())
        
        self.max_fitness = self.Get_Max_Fitness()
        self.average_fitness = self.Get_Average_Fitness()

    def Get_Average_Fitness(self):
        return sum(self.population_fitness) / len(self.population_fitness)

    def Get_Max_Fitness(self):
        max = 0
        for fitness in self.population_fitness:
            if fitness > max:
                max = fitness
        return max

    def Natural_Selection(self):
        self.selected = []
        for _ in range(self.number_of_population):
            self.selected.append(self.acept_reject())
            # fitness = self.population_fitness[i] / self.max_fitness
            # n = int(fitness * 100)
            # for _ in range(n):
            #     self.selected.append(self.population[i])

    def acept_reject(self):
        count = 0
        while(True and count < 10000):
            index = rand.randrange(len(self.population_fitness))
            individual_fitness = self.population_fitness[index]
            r = rand.random()
            if (r <= individual_fitness):
                return self.population[index]
            count += 1


    def Get_Mating_Pool(self):
        for individual in self.selected:
            print(
                f"Genes: {individual.Get_Genes()}, Fitness: {individual.Get_Fitness()}\n")

    def Generate_Generation(self):
        new_generation = []
        new_generation_genes = []
        for i in range(self.number_of_population):
            # Pick a random integer value to determine the parent for crossing / breeding
            a = rand.randrange(len(self.selected))
            b = rand.randrange(len(self.selected))

            partnerA = self.selected[a]
            partnerB = self.selected[b]

            # Create child individual. Since crossover can obtained 2 child here we create 2 child individual.
            child1 = Individual(len(self.target))
            child2 = Individual(len(self.target))
            
            # Get the middle point for crossover
            n = rand.randrange(len(self.target))

            # Crossover the genetics from parent A and B. 
            # First n - 1 genes from partnerA and last n genes from partnerB are taken then combined. 
            # Ex: n = 3
            # A = [a,b,c,d,e]
            # B = [z,x,c,v,b]
            # child = [a,b,c,v,b]
            child1.Crossover(partnerA, partnerB, n)

            # First n - 1 genes from partnerB and last n genes from partnerA are taken then combined. 
            # Ex: n = 3
            # A = [a,b,c,d,e]
            # B = [z,x,c,v,b]
            # child = [z,x,c,d,e]
            child2.Crossover(partnerB, partnerA, n)

            # Mutate some of child the genes based on the mutation rate 
            child1.Mutation(self.mutation_rate)

            child2.Mutation(self.mutation_rate)

            # To get the most unique genes among the child
            if child1.Get_Genes() not in new_generation_genes:
                new_generation.append(child1)
                new_generation_genes.append(child1.Get_Genes())
            if child2.Get_Genes() not in new_generation_genes:
                new_generation.append(child2)
                new_generation_genes.append(child2.Get_Genes())
            
        self.generations += 1

        # Constraints if the number of unique child/new generation is less than the number of population, repopulate 
        # the population with the new generation and pick random n individual from the previous population
        # Else if the number of new generation is the same or bigger then pick number of population individual from the 
        # new generation.
        if len(new_generation) < self.number_of_population:
            self.population = new_generation + list(rand.sample(self.population, self.number_of_population - len(new_generation)))
        else:
            self.population = list(rand.sample(new_generation, self.number_of_population))

    def Get_Population(self):
        populations = []
        for individual in self.population:
            populations.append(individual.Get_Genes())
        return populations


    def Get_Best_Individual(self):
        best_genes = ""
        best_fit = 0.00
        for individual in self.population:
            if individual.Get_Fitness() > best_fit:
                best_fit = individual.Get_Fitness()
                best_genes = individual.Get_Genes()

        if best_genes == self.target:
            self.matching_genes = True

        return best_genes

    def Reach_Target(self):
        return self.matching_genes

    def Current_Generations(self):
        print(f"Generation #{self.generations}\n")
        print(
            f"The current best matching genes: {self.Get_Best_Individual()}\n")
        print(f"Total current population: {len(self.population)}\n")
        print(
            f"Average current fitness: {(sum(self.population_fitness)/len(self.population_fitness)) * 100} %\n")
        print(f"Mutation rate: {self.mutation_rate * 100} %\n\n")
        return {
            "generation": self.generations,
            "best_genes": self.Get_Best_Individual(),
            "total_population": len(self.population),
            "average_fitness": (sum(self.population_fitness)/len(self.population_fitness)) * 100,
            "max_fitness": self.max_fitness * 100,
            "mutation_rate": self.mutation_rate * 100
        }

    def __init__(self, target, n, mutation_rate):
        self.population = []
        self.number_of_population = n
        self.target = target
        self.mutation_rate = mutation_rate
        self.matching_genes = False
        self.population_fitness = []
        self.generations = 1
        self.max_fitness = 0
        self.average_fitness = 0

        for _ in range(self.number_of_population):
            self.population.append(Individual(len(self.target)))

        self.selected = []


# populations = Population("Unicord", 1000, 0.04)

# populations.Calc_Fitness()
# populations.Get_Population()
# populations.Natural_Selection()

# populations.Get_Mating_Pool()

# populations.Generate_Generation()
