import random
from matplotlib.patches import Circle, Rectangle, Polygon, Wedge

class ShapeGenerator:
    @staticmethod
    def draw_circles(axes, x, y, size, color):
        shape_type = random.choice(['circle', 'quarter_circle'])

        if shape_type == 'circle':
            axes.add_patch(Circle((x + size / 2, y + size / 2), size / 2, color=color))
        elif shape_type == 'quarter_circle':
            radius = size
            start_angle = random.choice([0, 270]) # Upright or opposite orientation of quarter circle

            # Adjust center based on start angle
            if start_angle == 0:
                center_x = x
                center_y = y
            else:  # 270
                center_x = x
                center_y = y + size

            axes.add_patch(Wedge((center_x, center_y), radius, start_angle, start_angle + 90, color=color))

    @staticmethod
    def draw_square(axes, x, y, size, color, mini_circle_color):
        axes.add_patch(Rectangle((x, y), size, size, color=color))
        axes.add_patch(Circle((x + size / 2, y + size / 2), size / 4, color=mini_circle_color)) # Mini circle inside square

    @staticmethod
    def draw_triangle(axes, x, y, size, color, shape_type):
        if shape_type == 'triangle':
            axes.add_patch(Polygon([(x, y), (x + size, y), (x, y + size)], color=color))
        elif shape_type == 'inverted_triangle': # Inverted right triangle
            axes.add_patch(Polygon([(x, y + size), (x + size, y + size), (x + size, y)], color=color))
