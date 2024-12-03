REFERENCE_ARTWORK = { # Values based on colour analysis done in TinEye Labs
    "colors": {
        "#bdc0b5": 0.304,  # Grey
        "#303c44": 0.157,  # Dark Grey
        "#d55c48": 0.132,  # Red
        "#d9a328": 0.119,  # Orange / Yellow
        "#c9a47b": 0.094,  # Brown
        "#21598a": 0.075,  # Blue
        "#e67a1e": 0.041,  # Light Orange
        "#d62f1c": 0.040,  # Light Red
        "#419e5c": 0.037   # Green
    }
}

def calculate_color_proportions(colors):
    total = len(colors)
    proportions = {}
    for color in colors:
        proportions[color] = proportions.get(color, 0) + 1 # Count how often color appears in list
    return {color: count / total for color, count in proportions.items()} # Divide each count by total num of colors to calculate porportion

def calculate_similarity(used_colors):
    generated_colors = calculate_color_proportions(used_colors) # Calc min proportion between generated and referenced proportions
    reference_colors = REFERENCE_ARTWORK["colors"]

    color_similarity = sum(min(generated_colors.get(color, 0), reference_colors.get(color, 0))for color in reference_colors) # Sum overlaps for all colors to calc similarity

    max_possible_similarity = sum(reference_colors.values())
    if max_possible_similarity > 0: # Divide total similarity by max/sum of all ref proportions to ensure score is relative to ref
        color_similarity /= max_possible_similarity

    return round(color_similarity * 100, 2) # Convert to percentage
