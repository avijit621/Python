import random
import matplotlib.pyplot as plt
import numpy as np


class Dice:
    def __init__(self, num_sides=6): # the deafult value of the dice is 6
        self.num_sides = num_sides
        self.dist_values = [] # variable to print the distributin 
        self.prob_dist = [] # list for holdng the discrete distribution 
        if isinstance(self.num_sides, str) == True:
            try:
                raise Exception('Cannot construct dice')
            except Exception as inst:
                print(type(inst))
                print(inst)
            exit() 
        
        elif self.num_sides <= 3 or isinstance(self.num_sides, int) == False:
            try:
                raise Exception('Cannot construct dice')
            except Exception as inst:
                print(type(inst))
                print(inst)
            exit()    
        
        else:
            # if no distribution specified assigning uniform distribution
            for i in range(self.num_sides):
                self.prob_dist.append(1 / self.num_sides)
            self.dist_values = "{" + ", ".join([str(x) for x in self.prob_dist]) + "}"

    def __str__(self):
        return "Dice with {0} faces and probability distribution {1}".format(self.num_sides, self.dist_values)

    def setProb(self, prob_values):
        self.prob_values = prob_values
        self.prob_dist.clear() 
        # Assigning user provided distribution 
        for i in range(self.num_sides):
            self.prob_dist.append(prob_values[i])
        # checking the Assigned is a valid probability distribution   
        for i in self.prob_dist:
            if i < 0 or round(sum(self.prob_dist),10)!=1.0:
                print(sum(self.prob_dist))
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
        # labels for different sides of the dice
        labels = [x + 1 for x in range(self.num_sides)]
        # A dictionary is created to sample the random disitribution 
        prob_dict = {i : 0 for i in labels}
        
        CDF_list=[0]
        for i in range(len(self.prob_dist)):
            CDF_list.append(CDF_list[i]+self.prob_dist[i]) 
        # Sampling the random distribution 
        for i in range(self.iter):
            r=random.random()
            for i in range(len(CDF_list)):
                if (CDF_list[i]<r<CDF_list[i+1]):
                    prob_dict[i+1]=prob_dict[i+1]+1 # suming up the no of times different sides appear
        # Generating the final distribution 
        random_dist=[prob_dict[i]/iter for i in prob_dict.keys()]     
        fig, ax = plt.subplots()
        x = np.arange(len(labels))
        width = 0.15
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        # random disribution 
        ax.bar(x - width / 2, [self.iter * i for i in random_dist], width, label='Expected', color='r')
        # actual distribution 
        ax.bar(x + width / 2, [self.iter * i for i in self.prob_dist], width, label='Actual', color='b')
        ax.set_title('Outcome of {0} throws of a {1}-faced dice'.format(self.iter, self.num_sides), fontsize=12)
        ax.set_ylabel('Sides')
        ax.set_xlabel("Outcomes")
        ax.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
        plt.tight_layout()
        plt.show()
        

d = Dice(4)
#print(d)
#d.setProb((0.1, 0.2, 0.4,0.3))
#print(d)
# print(d)
d.roll(18000)
