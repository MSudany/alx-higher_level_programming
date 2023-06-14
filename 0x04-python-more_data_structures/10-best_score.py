#!usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_score = list(a_dictionary.keys())[0]
    for i in a_dictionary.keys():
        if a_dictionary[i] > a_dictionary[max_score]:
            max_score = i
    return max_score
