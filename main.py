# importing the required module
import matplotlib.pyplot as plt
import pid
import plot_data
import reference
import sample_generator

samples = sample_generator.generate(121)

(instantanious_time, references, outputs) = pid.implement(0.5, 0.5, 0.006, reference.get_function, samples)

x_plots = [instantanious_time, instantanious_time]
y_plots = [references, outputs]
colors = ['green', 'yellow']
legend_labels = ['Expected', 'Actual']

plot_data.plot(x_plots, y_plots, legend_labels, 'Time(s)', 'Motor Speed(rad/s)', colors, 'PID Implementation for DC Motor\nK_p=0.5 K_i=0.5 K_d=0.006')
