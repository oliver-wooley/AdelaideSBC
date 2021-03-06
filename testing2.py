def nucleotideContent(dnaString):    
    '''This function must return the contribution    
    of nucleotides ATCG (as uppercase) from a given DNA     
    string inside a dictionary, where each key refers to    
    a nucleotide    
    '''    
    if 'S' in dnaString: return False

    dnaDict = {}    
    uniques=set(dnaString)    
    for nucleotide in uniques:    
        dnaDict[nucleotide]=dnaString.count(nucleotide)    
    
    return dnaDict





            #seq      #expected                  
testTable =[['ACGTGT', {'A':1, 'C':1, 'T':2, 'G':2}], 
            ['CAGGTT', {'A':1, 'C':1, 'T':2, 'G':2}],
            ['caggt', {'A':1, 'C':1, 'T':2, 'G':2}],
            ['cSggt', False]     
           ]


passes =0

for (i, (seq, expected)) in enumerate(testTable):
     print nucleotideContent(seq)    
     if nucleotideContent(seq) == expected:
        passes += 1
     else:
        print 'test %i failed' % i


print passes
