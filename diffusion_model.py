def energy(density, coeff=1.0):

    #Imports
    from numpy import array, sum
  
    #Assign density list to an numpy array
    density = array(density)
  
    if density.ndim != 1:
        raise ValueError("Density should be an a *1-dimensional* array.")

    if any(density < 0):
        raise ValueError("Density should be an array of *positive integers*.")

    if density.dtype.kind != 'i' and len(density) > 0:
        raise TypeError("Density should be an array of *integers*.")

    #Main code in return
    return coeff * sum(density * (density - 1)) / 2