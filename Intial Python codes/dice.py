import random
import matplotlib.pyplot as plt
import numpy as np


class Dice:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
        self.dist_values = []
        self.prob_dist = []
        if isinstance(self.num_sides, str) == True:
            try:
                raise Exception('Cannot construct dice')
            except Exception as inst:
                print(type(inst))
                print(inst)

        elif self.num_sides <= 3 or isinstance(self.num_sides, int) == False:
            try:
                raise Exception('Cannot construct dice')
            except Exception as inst:
                print(type(inst))
                print(inst)
        else:
            for i in range(self.num_sides):
                self.prob_dist.append(1 / self.num_sides)
            self.dist_values = "{" + ", ".join([str(x) for x in self.prob_dist]) + "}"

    def __str__(self):
        return "Dice with {0} faces and probability distribution {1}".format(self.num_sides, self.dist_values)

    def setProb(self, prob_values):
        self.prob_values = prob_values
        # dist = []
        self.prob_dist.clear()
        for i in range(self.num_sides):
            self.prob_dist.append(prob_values[i])
        for i in self.prob_dist:
            if i < 0 or sum(self.prob_dist) != 1:
                try:
                    raise Exception('Invalid probability distribution')
                except Exception as inst:
                    print(type(inst))
                    print(inst)
                    break

        self.dist_values = "{" + ", ".join([str(x) for x in self.prob_dist]) + "}"
        return self

    def roll(self, iter):
        self.iter = iter
        #dis = []
        #dict = {}
        #keys = range(1, self.num_sides + 1)
        labels = [x + 1 for x in range(self.num_sides)]
        '''
        for i in keys:
            dict[i] = 0
        for i in range(self.iter):
            r = random.randint(1, self.num_sides)
            dict[r] = dict[r] + 1

        dis = []
        for i in range(self.num_sides):
            dis.append(dict[i + 1] / self.iter)
        '''
        dis = [random.random() for i in range(self.num_sides)]
        s = sum(dis)
        dis = [i / s for i in dis]

        fig, ax = plt.subplots()
        x = np.arange(len(labels))
        width = 0.15

        # dis1 = [1 / self.num_sides * self.iter for i in range(self.num_sides)]
        # print(dis1)

        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        print(dis)
        ax.bar(x - width / 2, [self.iter * i for i in dis], width, label='Expected', color='r')
        ax.bar(x + width / 2, [self.iter * i for i in self.prob_dist], width, label='Actual', color='b')
        ax.set_title('Outcome of {0} throws of a {1}-faced dice'.format(self.iter, self.num_sides), fontsize=12)
        ax.set_ylabel('Sides')
        ax.set_xlabel("Outcomes")
        ax.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
        plt.tight_layout()
        plt.show()


d = Dice(4)
# print(d)
#d.setProb((0.1, 0.2, 0.3, 0.1,0.2,0.1))
#print(d)
# print(d)
d.roll(100)
