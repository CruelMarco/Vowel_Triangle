# -*- coding: utf-8 -*-
"""
Created on Thu May 19 14:53:37 2022

@author: Spirelab
"""
import os as os
import numpy as np
import scipy.signal
from spectrum import aryule
from numpy.random import randn
import soundfile as sf
import librosa
from pylab import plot, axis, xlabel, ylabel, grid, log10
import scipy.signal
from spectrum import arma_estimate, arma2psd, Periodogram,parma
from spectrum import WelchPeriodogram
from pylab import log10, linspace, plot, xlabel, ylabel, legend, randn, pi

from spectrum import Periodogram, data_cosine

#data = data_cosine(N=1024, A=0.1, sampling=1024, freq=200)

dir = os.chdir('C:/Users/Spirelab/Desktop/Vowel_Triangle/Timit_VerySecret/Reverb_data')

file = os.listdir(dir)

audio = file[2]

sig,fs = librosa.load(audio)

AR_order = 15

MA_order = 15

lag = 2*AR_order

p1 = Periodogram(sig,sampling = fs)

p = parma(sig, AR_order, MA_order, lag, NFFT = fs, sampling=fs)

p1.plot(norm = True , color = 'blue' , linewidth = 1)

p.plot(norm=True, color='red', linewidth=2)

legend(["signal", "Arma order = {}".format(AR_order)])
