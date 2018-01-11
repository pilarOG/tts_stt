# -*- coding: utf-8 -*-

from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError

'''Function to use Amazon TTS and save audio as a file.
**Important** it requieres credentials with permissions in ~/.aws/credentials
input_text (str): text to synthesize
file_name (str): name of file to save
formato (str): mp3, wav, etc. (check documentation)'''

def amazon_TTS(input_text, file_name, formato):
    session = Session()
    polly = session.client("polly")
    voice = 'Penelope' # Change the voice here, see documentation for full catalog, this is Spanish
    response = polly.synthesize_speech(VoiceId=voice, Text=input_text, OutputFormat=formato)
    wav_file = open(file_name+'.'+formato, 'w')
    data = response['AudioStream'].read()
    wav_file.write(data)

# Ejemplo
# amazon_TTS('hola', 'sample', 'mp3')
