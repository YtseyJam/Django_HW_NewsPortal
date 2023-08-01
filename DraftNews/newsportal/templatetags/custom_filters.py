from django import template

register = template.Library()


BANNED_WORDS = ['Маска', 'маска', 'маски', 'маска,', 'вид', 'пёс', ]


@register.filter()
def censor(a):
    """ требуется доработка фильтра"""
    try:
        a_split = a.split()

    except AttributeError:
        print("ERROR! Expected str-type")

    else:
        for word in a_split:
            if word in BANNED_WORDS:
                word_fix = word[0] + '*'*(len(word)-1)
                i = a_split.index(word)
                a_split[i] = word_fix
        a_split = ' '.join(a_split)

        return a_split
