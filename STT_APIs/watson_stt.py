# -*- coding: utf-8 -*-
from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1
import glob
import codecs

speech_to_text = SpeechToTextV1(
    username=USERNAME
    password=PASSWORD
    x_watson_learning_opt_out=False)

for filename in glob.iglob('*.wav'):
    
    #keys = [u'']
    out = codecs.open(filename+'.txt', 'w', encoding='utf-8')
    with open(filename,'rb') as audio_file:
        response = speech_to_text.recognize(audio_file, content_type='audio/wav', model='es-ES_BroadbandModel',
        #keywords=keys, keywords_threshold=0.5
        )
        if response['results'] != []:
            out.write(response['results'][0]['alternatives'][0]['transcript'])
        else:
            pass
        out.close()
