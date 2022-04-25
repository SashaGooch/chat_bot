# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 02:18:31 2022

@author: gocan
"""

# Chat Bot.

import re
import long_responses as long

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True       # 3.Boolean
    
    # 4.Counts how many words are in each message
    for word in user_message:
        if word in recognised_words:
            message_certainty +=1
            
    # 5.Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))
    
    # 6.Checks that the required words are in the string
    for word in required_words:
        if word not in required_words:
            has_required_words = False
            break
     
    # 7.Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0
 
    
def check_all_messages(message):    # Step 8
    highest_prob_list = {}
    
    # 9.Simplest way of adding responses to the above dictionary
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list  # Used in nested
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)
        # Above is a key, value pairing
        
    # 10.Responses------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'heya', 'sup', 'yo'], single_response=True)
    response('See you!', ['bye', 'goodbye', 'cya'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thanks', 'thank', 'thx'], single_response=True)
    response('Talking to you..', ['what', 'are', 'you', 'doing'], required_words=['what'])
    response('PLS don\'t swear.', ['you', 'off'], required_words=['fuck', 'cunt', 'bitch', 'slut'])
    #response()
    
    
    # 12.Longer responses-----------------------------------------------------------------------------
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_GAMBLE, ['allowed', 'like', 'know', 'do'], required_words=['gamble', 'gambling'])
    response(long.R_COLOUR, ['colour', 'color', 'what', 'which'],  required_words=['colour', 'color'])
    response(long.R_CREATOR, ['who', 'created', 'built', 'you'], required_words=['created', 'built'])
    response(long.R_CRYPTO, ['what', 'which', 'crypto', 'currency'], required_words=['crypto',  'currency'])
    response(long.R_ADVICE, ['what', 'is'], required_words=['is'])
    
    
    # 11.Testing the responses
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # return best_match

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match
    


# 2.Used to get responses firstly split the message into an array
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

# 1.Testing the response system, create infinite while true loop to always get responses
while True:
        print('Bot: ' + get_response(input('You: ')))
    