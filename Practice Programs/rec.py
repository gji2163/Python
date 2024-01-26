import sounddevice as sd
from scipy.io.wavfile import write

try:
    fs=10000*int(input("Enter quality(Default is 5):"))
except:    
    fs = 50000  # Sample rate

seconds = int(input("Enter duration in seconds:"))  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
print(type(myrecording[0]))
write(input("File Name:"), fs, myrecording)  # Save as WAV file

