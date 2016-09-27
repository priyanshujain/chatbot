#########################################################################################
##
##
##
##
#########################################################################################
#import elizachat
from elizachat import eliza_chat
#import rudechat
from rudechat import rude_chat
#import warchat
from warchat import suntsu_chat
#import zenchat
from zenchat import zen_chat
#import casualchat
from casualchat import iesha_chat

import random
import re

print '='*72
print "\n"
print "Talk to the program by typing in plain English, using normal upper-"
print 'and lower-case letters and punctuation.  Enter "quit" when done.'
print '='*72
print "Hello.  How are you feeling today?"


def main():

  while True:
        statement = raw_input("> ")
        x = random.randint(1,5)
        if x == 1 :
            print eliza_chat(statement)

        elif x == 2:
            print rude_chat(statement)

        elif x == 3 :
            print suntsu_chat(statement)

        elif x == 4:
            print iesha_chat(statement)

        else:
            print zen_chat(statement)

        if statement == "quit":
            break

if __name__ == "__main__":
    main()
