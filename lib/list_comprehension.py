#!/usr/bin/env python3

def return_evens(num_list):
    even_list = [n for n in num_list if n % 2 == 0]
    if len(even_list) == 0:
        print([])
        return []
    else:
        print(even_list)
        return even_list
    
return_evens([1,25])

def make_exclamation(sentence_list):
    final_list = [n + "!" for n in sentence_list]
    if final_list:
        print(final_list)
        return final_list
    else:
        print([])
        return []

make_exclamation(["Hello", "I am doing great","Python is fun"])