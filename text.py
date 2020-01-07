import re
import random
from string import punctuation as punct, whitespace
from . import ifnone


parasites = {
    'нахуй', 'пиздец', 'ебать', 'блять', 'ахуеть', 'сука',
    'типа', 'кароче', 'получается', 'значит', 'вот', 'кста'
}


sep = punct + whitespace


get_words = lambda ws: list(ifnone(ws, parasites))


def rand_nahui(k, words=None):
    words = get_words(words)
    if random.random() < k:
        return random.choice(words)
    return ''


def suka_blyat(text, k=0.5, words=None):
    words = get_words(words)
    result = []

    def append_blyat():
        blyat = rand_nahui(k, words)
        if blyat:
            result.append(blyat)

    text = re.split(f'[{sep}]', text)
    append_blyat()
    for word in text:
        result.append(word)
        append_blyat()
    return ' '.join(result)


def del_punct(text):
    return re.sub('['+punct+']', '', text)
