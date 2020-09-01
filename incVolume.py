from pydub import AudioSegment
from pydub.playback import play

baseDir = "c:/dev/Mafat"

song = AudioSegment.from_wav(baseDir+'/sample_files/ActualSounds/reduced.wav')

# boost volume by 6dB
louder_song = song + 20

#save louder song 
louder_song.export(baseDir+'/sample_files/ActualSounds/loud.wav', format='wav')