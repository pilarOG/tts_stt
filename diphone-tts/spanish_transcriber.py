# -*- coding: utf-8 -*-

def ltsRules(text):
    phones = []

    # letter sets
    letsets = {'LNS': ('l', 'n', 's'),
                'DNSR': ('d', 'n', 's', 'r'),
                'EI': ('e', 'i', 'é', 'í'),
                'AEIOUt': ('á', 'é', 'í', 'ó', 'ú'),
                'V': ('a', 'e', 'i', 'o', 'u'),
                'C': ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k',
                      'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's',
                      't', 'v', 'w', 'x', 'y', 'z'),
                'noQ': ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k',
                      'l', 'm', 'n', 'ñ', 'p', 'r', 's',
                      't', 'v', 'w', 'x', 'y', 'z'),
                'AV': ('a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú'),
                'SN': ('p', 't', 'k', 'n', 'm', 'ñ'),
                'LN': ('l', 'n'),
                'LR': ('l', 'r') }

    letters = list(text)
    for let in range(0, len(letters)):
        if letters[let] != '#' and letters[let] != ' ':
            c_let = letters[let]
            p_let = letters[let-1]
            pp_let = letters[let-2]
            n_let = letters[let+1]
            nn_let = letters[let+2]

            # replace Q
            if c_let == 'q' and n_let == 'u' and n_let == 'a': phones.append('k')
            elif c_let == 'q' and n_let == 'u': phones.append('k')
            elif c_let == 'u' and p_let == 'q': pass
            elif c_let == 'q': phones.append('k')

            # u vowel with g
            elif c_let == 'u' or c_let == 'ü' and p_let == 'g' and n_let == 'i': pass
            elif c_let == 'u' or c_let == 'ü' and p_let == 'g' and n_let == 'e': pass
            elif c_let == 'u' or c_let == 'ü' and p_let == 'g' and n_let == 'í': pass
            elif c_let == 'u' or c_let == 'ü' and p_let == 'g' and n_let == 'é': pass

            # stress
            elif c_let == 'á': phones.append('aS')
            elif c_let == 'é': phones.append('eS')
            elif c_let == 'í': phones.append('iS')
            elif c_let == 'ó': phones.append('oS')
            elif c_let == 'ú': phones.append('uS')

            # semivowels
            elif c_let == 'u' and n_let in letsets['AV']: phones.append('uSC')
            elif c_let == 'u' and p_let in letsets['AV']: phones.append('uSV')
            elif c_let == 'i' and n_let in letsets['AV']: phones.append('iSC')
            elif c_let == 'i' and pp_let in letsets['noQ']: phones.append('iSV')

            # y as vowel and w
            elif c_let == 'y' and n_let == '#': phones.append('i')
            elif c_let == 'y' and n_let in letsets['C']: phones.append('i')
            elif c_let == 'w' and n_let == 'u': phones.append('uSC')
            elif c_let == 'w': phones.append('u')

            # fricatives
            elif c_let == 's' and p_let in letsets['AV'] and n_let in letsets['C']: phones.append('h')
            elif c_let == 's' and p_let in letsets['AV'] and n_let == '#': phones.append('h')
            elif c_let == 'c' and p_let == 's': pass
            elif c_let == 'c' and n_let in letsets['EI']: phones.append('s')
            elif c_let == 'g' and n_let in letsets['EI']: phones.append('x')
            elif c_let == 'g': phones.append('x')

            # keep z cause we'll need it to get stress
            elif c_let == 'z' and p_let in letsets['AV'] and n_let in letsets['C']: phones.append('hz')
            elif c_let == 'z' and p_let in letsets['AV'] and n_let == '#': phones.append('hz')
            elif c_let == 'z': phones.append('s')

            # affricates
            elif c_let == 'c' and n_let == 'h': phones.append('ch')
            elif c_let == 'h' and p_let == 'c': pass
            elif c_let == 'l' and n_let == 'l': phones.append('ll')
            elif c_let == 'l' and p_let == 'l': pass
            elif c_let == 'y' and p_let in letsets['LN']: phones.append('ll')
            elif c_let == 'y' and p_let == '#': phones.append('ll')
            elif c_let == 'l' and n_let == 'l' and p_let in letsets['LN']: phones.append('ll')
            elif c_let == 'l' and p_let == 'l' and pp_let in letsets['LN']: pass

            # unvoiced stops
            elif c_let == 'p' and n_let == 's': pass
            elif c_let == 'c': phones.append('k')

            # voiced stops
            elif c_let == 'v' and p_let == '#': phones.append('b')
            elif c_let == 'v' and p_let in letsets['SN']: phones.append('b')
            elif c_let == 'v' and n_let in letsets['LR']: phones.append('b')

            # approximants
            elif c_let == 'b' and p_let in letsets['AV'] and n_let in letsets['AV']: phones.append('bA')
            elif c_let == 'v' and p_let in letsets['AV'] and n_let in letsets['AV']: phones.append('bA')
            elif c_let == 'd' and p_let in letsets['AV'] and n_let in letsets['AV']: phones.append('dA')
            elif c_let == 'g' and p_let in letsets['AV'] and n_let in letsets['AV']: phones.append('gA')
            elif c_let == 'r' and p_let in letsets['AV'] and n_let in letsets['AV']: phones.append('rA')
            elif c_let == 'y': phones.append('llA')

            # nasals
            elif c_let == 'ñ': phones.append('ñ')

            # laterals
            elif c_let == 'l' and n_let == 'l' and nn_let == '#': phones.append('l')
            elif c_let == 'l' and p_let == 'l' and n_let == '#': pass
            elif c_let == 'l' and n_let == 'l': phones.append('llA')
            elif c_let == 'l' and p_let == 'l': pass

            # vibrants
            elif c_let == 'r' and n_let == 'r': phones.append('rr')
            elif c_let == 'r' and p_let == 'r': pass
            elif c_let == 'r' and p_let == '#': phones.append('rr')
            elif c_let == 'r' and p_let in letsets['LNS']: phones.append('rr')

            # get rid of h
            elif c_let == 'h': pass

            # else
            else: phones.append(c_let)

    return phones


