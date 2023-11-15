# importing the modules
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt


def create_matrix(n, m):
    matrix = np.zeros((n, m))
    return matrix

def select_random_cell(matrix):
    n, m = matrix.shape
    i = np.random.randint(0, n)
    j = np.random.randint(0, m)
    return i, j

def diminish_values(matrix, i, j,  max_strength):
    print(max_strength)
    n, m = matrix.shape
    for new_i in range(n):
        for new_j in range(m):
            distance = np.sqrt((new_i - i)**2 + (new_j - j)**2)
            matrix[new_i, new_j] = max_strength / (distance + 1)


def main():
    matrix = create_matrix(10, 10)
    i, j = select_random_cell(matrix)
    max_strength = 100  # Adjust as needed
    diminish_values(matrix, i, j, max_strength * pow(10, 6))

    # plotting the heatmap
    hm = sn.heatmap(data=matrix, cmap='viridis')  # Adjust cmap as needed

    # saving the plotted heatmap as a PNG file
    plt.savefig("heatmap.png")

    # displaying the plotted heatmap
    plt.show()


    plt.close()

if __name__ == "__main__":
    main()






