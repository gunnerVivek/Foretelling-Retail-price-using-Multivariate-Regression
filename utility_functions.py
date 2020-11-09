'''
    This module  defines the various utility functions needed
    in the project.
'''

import numpy as np
import pandas as pd

def threshold_data(feature):
    
    '''
        Apply thresholding to data. Threshold values are decided 
        by using IQR. 
        
        Maximum threshold value is 3rd Quartile added to 1.5 times the IQR(Inter QuartileRange)
        Minimum threshold value is 1st Quartile minus 1.5 times IQR(Inter QuartileRange)
        
        Parameters:
        -----------
            feature: the range of values to be thresholded.
            
        Returns:
        -------
        A dictionary containing minimum threshold, maximum  threshold, Thresholded values
        
    '''
    feature = pd.Series(feature)
    
    q1, q3 = np.percentile(feature, [25, 75])
    IQR = q3 - q1
    
    min_threshold = q1 - 1.5*IQR
    max_threshold = q3 + 1.5*IQR
    
    thresholded_data = feature.apply(lambda x: min(max(min_threshold, x), max_threshold))
    
    return {'min_th': min_threshold, 'max_th': max_threshold, 'th_data': thresholded_data}
    