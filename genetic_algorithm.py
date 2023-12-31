import numpy as np

class Chromosome:
    def __init__(self, weights, profits, knapsack_size):
        self.genes = np.random.randint(0, 2, len(weights))
        self.weights = weights
        self.profits = profits
        self.knapsack_size = knapsack_size
        self.update_fitness()

    def update_fitness(self):
        total_weight = np.dot(self.genes, self.weights)
        self.fitness = np.dot(self.genes, self.profits) if total_weight <= self.knapsack_size else 0

    def single_point_crossover(self, chromosome):
        crossover_point = np.random.randint(1, len(self.genes) - 1)
        offspring1, offspring2 = Chromosome(self.weights, self.profits, self.knapsack_size), Chromosome(self.weights, self.profits, self.knapsack_size)
        offspring1.genes = np.concatenate((self.genes[:crossover_point], chromosome.genes[crossover_point:]))
        offspring2.genes = np.concatenate((chromosome.genes[:crossover_point], self.genes[crossover_point:]))
        offspring1.update_fitness()
        offspring2.update_fitness()
        return offspring1, offspring2

    def mutate(self, mutation_probability):
        self.genes = np.where(np.random.random(len(self.genes)) < mutation_probability, self.genes ^ 1, self.genes)
        self.update_fitness()

class GeneticAlgorithm:
    def __init__(self, weights, profits, knapsack_size, population_size, selection_ratio=0.4, mutation_prob=0.5):
        self.population_size = population_size
        self.selection_ratio = selection_ratio
        self.mutation_prob = mutation_prob
        self.chromosomes = [Chromosome(weights, profits, knapsack_size) for _ in range(population_size)]

    def crossover(self, parents):
        return parents[0].single_point_crossover(parents[1])

    def mutation(self, offsprings):
        for offspring in offsprings:
            offspring.mutate(self.mutation_prob)
        return offsprings

    def next_generation(self):
        n_selection = int(self.population_size * self.selection_ratio)
        n_selection = (n_selection // 2) * 2
        fittest_individuals = sorted(self.chromosomes, key=lambda x: x.fitness, reverse=True)[:n_selection]

        offsprings = [self.crossover(fittest_individuals[i:i + 2]) for i in range(0, n_selection, 2)]
        offsprings = [item for sublist in offsprings for item in sublist]
        offsprings = self.mutation(offsprings)

        self.chromosomes += offsprings
        self.chromosomes = sorted(self.chromosomes, key=lambda x: x.fitness, reverse=True)[:self.population_size]

    def fittest_chromosome(self):
        return max(self.chromosomes, key=lambda x: x.fitness)

    def evolve(self, generations, log_freq=1000):
        for generation in range(1, generations + 1):
            self.next_generation()
            if generation % log_freq == 0:
                max_profit = self.fittest_chromosome().fitness
                print(f'Generation {generation}: Max Profit = {max_profit}')
        return self.fittest_chromosome()

item_count = 7
knapsack_size = 20
population_size = 8

weights = np.random.randint(1, knapsack_size, size=item_count)
profits = np.random.randint(1, 50, size=item_count)

print(f'Knapsack Size: {knapsack_size}')
print('Weight\tProfit')
for weight, profit in zip(weights, profits):
    print(f'{weight}\t{profit}')

ga = GeneticAlgorithm(weights=weights, profits=profits, knapsack_size=knapsack_size, population_size=population_size)

solution = ga.evolve(100)

print('\nSolution Found')
print('Weight\tProfit\tSelect')
for weight, profit, gene in zip(weights, profits, solution.genes):
    print(f'{weight}\t{profit}\t{gene}')
print(f'Max Profit: {solution.fitness}')
