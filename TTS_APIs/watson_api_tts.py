# -*- coding: utf-8 -*-
import urllib
import requests
import json

'''Function to use Watson TTS and save audio as file.
input_text (str): text to synthesize
file_name (str): nombre del archivo de audio generado
formato (str): mp3, wav, etc. (revisar documentacion)'''

def watson_TTS(input_text, file_name, formato):
    credentials = (USERNAME, PASSWORD) # Get the credentials when you create an instance of Watson TTS
    voice = 'es-LA_SofiaVoice' # Change voice here, this is spanish
    data = open(file_name+'.'+formato, 'wb')
    text = urllib.quote(input_text.encode('utf-8'))
    r = requests.get(url='https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize?accept=audio/'+formato+'&text='+text+u'&voice='+voice, auth=credentials, headers={'output':file_name})
    audio = r.content
    data.write(audio)
    data.close()

# Ejemplo
# watson_TTS('hola', 'sample', 'mp3')
