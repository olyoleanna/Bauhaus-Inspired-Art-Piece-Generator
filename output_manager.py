import random
from PyQt5.QtWidgets import QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from shape_generator import ShapeGenerator
from color_manager import get_primary_colours

class OutputManager:
    @staticmethod
    def create_canvas(width=8, height=6, dpi=100):
        """Create and return a new canvas and axes."""
        fig = Figure(figsize=(width, height), dpi=dpi)
        axes = fig.add_subplot(111)
        axes.set_axis_off() # Remove x and y axis
        fig.patch.set_facecolor('#e0e0e0')  # Light grey background
        canvas = FigureCanvas(fig)
        return canvas, axes

    @staticmethod
    def draw_art(axes, fig, artwork, available_shapes, use_colors=True):
        axes.set_axis_off()
        axes.clear()
        axes.set_facecolor('#e0e0e0')

        grid_size = random.randint(8, 10)
        cell_size = 1 / grid_size

        used_colors = [] # Track colours used

        for i in range(grid_size):
            for j in range(grid_size):
                x, y = i * cell_size, j * cell_size
                index = (i * grid_size + j) % len(artwork["shapes"])

                shape_choice = artwork["shapes"][index]
                color = artwork["colors"][index]

                if not use_colors:
                    color = '#bdc0b5'  # Grey when no colours
                    mini_circle_color = '#e0e0e0' # Background colour (empty)
                else:
                    mini_circle_color = random.choice([c for c in get_primary_colours() if c != color])

                if shape_choice not in available_shapes and available_shapes:
                    shape_choice = random.choice(available_shapes)

                used_colors.append(color)

                if shape_choice == 'circle':
                    ShapeGenerator.draw_circles(axes, x, y, cell_size, color)
                elif shape_choice == 'square':
                    ShapeGenerator.draw_square(axes, x, y, cell_size, color, mini_circle_color)
                elif shape_choice in ['triangle', 'inverted_triangle']:
                    ShapeGenerator.draw_triangle(axes, x, y, cell_size, color, shape_choice)

        axes.set_axis_off()
        fig.canvas.draw_idle()
        return used_colors

    @staticmethod
    def save_art(fig):
        file_path, _ = QFileDialog.getSaveFileName(None, "Save Art (PNG)", "", "PNG Files (*.png)")
        if file_path:
            fig.savefig(file_path, format='png')
