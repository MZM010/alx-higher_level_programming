#!/usr/bin/python3
def multiple_returns(sentence):
    if isinstance(sentence, str):
        length = len(sentence)
        first = sentence[0]
        return length, first
