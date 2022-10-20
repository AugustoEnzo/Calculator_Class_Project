import matplotlib
import matplotlib.pyplot as plt


class LinearFormula:
    def __init__(self):
        self.__ru: str = '3987863'

        self.__a: int = int(self.__ru[len(self.__ru) - 3])
        self.__b: int = int(self.__ru[len(self.__ru) - 2])
        self.__c: int = int(self.__ru[len(self.__ru) - 1])

        if self.__a == 0:
            self.__a = 3
        if self.__b == 0:
            self.__b = 3
        if self.__c == 0:
            self.__c = 3

        # Axis values
        self.__x1: int = 5
        self.__x2: int = 7
        self.__x3: int = 9

        # Doing the formula calculus for each x axis value
        # Formula calculus
        self.__y: float = self.__a * self.__x1 + self.__b + self.__x1 - self.__c

        # Append the results for y1
        self.__results1 = self.__y

        self.__y: float = self.__a * self.__x2 + self.__b + self.__x2 - self.__c

        # Append the results for y2
        self.__results2 = self.__y

        self.__y: float = self.__a * self.__x3 + self.__b + self.__x3 - self.__c

        # Append the results for y3
        self.__results3 = self.__y

        # Plotting the points
        plt.scatter(self.__x1, self.__results1, label='xy1')
        plt.scatter(self.__x2, self.__results2, label='xy2')
        plt.scatter(self.__x3, self.__results3, label='xy3')

        # Creating the legends
        plt.legend()
        # Naming the x-axis
        plt.xlabel('X - Axis')
        # Naming the y-axis
        plt.ylabel('y - axis')

        # Giving a title to the graph
        plt.title('y = ax + bx – c')

        # Function that show the plot
        plt.savefig("LinerFormula.png")


# Instantiate the object
LinearFormula()
