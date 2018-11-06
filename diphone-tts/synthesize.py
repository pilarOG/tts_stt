
import re
from pydub import AudioSegment
import spanish_transcriber
import pickle
import set_diphone_library
import sys
import random

DIPHONES = pickle.load(open('diphone_library.pckl', 'rb'))

def synthesize(text):
    # Get diphone list
    transcription = []
    for word in text.split(' '):
        transcription += spanish_transcriber.transcribe(word)

    # Postlex rules
    # 2 subsequental equal sounds
    transcribed_diphones = []
    for n in range(0, len(transcription)):
        if n != len(transcription)-1 and transcription[n] == transcription[n+1]: pass
        else: transcribed_diphones.append(transcription[n])
    print transcribed_diphones

    sentence_diphones = []
    for p in range(0, len(transcribed_diphones)-1):
        if p != len(transcribed_diphones):
            diphone = transcribed_diphones[p]+'_'+transcribed_diphones[p+1]
            sentence_diphones.append(diphone)

    # Select diphones from database
    silence = AudioSegment.from_wav('./wav/silence.wav')
    generated_audio = AudioSegment.from_wav('./wav/silence.wav')
    for diphone in sentence_diphones:
        # Backoff rules
        if diphone not in DIPHONES:
            if 'sp_' in diphone:
                diphone = diphone.replace('sp_', 'sil_')

        # If diphone exists
        selected = random.choice(DIPHONES[diphone])
        target = selected[1]
        filename = selected[0]
        t1 = float(target.c_seconds) * 1000
        t2 = float(target.n_seconds) * 1000

        # Get audio slice
        target_file = AudioSegment.from_wav('./wav/'+filename.replace('.lab', '.wav').replace('./lab',''))
        slice_audio = target_file[t1:t2]
        generated_audio += slice_audio
    generated_audio += silence
    generated_audio.export('generated.wav', format="wav")

synthesize(sys.argv[1].decode('utf-8'))