def syllabify(phones):
    syllables = []
    phones = ['#','#']+phones+['#','#']
    sylsets = {'V': ('aS', 'iS', 'uS', 'eS', 'oS', 'a', 'i', 'u', 'e', 'o',
                     'iSC', 'uSC', 'iSV', 'uSV'),
               'VV': ('aS', 'iS', 'uS', 'eS', 'oS', 'a', 'i', 'u', 'e', 'o'),
               'IUT': ('iS', 'uS'),
               'C': ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k',
                      'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's',
                      't', 'v', 'w', 'x', 'y', 'z'),
               'CC': ('bl', 'br', 'kl', 'kr', 'ks', 'dr', 'fl', 'fr', 'gl',
                      'gr', 'pl', 'pr', 'tl', 'tr'),
               'H': ('ia', 'ie', 'io', 'ua', 'ue', 'uo', 'ai', 'ei', 'oi', 'au',
                    'eu', 'ou', 'iu', 'ui','iaS', 'ieS', 'ioS', 'uaS', 'ueS', 'uoS',
                    'aSi', 'eSi', 'oSi', 'aSu', 'eSu', 'oSu', 'iuS', 'uiS') }

    for let in range(0, len(phones)):
        if phones[let] != '#':
            c_let = phones[let]
            p_let = phones[let-1]
            pp_let = phones[let-2]
            n_let = phones[let+1]
            nn_let = phones[let+2]

            # consonant clusters
            if c_let+n_let in sylsets['CC'] and n_let in sylsets['V']: syllables.append('-')

            # hiatus
            elif c_let+n_let in sylsets['H'] and p_let in sylsets['IUT']: syllables.append('-')

            # two strong vowels
            elif c_let in sylsets['VV'] and p_let in sylsets['VV']: syllables.append('-')

            # break other CC not allowed
            elif c_let in sylsets['C'] and p_let in sylsets['C'] and pp_let in sylsets['V'] and n_let in sylsets['V']: syllables.append('-')

            # usual CV
            elif c_let in sylsets['C'] and p_let in sylsets['V'] and n_let in sylsets['V']: syllables.append('-')

            syllables.append(c_let)

    return syllables


def transcribe(text):

    # lower case
    text = '##'+text.lower()+'##'
    # LTS rules
    phones = ltsRules(text)
    # syllabification
    syllables = syllabify(phones)

    return syllables



print transcribe('que es eso')
