import noisereduce as nr
import librosa
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

baseDir = "c:/dev/Mafat"

def concatNoiseFiles():
    print("loading noise file...")
    dataNoise1, rate = librosa.load(baseDir+"/sample_files/ActualSounds/n1.wav")
    dataNoise2, rate = librosa.load(baseDir+"/sample_files/ActualSounds/n2.wav")
    dataNoise3, rate = librosa.load(baseDir+"/sample_files/ActualSounds/n3.wav")
    dataNoise4, rate = librosa.load(baseDir+"/sample_files/ActualSounds/n4.wav")
    dataNoise5, rate = librosa.load(baseDir+"/sample_files/ActualSounds/n3_upwards.wav")
    dataNoise6, rate = librosa.load(baseDir+"/sample_files/ActualSounds/n3_upwards2.wav")
    dataNoiseAll = np.concatenate((dataNoise5,dataNoise6))
    write(baseDir+'/sample_files/ActualSounds/n_all.wav', rate, dataNoiseAll)  # Save as WAV file 
    
def concatSoundFiles():
    print("loading sound file...")
    dataNoise1, rate = librosa.load(baseDir+"/sample_files/ActualSounds/s1.wav")
    dataNoise2, rate = librosa.load(baseDir+"/sample_files/ActualSounds/s2.wav")
    dataNoise3, rate = librosa.load(baseDir+"/sample_files/ActualSounds/s3.wav")
    dataNoise4, rate = librosa.load(baseDir+"/sample_files/ActualSounds/s4.wav")
    dataNoiseAll = np.concatenate((dataNoise1,dataNoise2,dataNoise3,dataNoise4))
    write(baseDir+'/sample_files/ActualSounds/s_all.wav', rate, dataNoiseAll)  # Save as WAV file 


def reduceSourceFile(sourceFile):    
    print("loading noise file...")
    dataNoiseAll, rate = librosa.load(baseDir+"/sample_files/ActualSounds/n_all.wav")
    print(rate)
    # load sound file (sound + noise) data + rate 
    #rate, data = wavfile.read("c:/temp/TEST.wav")
    print("loading sound file...")
    data, rate = librosa.load(sourceFile)
    print(rate)
    print("reducing noise from sound...")
    noise_reduce = nr.reduce_noise(audio_clip=data, noise_clip=dataNoiseAll, prop_decrease=1.0, verbose=False)

    print("Writing output file...")
    # write output sound without noise
    write(baseDir+'/sample_files/ActualSounds/reduced.wav', rate, noise_reduce)  # Save as WAV file 


concatNoiseFiles()
reduceSourceFile(baseDir+"/sample_files/ActualSounds/upwards.wav")
#print("playing output file...")
#sd.play(reduced_noise, rate)
#status = sd.wait()