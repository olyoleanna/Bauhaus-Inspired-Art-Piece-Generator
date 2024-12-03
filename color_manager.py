import random

def get_primary_colours():
    primary_colors = [
        ("#d55c48", 0.15),  # Red
        ("#21598a", 0.12),  # Blue
        ("#d9a328", 0.12),  # Yellow
        ("#bdc0b5", 0.10),  # Grey (Additions)
        ("#303c44", 0.10),  # Dark Grey
        ("#c9a47b", 0.08),  # Brown
        ("#e67a1e", 0.08),  # Bright Orange
        ("#d62f1c", 0.08),  # Bright Red
        ("#419e5c", 0.07),  # Green
    ]

    color_pool = [color for color, weight in primary_colors for _ in range(int(weight * 100))]

    random.shuffle(color_pool)
    return random.sample(color_pool, len(primary_colors)) 
