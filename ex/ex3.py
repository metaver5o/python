# -*- coding: utf-8 -*-

# this lesson was great to paste operations into python and use it as a calculator
# 
# mkdir /opt/code/; ln -s /code ~/code/
# cd ~/code/; git clone your.python.git.repo.comes.here
# docker pull python:2.7
# docker run -ti --name py -v /opt/code/:/opt/code/ python:2.7
# docker exec py python /opt/code/repo/file.py 
# docker attach py #run your py 

print "I will now count my chickens:"

print "Hens", 25 + 30 / 6

print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2

print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2

print "Is it greater or equal?", 5 >= -2

print "Is it less or equal?", 5 <= -2


