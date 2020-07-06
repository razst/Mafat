import sounddevice as sd
from scipy.io.wavfile import write
import soundfile as sf


fs = 44100  # Sample rate
seconds = 10  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('c:/temp/Regular.wav', fs, myrecording)  # Save as WAV file 

filename = 'c:/temp/Regular.wav'
# Extract data and sampling rate from file
data, fs = sf.read(filename, dtype='float32')  
sd.play(data, fs)
status = sd.wait()  # Wait until file is done playing