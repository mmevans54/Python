import numpy as np


def calculate_mini_square_sum(the_numps, x_origin, y_origin):
    the_sum = 0

    for x in range(x_origin, x_origin + 3):
        for y in range(y_origin, y_origin + 3):
            the_sum += the_numps[y, x]

    return the_sum


if __name__ == '__main__':

    with open("array-final-2d.txt", 'r') as input_file:
        # 200 rows
        # 50 columns
        my_numpy_array = np.empty((50, 50))

        for line in input_file:
            x = 0
            y = 0
            for data in line.split(","):

                my_numpy_array[y, x] = data
                x += 1

                if x == 50:
                    x = 0
                    y += 1
                    if y == 50:
                        break

        # print("the numps: ")
        # print(my_numpy_array)

        x = 0
        y = 0
        sum_list = {}

        current_max = 0
        current_max_x = 0
        current_max_y = 0
        while y <= 47:
            x = 0
            while x <= 47:
                # print(f"the coordinates: {x}, {y}")

                this_max = int(calculate_mini_square_sum(my_numpy_array, x, y))
                if this_max in sum_list:
                    sum_list[this_max] += 1
                else:
                    sum_list[this_max] = 1
                # Store the new max value
                if this_max > current_max:
                    current_max_x = x
                    current_max_y = y
                    current_max = this_max

                x += 3
            y += 3
        print(f"The max square value is: {current_max}")
        print(f"The location of the max square value is: {current_max_x},{current_max_y}")
        # print(f"The sumlist: {sum_list}")

        current_max_sum = 0
        current_max_occurrences = 0
        for key in sum_list.keys():
            if sum_list[key] > current_max_occurrences:
                current_max_sum = key
                current_max_occurrences = sum_list[key]
                # print(f"the sum: {key}, number of occurrences: {sum_list[key]}")

        for key in sum_list.keys():
            if sum_list[key] == current_max_occurrences:
                print(f"the current max sum: {current_max_sum}, current max number of occurrences: {current_max_occurrences}")



