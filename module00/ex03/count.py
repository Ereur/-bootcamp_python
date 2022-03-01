# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aamoussa <aamoussa@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/02/28 17:39:46 by aamoussa          #+#    #+#              #
#    Updated: 2022/03/01 14:36:54 by aamoussa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
def text_analyzer(str = 'Default') :
    "This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."
    lower_case = 0
    upper_case = 0
    spaces = 0
    i = 0
    punctuation = 0
    if (str == 'Default'):
        str = input("What is the text to analyze?\n")
        
    if (type(str) == int) :
        print('argument is not a string')
        quit()
   
    while (i < len(str)) :
        if (ord(str[i]) > 64 and ord(str[i]) < 91):
            upper_case = upper_case + 1
        elif (ord(str[i]) > 96 and ord(str[i]) < 123) :
            lower_case = lower_case + 1
        elif (ord(str[i]) == 32) :
            spaces = spaces + 1
        elif ((ord(str[i]) < 48 and ord(str[i]) > 32) or ord(str[i]) < 65 and ord(str[i]) > 57):
            punctuation = punctuation + 1
        i = i + 1
    print('The text contains',upper_case + lower_case + spaces + punctuation ,'character(s):\n')
    print('-', upper_case ,'upper letter(s) \n')
    print('-', lower_case ,'lower letter(s) \n')
    print('-', spaces ,'spaces letter(s) \n')
    print('-', punctuation ,'punctuation letter(s) \n')

if (len(sys.argv) > 2) :
    print('there is more than one argument')
    quit()
if (len(sys.argv) > 1) :
    text_analyzer(sys.argv[1])
