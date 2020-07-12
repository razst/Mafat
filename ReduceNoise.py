import noisereduce as nr
import librosa
import sounddevice as sd
from scipy.io.wavfile import write

baseDir = "c:/dev/Mafat"
# load sound file (sound + noise) data + rate 
#rate, data = wavfile.read("c:/temp/TEST.wav")
print("loading sound file...")
data, rate = librosa.load(baseDir+"/sample_files/ActualSounds/s4.wav")
# load noise only file
print("loading noise file...")
dataNoise, rate = librosa.load(baseDir+"/sample_files/ActualSounds/n4.wav")
# perform noise reduction
print("reducing noise from sound...")
reduced_noise = nr.reduce_noise(audio_clip=data, noise_clip=dataNoise, prop_decrease=1.0, verbose=False)
reduced_noise = nr.reduce_noise(audio_clip=reduced_noise, noise_clip=dataNoise, prop_decrease=0.75, verbose=False)

print("Writing output file...")
# write output sound without noise
write(baseDir+'/sample_files/ActualSounds/reduced4_twice_0.75.wav', rate, reduced_noise)  # Save as WAV file 

# print("playing output file...")
# # play the WAV file 
# sd.play(reduced_noise, rate)
# status = sd.wait()