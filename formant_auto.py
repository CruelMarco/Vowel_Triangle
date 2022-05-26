import parselmouth
import numpy as np
import pandas as pd
import os
import glob
from scipy.io import wavfile
import parselmouth as pm
import sys
import re
import statistics
from scipy.io.wavfile import write

from parselmouth.praat import call
from scipy.stats.mstats import zscore
from IPython.display import Audio
import librosa
dir = 'C:/Users/Spirelab/Desktop/Vowel_Triangle/subject_wise/test'

os.chdir(dir);

dir

file = os.listdir(dir)

formant_DF = pd.DataFrame(columns = ['ID' , 'F1' , 'F2'])
formant_data = pd.DataFrame(columns = ['ID' , 'F1' , 'F2'])
data = []
data_com = []

for file in file :
    d = os.path.join(dir,file)
    print(file)
    sound = pm.Sound(d)
    Audio(data = sound.values, rate = sound.sampling_frequency)
    
    pointProcess = call(sound, "To PointProcess (periodic, cc)",75,300)

    formants = call(sound, "To Formant (burg)", 0.0025, 5, 5500, 0.025, 50)

    numPoints = call(pointProcess, "Get number of points")
    
    f1_list = []
    f2_list = []
    
    
    for point in range(0,numPoints):
        point= point + 1;
        t = call(pointProcess, "Get time from index", point)
        f1 = call(formants, "Get value at time", 1, t, 'Hertz', 'Linear')
        f2 = call(formants, "Get value at time", 2, t, 'Hertz', 'Linear')
        f1_list.append(f1)
        f2_list.append(f2)
    
        
        
        #for i in range(len(phon)):
            #f1_mean[phon[i]] = str(statistics.mean(f1_list))
            #f2_mean[phon[i]] = str(statistics.mean(f2_list))
        #locals().update(f1_mean)
        #locals().update(f2_mean)
            
    
        #f1_mean = statistics.mean(f1_list)
        #f2_mean = statistics.mean(f2_list)
    f1_list = [f1 for f1 in f1_list if str(f1) != 'nan']
    
    f2_list = [f2 for f2 in f2_list if str(f2) != 'nan']
    
    f1_mean = statistics.mean(f1_list)
    f2_mean = statistics.mean(f2_list)
    
    print(file)
    
    print(f1_mean)
    print(f2_mean)
    
    name_split = file.split('_')
    name = name_split[0] + '_' + name_split[1]
    
    formant_DF  = pd.DataFrame([[name , f1_mean , f2_mean]], columns = ['ID' , 'F1' , 'F2'])
    
    print(formant_DF)
    
    formant_data = pd.concat([formant_data , formant_DF], ignore_index= True, axis = 0)
    
    print(formant_data)
    

    
    #data_com = data_com + data
    
    #formant_DF.loc[len(formant_DF)] = formant_DF
    
    #formant_data = pd.concat([formant_data , formant_DF], ignore_index= True, axis = 0)

            
    
    
    
    
    #data_com = data.append(data)
    #formant_data = pd.concat([formant_data,formant_DF], axis = 0)
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    

