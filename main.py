import plotly.figure_factory as ff;
import plotly.graph_objects as go;
import pandas as pd;
import csv;
import random;
import statistics;


data_file = pd.read_csv('medium_data.csv');
data = data_file['reading_time'].tolist();


def random_set_of_mean(counter):
    data_set = [];
    for i in range(0, counter):
        index = random.randint(0, len(data ) - 1);
        value = data[index];
        data_set.append(value);

    sampling_mean = statistics.mean(data_set);
    print("Sampling mean - ", sampling_mean)
    return sampling_mean;

def show_graph(mean_list):
    df = mean_list;
    mean= statistics.mean(df);
    print("Mean - ", mean);
    graph = ff.create_distplot([df],['average'],show_hist= False);
    graph.add_trace(go.Scatter(x=[mean, mean], y=[0,1], mode = 'lines', name= 'mean'))
    graph.show();

def setup():
    mean_list = [];
    for i in range(0, 100):
        set_means = random_set_of_mean(30);
        mean_list.append(set_means);
    show_graph(mean_list); 

setup();    