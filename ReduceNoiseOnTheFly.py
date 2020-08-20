import sounddevice as sd
from scipy.io.wavfile import write
import soundfile as sf
import librosa
import numpy as np
import noisereduce as nr

baseDir = "c:/dev/Mafat"
SaveFile = True

def reduceSourceFile(data):    
    print("loading noise file...")
    dataNoiseAll, rate = librosa.load(baseDir+"/sample_files/ActualSounds/n_all.wav")

    data = (data[:,0] + data[:,1]) / 2

    print("reducing noise from sound...")
    noise_reduce = nr.reduce_noise(audio_clip=data, noise_clip=dataNoiseAll, prop_decrease=1.0, verbose=False)
    if SaveFile:
        write(baseDir+'/sample_files/ActualSounds/reduce.wav', rate, noise_reduce)  # Save as WAV file 

    return noise_reduce

# ****** RECORD ********
fs = 44100  # Sample rate
seconds = int(input("please enter number of seconds to record: "))
print("Start recording...")
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
print("Done recording...")
if SaveFile:
    write(baseDir+'/sample_files/ActualSounds/NotReduced.wav', fs, myrecording)  # Save as WAV file if SaveFile = True


print("Playing...")
sd.play(reduceSourceFile(myrecording), fs)
status = sd.wait()  # Wait until file is done playing
print("Done playing...")
