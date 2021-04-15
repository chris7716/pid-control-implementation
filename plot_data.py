import matplotlib.pyplot as plt

def plot(x_plots, y_plots, legend_labels, x_label, y_label, colors, title):
    for i in range (0, len(x_plots)):
        plt.plot(x_plots[i], y_plots[i], label=legend_labels[i], color=colors[i])

    plt.xlabel(x_label, color = 'black')
    plt.ylabel(y_label,color = 'black')

    plt.title(title)

    plt.legend()

    plt.grid(True)
    plt.show()
