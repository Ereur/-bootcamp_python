# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aamoussa <aamoussa@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/02/28 16:52:08 by aamoussa          #+#    #+#              #
#    Updated: 2022/02/28 17:38:36 by aamoussa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

i = 0
intiger = 0
if (len(sys.argv) > 2):
    print('more than one argument are provided')
if (len(sys.argv) == 2) :
    while (i < len(sys.argv[1])):
        if (ord(sys.argv[1][i]) > 58 and ord(sys.argv[1][i]) > 48):
            print('argument is not an integer')
            quit(),
        i = i + 1
    intiger = int(sys.argv[1])
    if (intiger == 0 ) :
        print ('Im Zero')
    elif (intiger % 2 == 0) :
        print ('Im Even')
    else :
        print('Im Odd')
