from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
import numpy


def animate_using_pause():
    x = []
    y = []
    for i in range(100):
        x.append(i)
        y.append(i)
        pyplot.xlim(0, 100)
        pyplot.ylim(0, 100)
        pyplot.plot(x, y, color="green")
        pyplot.pause(0.01)
    pyplot.show()


def animate_using_func_animation():
    x = []
    y = []

    figure, ax = pyplot.subplots()
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    line, = ax.plot(0, 0)

    def animation_function(i):
        x.append(i)
        y.append(i)
        line.set_xdata(x)
        line.set_ydata(y)
        return line,
    animation = FuncAnimation(figure, func=animation_function, frames=10, interval=10)
    pyplot.show()


if __name__ == '__main__':
    animate_using_func_animation()
