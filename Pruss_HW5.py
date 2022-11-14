# Write a function that will generate a bootstrap sample from a list of data 
#   points.

import random

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
    
    sim_list = []
    
    for i in range(num_sims):
        sample = bootstrap_sample(data)
        sim_list.append(calc_trimmed_mean(sample, percent))
        
    return sim_list
    
# test
bootstrap_simulation([0,1,2,3,4,5,6,7,8,9], .25, 15)


