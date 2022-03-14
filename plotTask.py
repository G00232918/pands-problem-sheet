# Write a program called plottask.py that displays a plot 
# of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] 
# on the one set of axes.
# Author: James Connolly

# import numpy for calculations on array
import numpy as np
#import matplotlib for plotting on graph
import matplotlib.pyplot as plt

def plotsFunc():
    # setting up the range
    xpoints = np.array(range(0,5))
    # f(x) = x
    fpoints = xpoints
    # g(x) = x2
    gpoints = xpoints*xpoints
    # h(x) = x3
    hpoints = xpoints**xpoints

    # fpoints plotted, marker o to plot the variable value for each
    plt.plot(fpoints, marker = "o", color="r", label ="f(x) = x")
    #gpoints plotted, line dashed and linewidth set different
    plt.plot(gpoints, marker = "o", color="b", label ="g(x) = x2", linestyle = "dashed", linewidth=2)
    # hpoints plotted, linewidth set to higher than other plots
    plt.plot(hpoints, marker = "o", color="y", label ="h(x) = x3", linewidth=5)

    # set title, position to the left, font size
    plt.title("Plotting task", loc ="left", fontsize=15)
    # set the axis labels
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")

    # set legend for plots
    plt.legend()
    # save the file
    plt.savefig(fname="PlottingTask.png")
    plt.show()

plotsFunc()
    
    