import os
import wave
from pydub import AudioSegment
import pylab

def graph_spectrogram(wav_file):
    sound_info, frame_rate = get_wav_info(wav_file)
    pylab.figure(num=None, figsize=(19, 12))
    pylab.subplot(111)
    pylab.title('spectrogram of %r' % wav_file)
    pylab.specgram(sound_info, Fs=frame_rate)
    pylab.savefig('hello.png')


def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'Int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate

def init(mp3_file ,wav_file = 'hello.wav'):
    AudioSegment.from_mp3(mp3_file).export(wav_file, format="wav")
    graph_spectrogram(wav_file)

if __name__ == '__main__':
    init()
    
