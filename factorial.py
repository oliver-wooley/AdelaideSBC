def fact(n):
    '''Return the factorial of n, an integer >= 0    
    >>> fact(4)
    24
    >>> fact(-1)
    1
    '''

    

    import math
    if not n>=0: #n needs to be positive
        raise ValueError('n must be >=0')
    if math.floor(n) !=n : #needs to be an integer 
        raise ValueError('n must be integer')
   
	# Jimmy changed this file here    
 
    #this counts from 1 up to n whilst the traditional way we think of factors is the opposite
    result =1  
    factor  =2
    while factor <= n:
        result *= factor
        factor += 1    

    return result
#1 will return 2

print 'testing testing'

if __name__ == '__main__':
    import doctest
    doctest.testmod()
