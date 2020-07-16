import noisereduce as nr
import librosa
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

baseDir = "c:/dev/Mafat"



def reduceSourceFile(sourceFile):    
    print("loading noise file...")
    dataNoise1, rate = librosa.load(baseDir+"/sample_files/ActualSounds/n1.wav")
    dataNoise2, rate = librosa.load(baseDir+"/sample_files/ActualSounds/n2.wav")
    dataNoise3, rate = librosa.load(baseDir+"/sample_files/ActualSounds/n3.wav")
    dataNoise4, rate = librosa.load(baseDir+"/sample_files/ActualSounds/n4.wav")
    dataNoiseAll = np.concatenate((dataNoise1,dataNoise2,dataNoise3,dataNoise4))
     


    # load sound file (sound + noise) data + rate 
    #rate, data = wavfile.read("c:/temp/TEST.wav")
    print("loading sound file...")
    data, rate = librosa.load(sourceFile)

    print("reducing noise from sound...")
    noise_reduce = nr.reduce_noise(audio_clip=data, noise_clip=dataNoiseAll, prop_decrease=1.0, verbose=False)

    print("Writing output file...")
    # write output sound without noise
    write(baseDir+'/sample_files/ActualSounds/reduced.wav', rate, noise_reduce)  # Save as WAV file 


reduceSourceFile(baseDir+"/sample_files/ActualSounds/s3.wav")
# print("playing output file...")
# # play the WAV file 
# sd.play(reduced_noise, rate)
# status = sd.wait()