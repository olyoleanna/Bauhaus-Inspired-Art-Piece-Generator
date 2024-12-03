import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QCheckBox, QPushButton, QMessageBox, QLabel
from PyQt5.QtCore import Qt
from genetic_algorithm import GeneticAlgorithm
from output_manager import OutputManager
from similarity_manager import calculate_similarity, REFERENCE_ARTWORK


def initialize_func(instance, grid_size, population, genetic_algorithm):
    instance.setGeometry(600, 150, 800, 800)  # Center output box to screen
    instance.setWindowTitle('Bauhaus Art Generator')
    layout = QVBoxLayout()
    
    # Toggles
    cb_triangle = QCheckBox('Triangle')
    cb_square = QCheckBox('Square')
    cb_circle = QCheckBox('Circle')
    for cb in [cb_triangle, cb_square, cb_circle]:
        cb.setChecked(True)
        layout.addWidget(cb)
    cb_use_colors = QCheckBox('Use Colors')
    cb_use_colors.setChecked(True)
    layout.addWidget(cb_use_colors)

    canvas, axes = OutputManager.create_canvas()
    layout.addWidget(canvas)

    # Similarity Score Label
    similarity_label = QLabel("Bauhaus Artworks Colour Similarity Score: N/A") 
    similarity_label.setAlignment(Qt.AlignHCenter)  # Align score to center
    layout.addWidget(similarity_label)

    # Buttons
    btn_generate = QPushButton('Generate Art')
    btn_generate.clicked.connect(
        lambda: generate_next_generation(
            cb_triangle, cb_square, cb_circle, cb_use_colors,
            canvas, axes, population, grid_size, genetic_algorithm, similarity_label
        )
    )
    layout.addWidget(btn_generate)
    btn_save = QPushButton('Save Art')
    btn_save.clicked.connect(lambda: OutputManager.save_art(canvas.figure))
    layout.addWidget(btn_save)
    widget = QWidget()
    widget.setLayout(layout)
    instance.setCentralWidget(widget)


def get_available_shapes(cb_triangle, cb_square, cb_circle):
    shapes = []
    if cb_triangle.isChecked():
        shapes += ['triangle', 'inverted_triangle']
    if cb_square.isChecked():
        shapes.append('square')
    if cb_circle.isChecked():
        shapes.append('circle')
    return shapes


def generate_next_generation(cb_triangle, cb_square, cb_circle, cb_use_colors, canvas, axes, population, grid_size, genetic_algorithm, similarity_label):
    available_shapes = get_available_shapes(cb_triangle, cb_square, cb_circle)
    if not available_shapes:
        QMessageBox.warning(None, "Error", "Please select at least one shape.")
        return

    if not population:
        population.extend(genetic_algorithm.initialize_population(grid_size, available_shapes))

    # Evolve the population to the next generation
    new_population = genetic_algorithm.evolve_population(population, available_shapes)
    population.clear()
    population.extend(new_population)
    use_colors = cb_use_colors.isChecked()
    best_artwork = max(population, key=genetic_algorithm.evaluate_fitness)
    
    used_colors = OutputManager.draw_art(axes, canvas.figure, best_artwork, available_shapes, use_colors)
    similarity_score = calculate_similarity(used_colors)
    similarity_label.setText(f"Bauhaus Artworks Colour Similarity Score: {similarity_score}%")

def main():
    app = QApplication([])
    grid_size = random.randint(8, 10)
    population = []
    genetic_algorithm = GeneticAlgorithm()
    instance = QMainWindow()
    initialize_func(instance, grid_size, population, genetic_algorithm)
    instance.show()
    app.exec_()

main()