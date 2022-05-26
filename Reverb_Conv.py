import os
from os import path
import librosa
import numpy as np
from scipy.fft import fft, ifft
import soundfile as sf


audio_data_path = "C:/Users/Spirelab/Desktop/Vowel_Triangle/Timit_VerySecret/Timit_Synth" #Audio Data path
rir_data_path = "C:/Users/Spirelab/Desktop/Vowel_Triangle/Timit_VerySecret/RIR_data" #RIR Data path
reverb_data_path = "C:/Users/Spirelab/Desktop/Vowel_Triangle/Timit_VerySecret/Reverb_data" #Reverbed Data Destination
os.chdir(audio_data_path)

audios = os.listdir(audio_data_path)
rirs = os.listdir(rir_data_path)
for i in audios :
    sound_path = os.path.join(audio_data_path,i)
    aud = i;
    y , sr = librosa.load(sound_path , sr = 16000)
    print(sound_path)
    temp = aud.replace(".wav", "_")
    print(temp)
    
    for j in rirs :
        rir_path = os.path.join(rir_data_path,j)
        print(rir_path)
        rir_aud = j
        rir_temp = rir_aud.replace("RVB2014_type1_rir_", "")
        y_rir , sr_rir = librosa.load(rir_path,sr = 16000)
        y_rir = y_rir[: len(y_rir) // 15]
        out_len = len(y) + len(y_rir) - 1
        y_fft = fft(y, n=out_len)
        y_rir_fft = fft(y_rir, n=out_len)
        y_reverb = np.real(ifft(np.multiply(y_fft, y_rir_fft)))[: len(y)]
        y_reverb = y_reverb / max(abs(y_reverb))
        reverbed_name = temp + rir_temp
        print(reverbed_name)
        reverb_dest = reverb_data_path + "/" + reverbed_name
        sf.write(reverb_dest , y_reverb,sr) #writing to destination folder
        
    
    
             

                             