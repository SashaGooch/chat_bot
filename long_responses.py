# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 02:21:42 2022

@author: gocan
"""

R_ADVICE = 'If I were you, I would type your question into the Google search bar!'
R_GAMBLE = 'I\'m a Bot, I\'m not allowed.'
R_COLOUR = 'I like all colours although blue is my favourite.'
R_CREATOR = 'Sasha did, he is the betsamurai!'
R_CRYPTO = 'Any of our ADA pairs listed on our website.'


import random

def unknown():
    response = ['Could you please re-phrase that?',
                '...', 
                'Sounds about right.', 
                'What does that mean?'][random.randrange(4)]
    return response

