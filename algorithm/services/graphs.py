import os
import numpy as np
from scipy.interpolate import splrep, splev
import matplotlib.pyplot as plt

from AMO_3 import settings
from AMO_3.settings import BASE_DIR
from algorithm.services.algorithms import UIViewController

STATIC_ROOT = settings.STATIC_ROOT
GRAPH_DIR = os.path.join(STATIC_ROOT, 'graphs')
os.makedirs(GRAPH_DIR, exist_ok=True)


def draw_function_and_mistake_graphs(a=0, b=4, function="sin(x)"):
    count_of_interpolation = 5
    count_of_array = 10
    (x_theoretical, y_theoretical), (x_interpolated, y_interpolated), (
        x_errors, y_errors) = UIViewController.get_full_data(
        function, a, b, count_of_interpolation, count_of_array)

    x_smooth_theoretical = np.linspace(min(x_theoretical), max(x_theoretical), 1000)
    y_smooth_theoretical = splev(x_smooth_theoretical, splrep(x_theoretical, y_theoretical))

    x_smooth_interpolated = np.linspace(min(x_interpolated), max(x_interpolated), 1000)
    y_smooth_interpolated = splev(x_smooth_interpolated, splrep(x_interpolated, y_interpolated))

    plt.plot(x_smooth_theoretical, y_smooth_theoretical, label='Theoretical (Smooth)')
    plt.plot(x_smooth_interpolated, y_smooth_interpolated, label='Interpolated (Smooth)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interpolation and Smoothed Theoretical Values')
    plt.legend()
    plt.grid(True)

    plt.savefig(os.path.join(f'{BASE_DIR}\\algorithm\\static\\img', f'function_graph.png'))
    plt.close()

    x_smooth_errors = np.linspace(min(x_errors), max(x_errors), 1000)
    y_smooth_errors = splev(x_smooth_errors, splrep(x_errors, y_errors))
    y_smooth_errors = [abs(error) for error in y_smooth_errors]

    plt.plot(x_smooth_errors, y_smooth_errors, label='Error (Smooth)')
    plt.xlabel('x')
    plt.ylabel('Error')
    plt.title('Error of Interpolation')
    plt.legend()
    plt.grid(True)

    plt.savefig(os.path.join(f'{BASE_DIR}\\algorithm\\static\\img', f'mistake_graph.png'))
    plt.close()


draw_function_and_mistake_graphs()