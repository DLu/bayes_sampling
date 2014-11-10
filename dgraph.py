import matplotlib.pyplot as plt
import numpy
from time import sleep

class DynamicGraph:
    def __init__(self, sleep=0.0):
        self.sleep = sleep
        self.hl, = plt.plot([], [], '-')
        plt.show(block=False)
        self.ax = plt.gca()
        
    def add_point(self, x, y):
        self.hl.set_xdata(numpy.append(self.hl.get_xdata(), x))
        self.hl.set_ydata(numpy.append(self.hl.get_ydata(), y))
        self.ax.relim()
        self.ax.autoscale_view() 
        plt.draw()
        sleep(self.sleep)
        
    def show(self):
        plt.show()
    


