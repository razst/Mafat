import sounddevice as sd
from scipy.io.wavfile import write
import soundfile as sf

# ****** RECORD ********
outFileName = input("please enter output file name (without .WAV). outfile directory is c:/temp: ")
outFileName = 'c:/temp/'+ outFileName + ".wav"
fs = 44100  # Sample rate
seconds = int(input("please enter number of seconds to record: "))
print("Start recording...")
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
print("Done recording...")
write(outFileName, fs, myrecording)  # Save as WAV file 


# ****** PLAY ********
print("Playing...")
# Extract data and sampling rate from file
data, fs = sf.read(outFileName, dtype='float32')  
sd.play(data, fs)
status = sd.wait()  # Wait until file is done playing
print("Done playing...")