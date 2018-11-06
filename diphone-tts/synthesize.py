
import re
from pydub import AudioSegment

DIPHONES = {}

class Diphone(object):

    def __init__(self, filename, c_line, n_line):
        self.c_diphone = re.findall(r'(\w+)\s\;\sscore', c_line)[0]
        self.c_seconds = re.findall(r'(\d+\.?\d+?)\s', c_line)[0]
        self.n_diphone = re.findall(r'(\w+)\s\;\sscore', n_line)[0]
        self.n_seconds = re.findall(r'(\d+\.?\d+?)\s', n_line)[0]
        diphone = self.c_diphone+'_'+self.n_diphone
        if diphone not in DIPHONES:
            DIPHONES[diphone] = [(filename, self)]
        else:
            DIPHONES[diphone] += [(filename, self)]


class GetDiphoneTimes(object):
    def __init__(self, filename):
        data = open(filename, 'r').read().split('\n')
        for l in range(0, len(data)-2):
            if l != len(data):
                c_line = data[l]
                n_line = data[l+1]
                if re.findall(r'\d+\t\d+\t\w+', c_line):
                    Diphone(filename, c_line, n_line)

def transcribe(text):
    transcription = ['oS','b_cl','b','r','a','sp','l','aS','r','gA','a']
    return transcription


def main():

    transcription = transcribe('asdasd')
    sentence_diphones = []
    for p in range(0, len(transcription)-1):
        if p != len(transcription):
            diphone = transcription[p]+'_'+transcription[p+1]
            sentence_diphones.append(diphone)
    print sentence_diphones

    generated_audio = AudioSegment.from_wav('start.wav')
    for diphone in sentence_diphones:
        target = DIPHONES[diphone][0][1]
        filename = DIPHONES[diphone][0][0]
        t1 = float(target.c_seconds) * 1000
        t2 = float(target.n_seconds) * 1000
        target_file = AudioSegment.from_wav(filename.replace('.lab', '_5.wav'))
        slice_audio = target_file[t1:t2]
        generated_audio += slice_audio

    generated_audio.export('generated.wav', format="wav")


GetDiphoneTimes('chilean_n0001.lab')
main()
