import numpy as np

def calculate(list):

    #Exception if list has more or less than 9 numbers

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")


      

    #Convert list to numpy array

    array = np.array([[list[0], list[1], list[2]],
    [list[3], list[4], list[5]], 
    [list[6], list[7], list[8]]])


  
    
    # Axis and flattened array means

    axis1Means = [array[:,0].mean(), array[:,1].mean(), array[:,2].mean()]

    axis2Means = [array[0,:].mean(), array[1,:].mean(), array[2,:].mean()]

    flatMean = array.mean()

    # Axis and flattened array variances

    axis1Vars = [array[:,0].var(), array[:,1].var(), array[:,2].var()]

    axis2Vars = [array[0,:].var(), array[1,:].var(), array[2,:].var()]

    flatVar = array.var()

    # Axis and flattened array standard deviations

    axis1Stds = [array[:,0].std(), array[:,1].std(), array[:,2].std()]

    axis2Stds = [array[0,:].std(), array[1,:].std(), array[2,:].std()]

    flatStd = array.std()

    # Axis and flattened array maxes

    axis1Maxes = [array[:,0].max(), array[:,1].max(), array[:,2].max()]

    axis2Maxes = [array[0,:].max(), array[1,:].max(), array[2,:].max()]

    flatMax = array.max()

    # Axis and flattened array minimums

    axis1Mins = [array[:,0].min(), array[:,1].min(), array[:,2].min()]

    axis2Mins = [array[0,:].min(), array[1,:].min(), array[2,:].min()]

    flatMin = array.min()

    # Axis and flattened array sums

    axis1Sums = [array[:,0].sum(), array[:,1].sum(), array[:,2].sum()]

    axis2Sums = [array[0,:].sum(), array[1,:].sum(), array[2,:].sum()]

    flatSum = array.sum()



    calculations = {
    'mean': [axis1Means, axis2Means, flatMean],
    'variance': [axis1Vars, axis2Vars, flatVar],
    'standard deviation': [axis1Stds, axis2Stds, flatStd],
    'max': [axis1Maxes, axis2Maxes, flatMax],
    'min': [axis1Mins, axis2Mins, flatMin],
    'sum': [axis1Sums, axis2Sums, flatSum]
    }


  

    return calculations