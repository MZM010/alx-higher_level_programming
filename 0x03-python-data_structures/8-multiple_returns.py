#!/usr/bin/python3
def multiple_returns(sentence):
    if isinstance(sentence, str):
        length = len(sentence)
        first = sentence[0]
        if not sentence:
            first = None
        return length, first
