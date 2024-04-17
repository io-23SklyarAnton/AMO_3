import math


class UIViewController:
    variant = "sin^3(x) + 3cos^2(x)"
    sin_x = "sin(x)"

    @staticmethod
    def aitken_formula(x_array, y_array, x0_point):
        n_count = len(x_array)
        p = [0.0] * n_count
        for k in range(n_count):
            some = n_count - k
            for i in range(some):
                if k == 0:
                    p[i] = y_array[i]
                else:
                    p[i] = ((x0_point - x_array[i + k]) * p[i] + (x_array[i] - x0_point) * p[i + 1]) / (
                            x_array[i] - x_array[i + k])
        return p[0]

    @staticmethod
    def formula_data(formula, a, b, count_values=10):
        h = (b - a) / count_values
        x = []
        y = []
        for i in range(count_values + 1):
            x.append(a + (h * i))
            if formula == UIViewController.variant:
                y.append(math.sin(x[i]) ** 3 + 3 * math.cos(x[i]) ** 2)  # "sin^3(x) + 3cos^2(x)"
            elif formula == UIViewController.sin_x:
                y.append(math.sin(x[i]))
        return x, y

    @staticmethod
    def internolated_array(formula, a, b, count_of_interpolation, count_of_array):
        x_teoretical, y_teoretical = UIViewController.formula_data(formula, a, b, count_of_interpolation)
        x_interpolated = UIViewController.formula_data(formula, a, b, count_of_array)[0]
        y_interpolated = []
        for x_val in x_interpolated:
            y_interpolated.append(UIViewController.aitken_formula(x_teoretical, y_teoretical, x_val))
        return x_interpolated, y_interpolated

    @staticmethod
    def get_full_data(aviable_formula, a, b, count, accurate_count=1000):
        x_teoretical, y_teoretical = UIViewController.formula_data(aviable_formula, a, b, accurate_count)
        x_test_lagrange, y_test_lagrange = UIViewController.internolated_array(aviable_formula, a, b, count,
                                                                               accurate_count)
        y_test_lagrange_next = UIViewController.internolated_array(aviable_formula, a, b, count + 1, accurate_count)[1]
        y_errors = [(y_test_lagrange[i] - y_test_lagrange_next[i]) for i in range(len(y_test_lagrange_next))]
        return (x_teoretical, y_teoretical), (x_test_lagrange, y_test_lagrange), (x_test_lagrange, y_errors)
