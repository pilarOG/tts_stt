# -*- coding: utf-8 -*-

from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError

'''Función para utilizar el TTS de Amazon y guardar un archivo de audio como resultado.
**Importante** requiere tener credenciales con permiso en ~/.aws/credentials
input_text (str): texto que se quiere sintetizar
file_name (str): nombre del archivo de audio generado
formato (str): mp3, wav, etc. (revisar documentacion)'''

def amazonTTS(input_text, file_name, formato):
    session = Session()
    polly = session.client("polly")
    voice = 'Penelope'
    response = polly.synthesize_speech(VoiceId=voice, Text=input_text, OutputFormat=formato)
    wav_file = open(file_name+'.'+formato, 'w')
    data = response['AudioStream'].read()
    wav_file.write(data)

# Ejemplo
# amazonTTS('hola', 'sample', 'mp3')
