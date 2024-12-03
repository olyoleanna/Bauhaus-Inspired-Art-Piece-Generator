import random
from get_colors import get_primary_colours

class Artwork:
    @staticmethod
    def create(shapes, colors): # Artwork object creator method
        return {"shapes": shapes, "colors": colors}

    @staticmethod
    def mutate(artwork, available_shapes):
        if random.random() < 0.2:  # 20% chance to mutate
            index = random.randint(0, len(artwork["shapes"]) - 1) # Mutate random cell
            artwork["shapes"][index] = random.choice(available_shapes) # Replace with random shape

    @staticmethod
    def crossover(artwork1, artwork2):
        point = random.randint(1, len(artwork1["shapes"]) - 2) # Random crossover point
        new_shapes = artwork1["shapes"][:point] + artwork2["shapes"][point:] # Shapes and colors are split and recombined to form child
        new_colors = artwork1["colors"][:point] + artwork2["colors"][point:] 
        return Artwork.create(new_shapes, new_colors) # Return child with combined shapes and colors

class GeneticAlgorithm:
    @staticmethod
    def initialize_population(grid_size, available_shapes):
        return [
            Artwork.create(
                [random.choice(available_shapes) for _ in range(grid_size ** 2)],
                [random.choice(get_primary_colours()) for _ in range(grid_size ** 2)]
            )
            for _ in range(25) # 25 artworks for initial population
        ]

    @staticmethod
    def evolve_population(population, available_shapes):
        new_population = []
        for _ in range(len(population)):
            parent1, parent2 = random.sample(population, 2) # 2 random parents from pop
            child = Artwork.crossover(parent1, parent2) # Combine parents
            Artwork.mutate(child, available_shapes) # Randomly mutate child for diversity
            new_population.append(child) # Until new pop is same size as original
        return new_population

    @staticmethod
    def evaluate_fitness(artwork):
        return len(set(artwork["shapes"])) # Artworks with higher shape variete = higher score
