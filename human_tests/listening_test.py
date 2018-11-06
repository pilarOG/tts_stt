# -*- coding: utf-8 -*-
'''Script to run a listening test, in this case to compare 3 TTS systems with 10 samples'''

import os
import random

amazon = 'amazon_tts_X.mp3'
watson = 'watson_tts_X.wav.mp3'
bing = 'bing_tts_X.wav.mp3'

def playSample(n):

    s1 = u'Cuéntame si estás de acuerdo con lo que digo para conocerte mejor.'
    s2 = u'El pudú es un animal de la clase de los mamíferos. Son los miembros más pequeños de la familia de los cérvidos.'
    s3 = u'Hola, Soy Brainy! Qué alegría conocerte!'
    s4 = u'Miden entre 60 y 90 centímetros de largo y entre 30 y 40 centímetros de alto. Pesan entre 7 y 10 kilos. El color de los pudúes varía de café rojizo a grisáceo amarillento.'
    s5 = u'Muchas gracias por dejarme conocerte! Nos vemos pronto! Chao!'
    s6 = u'El megaterremoto de Valdivia de 1960, conocido también como el Gran terremoto de Chile, fue un sismo ocurrido el domingo 22 de mayo de 1960 a las 15:11 hora local.'
    s7 = u'Ayuda a Don José a ordenar los libros!'
    s8 = u'El agua del océano podría desplazarse de la costa, por lo que las conchas, la arena y las especies marinas podrían quedar expuestas de un momento a otro.'
    s9 = u'Cuéntame si estás de acuerdo o no con las frases!'
    s10 = u'Son animales que se alimentan exclusivamente de plantas, pastos, hierbas y vegetales en general. Hay muchos herbívoros que comen huevos y a veces, otras proteínas provenientes de animales.'

    samples = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]

    a = 'amazon_tts_X.mp3'.replace('X', str(n))
    w = 'watson_tts_X.wav.mp3'.replace('X', str(n))
    b = 'bing_tts_X.wav.mp3'.replace('X', str(n))
    l = [a,w,b]
    random.shuffle(l)

    print
    print 'Texto: \''+samples[n]+'\''
    print 'Muestra 1'
    os.system('afplay '+l[0])
    print 'Muestra 2'
    os.system('afplay '+l[1])
    print 'Muestra 3'
    os.system('afplay '+l[2])
    print

    variable = raw_input('¿Cuál te gustó más?: 1, 2 o 3 (Para volver a escuchar escribe \'repetir\'):    ').strip()

    if variable == 'repetir':
        print
        return playSample(n)
    if variable in ['1', '2', '3']:
        return variable+'\t'+l[0]+' '+l[1]+' '+l[2]+'\n'
    else:
        print 'Input incorrecto, repitiendo set'
        print
        return playSample(n)


for n in range(0, 10):
    save = open('sujeto18.txt', 'a')
    respuesta = playSample(n)
    save.writelines(str(n)+'\t'+respuesta)
save.close()
