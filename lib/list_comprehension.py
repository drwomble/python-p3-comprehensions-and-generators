#!/usr/bin/env python3

def return_evens(num_list):
    only_evens = [num for num in num_list if (num % 2 == 0)]
    return only_evens

def make_exclamation(sentence_list):
    new_list = [(f"{string}!") for string in sentence_list]
    return new_list