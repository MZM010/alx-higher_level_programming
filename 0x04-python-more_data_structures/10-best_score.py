#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or a_dictionary is None:
        return None
    Max = 0
    for i in range(len(a_dictionary)):
        for key, value in a_dictionary.items():
            if value > Max:
                Max = value
                max_key = key
    return max_key