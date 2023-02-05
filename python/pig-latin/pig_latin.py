"""
Pig Latin
"""
def translate(text):
    """:param text: string
    :return: string
    """
    vowels = 'aeiou'
    words = text.split()
    result = []
    for word in words:
        if word[0] in vowels:
            result.append(word + 'ay')
        elif word[0:2] == 'xr' or word[0:2] == 'yt':
            result.append(word + 'ay')
        elif word[0] not in vowels and word[1:3] == 'qu':
            result.append(word[3:] + word[0:3] + 'ay')
        elif word[0:3] == 'sch' or word[0:3] == 'thr':
            result.append(word[3:] + word[0:3] + 'ay')
        elif word[0:2] == 'ch' or word[0:2] == 'th' or word[0:2] == 'qu':
            result.append(word[2:] + word[0:2] + 'ay')
        elif word[0] not in vowels and word[1] == 'y':
            result.append(word[1:] + word[0] + 'ay')
        elif 'y' in word and word.index('y') > 0:
            result.append(word[word.index('y'):] + word[:word.index('y')] + 'ay')
        else:
            result.append(word[1:] + word[0] + 'ay')
    return ' '.join(result)
