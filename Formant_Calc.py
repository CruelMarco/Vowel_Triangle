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

dir = 'C:/Users/Spirelab/Desktop/Vowel_Triangle/Vowel_Synth/'

os.chdir(dir);

dir
file = os.listdir(dir)

wav = os.path.join(dir, file[1])

sound = pm.Sound(wav)

Audio(data = sound.values, rate = sound.sampling_frequency)

pointProcess = call(sound, "To PointProcess (periodic, cc)",75,300)

formants = call(sound, "To Formant (burg)", 0.0025, 5, 5500, 0.025, 50)

numPoints = call(pointProcess, "Get number of points")



f1_list = []
f2_list = []


for point in range(0, numPoints):
    point += 1
    t = call(pointProcess, "Get time from index", point)
    f1 = call(formants, "Get value at time", 1, t, 'Hertz', 'Linear')
    f2 = call(formants, "Get value at time", 2, t, 'Hertz', 'Linear')
    
    f1_list.append(f1)
    f2_list.append(f2)
    
f1_list = [f1 for f1 in f1_list if str(f1) != 'nan']
f2_list = [f2 for f2 in f2_list if str(f2) != 'nan']

f1_mean = statistics.mean(f1_list)
f2_mean = statistics.me/an(f2_list)


