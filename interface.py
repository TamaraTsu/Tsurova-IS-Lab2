from tkinter import *
from tkinter import messagebox
from population import Population
from matplotlib import pyplot as plt
import json


class App:
    def genetic_algorithm(self):
        result_text = ""
        image = ""
        json_file = open("Result.json", "w")
        # For console app
        # number_of_population = int(input("Please enter number of population: "))
        # target = input("Please input your target word: ")
        # mutation_rate = float(
        #     input("Please input mutation rate in decimal value: "))

        # Add constraint that we only look up to 1000th generation.
        max_generation = 1000

        # First initialize population
        population = Population(
            self.target, self.number_of_population, self.mutation_rate)

        index = 0

        while not population.Reach_Target() and index < max_generation:
            # We count the fitness rate for each individual in the population
            population.Calc_Fitness()

            # We get the information of the current generations
            res = population.Current_Generations()
            self.average_fitness_res.append(res["average_fitness"])
            self.max_fitness_res.append(res["max_fitness"])
            self.generation_res.append(res["generation"])

            self.show_information(res["best_genes"], res["generation"], res["total_population"],
                                  res["average_fitness"], res["max_fitness"], res["mutation_rate"])
            # self.add_list(population.Get_Population())
            self.add_list(res["best_genes"])

            # Add the current generation to the result array for later to be saved into file
            self.result.append(res)

            # Another constraints if the last 4 generations best genes are the same so there's low chance that we could get
            # the target in the next generation, so we break the loop. Means that our initial population can't produce our target genes
            if index >= 5:
                if self.result[index]["best_genes"] == self.result[index - 1]["best_genes"] and self.result[index]["best_genes"] == self.result[index - 2]["best_genes"] and self.result[index]["best_genes"] == self.result[index - 3]["best_genes"]:
                    current_best_genes = res["best_genes"]
                    result_text = f"Sorry but we can only find the best match of target: {current_best_genes}\nIt may be that the number of population is to low thus lower variation in the population,\nor the mutation rate is too low or too high!\n"
                    print("\n\n" + result_text)
                    image = ""  # Need to add image here for popup window
                    break

            index += 1

            # Selection of our population
            population.Natural_Selection()

            # Generate the new generation
            population.Generate_Generation()

            self.window.update()

        if not population.Reach_Target() and self.result[-1]["generation"] == 1200:
            current_best_genes = self.result[-1]["best_genes"]
            result_text = f"Sorry up till the 1200th generation the best genes that have been produced from {self.number_of_population} genes are: {current_best_genes}\n"
            image = ""  # Need to add image here for popup window
            print(result_text)
        elif population.Reach_Target():
            no_generation = self.result[-1]["generation"]
            result_text = f"We have finally obtained individual with genes {self.target} on the {no_generation}th generation!"
            image = ""  # Need to add image here for popup window
            print(result_text)

        json.dump(self.result, json_file, indent=4)

        # messagebox.showinfo("Result", result_text)
        self.messageWindow(result_text, image)

        # self.draw_graph()

        json_file.close()

    def run_algorithm(self):
        self.number_of_population = int(self.input_population.get())
        self.target = self.input_target.get()
        self.mutation_rate = float(self.input_mutation_rate.get())
        self.population_listbox.delete(0, END)
        self.run_button.config(state=DISABLED)
        self.genetic_algorithm()
        self.run_button.config(state=NORMAL)

    def show_information(self, best_genes, number_generation, population, average_fitness, max_fitness, mutation_rate):
        self.best_genes_label.configure(text=str(best_genes))
        self.generation_label.configure(
            text="Generation #" + str(number_generation))
        self.population_label.configure(
            text="Total individual in population : " + str(population))
        self.average_fitness_label.configure(
            text="Average fitness : " + str(average_fitness))
        self.max_fitness_label.configure(
            text="Maximum fitness : " + str(max_fitness))
        self.mutation_rate_label.configure(
            text="Mutation rate : " + str(mutation_rate))

    def add_list(self, generated_individuals):
        self.population_listbox.insert(0, generated_individuals)
        # for individual  in generated_individuals:
        #     self.population_listbox.insert(0, individual)

    def messageWindow(self, result_message, image):
        win = Toplevel()
        win.title("Result")
        # Need to add image here and add icon
        Label(win, text=result_message).pack()
        Button(win, text="Ok, show graph!", command=lambda:[win.destroy(), self.draw_graph()]).pack()

    def draw_graph(self):
        # average_fitness = []
        # max_fitness = []
        # generation = []
        # for res in self.result:
        #     generation.append(res["generation"])
        #     average_fitness.append(res["average_fitness"])
        #     max_fitness.append(res["max_fitness"])
        plt.figure().set_size_inches(13, 8)
        plt.plot(self.generation_res, self.max_fitness_res, color='#820401', linestyle='-', marker='o', label='Максимальный фитнесс в поколении')
        plt.plot(self.generation_res, self.average_fitness_res, color='#29066B', linestyle='--', marker='o', label='Средний фитнесс в поколении')
        plt.xticks(self.generation_res)
        plt.yticks([(index + 1) * 5 for index in range(20)])
        plt.xlabel("Поколение")
        plt.ylabel("Фитнесс оценки (%)")
        plt.legend(loc='lower center')
        plt.title('Genetic algorithm')
        plt.text(2000, 2000, "This is text", fontsize=14)
        plt.grid()
        plt.show()

    def __init__(self):
        self.window = Tk()
        self.window.title("Genetic Algorithm")
        self.window.geometry("600x350")
        self.window.resizable(False, False)
        self.window.iconbitmap("geneicon.ico")

        ### VIEW ###

        # Left frame for information
        self.frame = LabelFrame(self.window, width=300,
                                height=250, bg="#465B75", bd=1, relief=FLAT)
        self.frame.place(x=0, y=0)
        self.frame.propagate(0)

        # All labels
        self.label1 = Label(self.frame, text='The Best Genes:', font=20,
                            background="#465B75")
        self.label1.pack(side=TOP, anchor="w")

        self.best_genes_label = Label(self.frame, text='To be or not to be', font=20,
                                      background="#465B75")
        self.best_genes_label.pack(pady=(0, 10), side=TOP, anchor="w")

        self.generation_label = Label(self.frame, text='Generation #0', font=20,
                                      background="#465B75")
        self.generation_label.pack(side=TOP, anchor="w")

        self.population_label = Label(self.frame, text='Total individual in population n : ' +
                                      '0', font=20,
                                      background="#465B75")
        self.population_label.pack(side=TOP, anchor="w")

        self.average_fitness_label = Label(self.frame, text='Average fitness : ' +
                                           '0 %', font=20,
                                           background="#465B75")
        self.average_fitness_label.pack(side=TOP, anchor="w")

        self.max_fitness_label = Label(self.frame, text='Max fitness : ' +
                                       '0 %', font=20,
                                       background="#465B75")
        self.max_fitness_label.pack(side=TOP, anchor="w")

        self.mutation_rate_label = Label(self.frame, text='Mutation rate : ' +
                                         '0 %', font=20,
                                         background="#465B75")
        self.mutation_rate_label.pack(side=TOP, anchor="w")

        self.scrollbar = Scrollbar(self.frame, orient=VERTICAL)

        # Right frame for list box
        self.frame2 = LabelFrame(
            self.window, width=300, height=250, bg="#465B75", bd=1, relief=FLAT)
        self.frame2.place(x=300, y=0)
        self.frame2.propagate(0)

        self.scrollbar = Scrollbar(self.frame2, orient=VERTICAL)

        self.population_listbox = Listbox(
            self.frame2, yscrollcommand=self.scrollbar.set, width=290)
        self.scrollbar.config(command=self.population_listbox.yview)
        self.scrollbar.pack(side=RIGHT, fill=BOTH)

        self.population_listbox.pack(side=LEFT, fill=BOTH)

        # Bottom Input
        self.frame3 = LabelFrame(
            self.window, width=600, height=100, bg="#465B75", bd=1, relief=FLAT,)
        self.frame3.grid(pady=(250, 0))
        self.frame3.grid_propagate(False)

        # Number of population input block
        self.input_population_label = Label(self.frame3, text='Population:', font=19,
                                            background="#465B75")
        self.input_population_label.grid(column=0, row=0)
        self.input_population = Entry(self.frame3, width=23)
        self.input_population.grid(column=1, row=0)

        # Targe input block
        self.input_target_label = Label(self.frame3, text='Target:', font=19,
                                        background="#465B75")
        self.input_target_label.grid(column=0, row=1)
        self.input_target = Entry(self.frame3, width=23)
        self.input_target.grid(column=1, row=1)

        # Mutation rate input block
        self.labelpoprate = Label(self.frame3, text='Mutation Rate:', font=19,
                                  background="#465B75")
        self.labelpoprate.grid(column=0, row=2)
        self.input_mutation_rate = Entry(self.frame3, width=23)
        self.input_mutation_rate.grid(column=1, row=2)

        # Run button
        self.run_button = Button(self.frame3, text='GO!', height=2, width=10,
                               activebackground='#345', activeforeground='white',
                               command=self.run_algorithm)
        self.run_button.grid(column=3, row=1, padx=(110))

        ### VIEW ###

        ### MAIN PROGRAM'S VARIABLES ###
        self.population = 0
        self.target = ""
        self.mutation_rate = 0.0
        self.result = []
        self.average_fitness_res = []
        self.max_fitness_res = []
        self.generation_res = []

        self.window.mainloop()


# app = App()
