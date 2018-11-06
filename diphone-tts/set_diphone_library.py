
import re
import glob
import pickle

DIPHONES = {}

class Diphone(object):
    def setDiphone(self, filename, c_line, n_line):
        self.filename = filename
        self.c_diphone = re.findall(r'(\w+)\s\;\sscore', c_line)[0]
        self.n_diphone = re.findall(r'(\w+)\s\;\sscore', n_line)[0]
        self.c_seconds = re.findall(r'(\d+\.?\d+?)\s', c_line)[0]
        self.n_seconds = re.findall(r'(\d+\.?\d+?)\s', n_line)[0]
        diphone = self.c_diphone+'_'+self.n_diphone
        if diphone not in DIPHONES:
            DIPHONES[diphone] = [(filename, self)]
        else:
            DIPHONES[diphone] += [(filename, self)]

    def getTimes(self):
        return (self.c_seconds, self.n_seconds)
    def getFilename(self):
        return self.filename
    def getDiphone(self):
        return (self.c_diphone, self.n_diphone)


def setDiphoneLibrary(wav_path, lab_path):
    for filepath in glob.iglob(lab_path+'/*.lab'):
        # Checking wav exists for lab file
        wav_list = [wav_file.split('/')[-1].replace('.wav','') for wav_file in glob.iglob(wav_path+'/*.wav')]
        if filepath.split('/')[-1].replace('.lab','') in wav_list:
            data = open(filepath, 'r').read().split('\n')
            # Check format of the labels - most be HTK like
            # TODO
            # Range over each line to build diphone dictionary
            for l in range(0, len(data)-2):
                if l != len(data):
                    c_line = data[l]
                    n_line = data[l+1]
                    if re.findall(r'\d+\t\d+\t\w+', c_line):
                        diphone = Diphone()
                        diphone.setDiphone(filepath, c_line, n_line)
        # Warn if alike
        else:
            print filepath+' does not have wav file with the same name'

    # Save diphone dictionary
    pickle.dump(DIPHONES, open("diphone_library.pckl", "wb"))
    return DIPHONES


# Input path to wav folder and label folder
setDiphoneLibrary('./wav','./lab')
