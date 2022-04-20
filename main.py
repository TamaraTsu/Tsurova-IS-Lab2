from shutil import ReadError
from population import Population
import json


def main():
    # number_of_population = 400
    # target = "To be or not to be"
    # mutation_rate = 0.01

    result_file = open("Result.txt", "w")
    result = []

    number_of_population = int(input("Please enter number of population: "))
    target = input("Please input your target word: ")
    mutation_rate = float(
        input("Please input mutation rate in decimal value: "))

    # Add constraint that we only look up to 1200th generation.
    max_generation = 1200

    # First initialize population
    population = Population(target, number_of_population, mutation_rate)

    index = 0

    while not population.Reach_Target() and index < max_generation:
        # We count the fitness rate for each individual in the population
        population.Calc_Fitness()

        # We get the information of the current generations
        res = population.Current_Generations()

        # Add the current generation to the result array for later to be saved into file
        result.append(res)

        # Another constraints if the last 4 generations best genes are the same so there's low chance that we could get
        # the target in the next generation, so we break the loop. Means that our initial population can't produce our target genes
        if index >= 5:
            if result[index]["best_genes"] == result[index - 1]["best_genes"] and result[index]["best_genes"] == result[index - 2]["best_genes"] and result[index]["best_genes"] == result[index - 3]["best_genes"]:
                current_best_genes = res["best_genes"]
                print(
                    f"\n\nSorry but we can only find the best match of target: {current_best_genes}\nIt may be that the number of population is to low thus lower variation in the population,\nor the mutation rate is too low or too high!\n")
                break

        index += 1

        # Selection of our population
        population.Natural_Selection()

        # Generate the new generation
        population.Generate_Generation()

    if not population.Reach_Target() and result[-1]["generation"] == 1200:
        current_best_genes = result[-1]["best_genes"]
        print(
            f"Sorry up till the 1200th generation the best genes that have been produced from {number_of_population} genes are: {current_best_genes}\n")
        for item in result:
            result_file.write(str(json.dumps(item, indent=4)) + '\n')
    elif population.Reach_Target():
        no_generation = result[-1]["generation"]
        print(
            f"We have finally obtained individual with genes {target} on the {no_generation}th generation!")
        for item in result:
            result_file.write(str(json.dumps(item, indent=4)) + '\n')

    result_file.close()


if __name__ == "__main__":
    main()
