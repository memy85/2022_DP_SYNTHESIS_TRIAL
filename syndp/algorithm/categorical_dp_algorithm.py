

import numpy as np

def get_discretized_value(value, level):
    '''
    value : 카테고리컬 값
    level : 카테고리컬 레벨
    '''
    if level == 1:
        return -1
    
    beta = (value + 1) * (level -1) /2
    k = np.floor(beta)
    z1 = 2 * (k+1)/(level -1) -1
    z2 = 2 * k / (level -1) -1
    p = (level -1) * (value + 1) / 2 - k
    
    # bionom function to get {0, 1} by p
    binom = lambda p_i : np.random.binomial(size=1, n=1, p=p_i)
    
    # make Z vector by choosing z1, z2 using condition vector
    
    Z = np.where(binom(p), z1, z2)
    return Z
    