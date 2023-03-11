# EXPLANATIONS
'''
Genetic Algorithms (GAs) are a class of optimization algorithms inspired by the process of natural selection in biological systems. 
In a GA, a population of candidate solutions is evolved over time to find an optimal or near-optimal solution to a given problem.
'''



# STEPS
'''
The basic framework of a GA involves the following steps:

Initialization: Create an initial population of candidate solutions (chromosomes) randomly.
Evaluation: Evaluate the fitness of each chromosome by calculating the objective function value or fitness score.
Selection: Select the fittest chromosomes from the population to create a new population for the next generation.
Crossover: Combine pairs of chromosomes (parents) to create new offspring by exchanging genetic information (genes).
Mutation: Randomly modify the genes of some offspring to introduce new genetic variation in the population.
Termination: Repeat steps 2 to 5 until a termination criterion is met, such as a maximum number of generations or a satisfactory fitness score.

'''
# CODE

import random

# Define the fitness function
def fitness_func(x):
    return x**2 + 2*x - 3

# Define the initial population
def init_population(size):
    return [random.uniform(-10, 10) for _ in range(size)]

# Define the selection function
def selection(population):
    sorted_pop = sorted(population, key=lambda x: fitness_func(x))
    return sorted_pop[:len(sorted_pop)//2]

# Define the crossover function
def crossover(parents, size):
    children = []
    while len(children) < size:
        mom, dad = random.choices(parents, k=2)
        child = (mom + dad) / 2
        children.append(child)
    return children

# Define the mutation function
def mutation(children, rate):
    for i, child in enumerate(children):
        if random.random() < rate:
            children[i] = random.uniform(-10, 10)
    return children

# Define the main function for running the GA
def genetic_algorithm(num_generations, pop_size, crossover_rate, mutation_rate):
    population = init_population(pop_size)
    for i in range(num_generations):
        parents = selection(population)
        children = crossover(parents, pop_size - len(parents))
        children = mutation(children, mutation_rate)
        population = parents + children
    return min(population, key=lambda x: fitness_func(x))

# Run the GA with some example parameters
best_solution = genetic_algorithm(num_generations=100, pop_size=100, crossover_rate=0.8, mutation_rate=0.1)

# Print the best solution and fitness score
print(f"Best solution: {best_solution}")
print(f"Fitness score: {fitness_func(best_solution)}")




# further Explanations of CODE

'''
In this implementation, we define the fitness function fitness_func to be f(x) = x^2 + 2x - 3, which we want to minimize. We also define the init_population, 
selection, crossover, and mutation functions, which are the basic components of the GA.

We then define the genetic_algorithm function, which runs the GA for a given number of generations and returns the best solution found.
In each generation, we select the fittest individuals from the population using the selection function, 
then generate new offspring using the crossover function and mutate them using the mutation function. Finally, we replace the old population with the new one and repeat the process for the specified number of generations.

Finally, we run the GA with some example parameters and print the best solution and fitness score found.

Note that this is a very basic example and there are many ways to customize and optimize the GA, such as using different selection, 
crossover, and mutation operators, using elitism to preserve the best individuals, or incorporating domain-specific knowledge 
into the fitness function or encoding scheme.
'''


