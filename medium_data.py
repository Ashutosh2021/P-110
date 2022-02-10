import pandas as pd
import statistics
import plotly.figure_factory as ff
import random

df = pd.read_csv("medium_data.csv")
population_data = df["reading_time"].tolist()

population_mean = statistics.mean(population_data)
print("Population Mean :",population_mean)

def random_set_of_mean(counter) :
    random_data_list =[]
    for i in range(0,counter) :
        random_index = random.randint(0,len(population_data)-1)
        value = population_data[random_index]
        random_data_list.append(value)
    mean = statistics.mean(random_data_list)
    return mean

def show_fig(mean_list) :
    d_f = mean_list
    fig = ff.create_distplot([d_f],["Means"],show_hist=False)
    fig.show()


def setup() :
    mean_list = []
    for i in range(0,100) :
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    sample_mean = statistics.mean(mean_list)
    print("Sampling Mean :",sample_mean)
    show_fig(mean_list=mean_list)


setup()