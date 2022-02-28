# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aamoussa <aamoussa@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/02/28 15:43:54 by aamoussa          #+#    #+#              #
#    Updated: 2022/02/28 16:49:39 by aamoussa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


count = len(sys.argv)
i = 2

if (count > 1) :
    string = sys.argv[1]
    while (i < count):
        string = string + " " +sys.argv[i]
        i = i + 1
    string  = string[::-1]
    print (string)