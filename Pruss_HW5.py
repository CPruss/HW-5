# Write a function that will generate a bootstrap sample from a list of data 
#   points.

import random
from plotnine import *
import pandas as pd

def bootstrap_sample(data):
    """
    Generates a bootstrap sample from the list of data.

    Parameters
    ----------
    data : list
        The data list to sample from.

    Returns
    -------
    sample : list
        A list containing the bootstrap sample.

    """
    sample = []
    
    for i in range(len(data)):
        sample += random.sample(data, 1)
        
    return sample
        

# Write a function that will calculate the trimmed mean from a list of data. 

def calc_trimmed_mean(data, percent):
    """
    Calculates the trimmed mean from the given list of data, removing the given
    percent from top and bottom.

    Parameters
    ----------
    data : list
        The list to calculate the trimmed mean of.
    percent : positive float < .5
        The percentage of data to remove.

    Returns
    ----------
    trimmed_mean : float
        The trimmed mean of the given data.

    """
    # sort the data
    data.sort()
    
    # find the amount of points to trim off
    outliers_num = int(percent * len(data))
    
    # trim the points
    trimmed_data = []
    
    for i in range(len(data)):
        if i+1 > outliers_num and i < (len(data) - outliers_num):
            trimmed_data.append(data[i])
            
    # take the mean
    trimmed_mean = sum(trimmed_data)/len(trimmed_data)
    
    return trimmed_mean

# Write a function that will use the previous two functions and will perform 
#   a bootstrap simulation for the trimmed mean. 

def bootstrap_simulation(data, percent, num_sims):
    """
    Runs a bootstrap simulation for the given data, calculating trimmed means
    from the samples.

    Parameters
    ----------
    data : list
        The list of data to run the simulation on.
    percent : float
        The percent of data to trim off from the upper and lower ends of the sample.
    num_sims : int
        The number of simulations to run.

    Returns
    -------
    sim_list : list
        List of trimmed means from the simulation.

    """
    
    sim_list = []
    
    for i in range(num_sims):
        sample = bootstrap_sample(data)
        sim_list.append(calc_trimmed_mean(sample, percent))
        
    return sim_list
    
def bootstrap_hist(dat, percent, num_sims):
    """
    Creates a histogram of trimmed means from a bootstrap simulation on the data.

    Parameters
    ----------
    dat : list
        The list of data to run the simulation on.
    percent : float
        The percent of data to trim off from the upper and lower ends of the sample.
    num_sims : int
        The number of simulations to run.

    Returns
    -------
    p : plot
        The histogram plot of trimmed means.

    """
    
    sim_list = bootstrap_simulation(dat, percent, num_sims)
    
    p = (
        ggplot(data = pd.DataFrame(sim_list))+
        aes(x = sim_list)+
        geom_histogram()
        )
    return p
    
# test
bootstrap_simulation([0,1,2,3,4,5,6,7,8,9], .25, 15)



dat = pd.read_csv("ckconcentration.csv")
bootstrap_simulation(list(dat["CKConcentration"]), .2, 15)
bootstrap_hist(list(dat["CKConcentration"]), .2, 10000)
