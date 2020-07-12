import noisereduce as nr
from scipy.io import wavfile
import librosa
import sounddevice as sd
from scipy.io.wavfile import write

# load data
#rate, data = wavfile.read("c:/temp/TEST.wav")
data, rate = librosa.load("c:/temp/Regular.wav")
dataNoise, rate = librosa.load("c:/temp/Noise.wav")
# perform noise reduction
reduced_noise = nr.reduce_noise(audio_clip=data, noise_clip=dataNoise, prop_decrease=1.0, verbose=False)

write('c:/temp/reduced.wav', rate, reduced_noise)  # Save as WAV file 

# play the WAV file
sd.play(reduced_noise, rate)
status = sd.wait()