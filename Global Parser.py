from collections import Counter
import re
from typing import List, Any, Tuple


def Word_count():
    f = open('chat.log', "r+", encoding="utf-8-sig")
    wordcount = {}
    for word in f.read().split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    print(word, wordcount)
    return
Word_count()
