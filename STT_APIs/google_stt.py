# -*- coding: utf-8 -*-
import base64
import io
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import glob
import codecs

# only works on FLAC - ffmpeg -i input.mp3 -ac 1 output.flac

"""Transcribe the given audio file."""
def transcribe(filename):

    #phrases = [u'']

    out = codecs.open(filename+'.txt', 'w', encoding='utf-8')
    speech_file = filename
    client = speech.SpeechClient()

    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        #speech_contexts=[speech.types.SpeechContext(phrases=phrases)],
        language_code='es-CL')

    response = client.recognize(config, audio)
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        out.writelines(result.alternatives[0].transcript)
    out.close()

for filename in glob.iglob('*.flac'):
    transcribe(filename)
