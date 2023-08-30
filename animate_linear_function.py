from matplotlib import pyplot
if __name__ == '__main__':
    ...
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
