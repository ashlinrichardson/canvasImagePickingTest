#!/usr/bin/env python
import os, sys
words = open("words.txt").readlines()
s = "var words = ["; 
for word in words:
  s+="'"+(word.strip())+"'"+","
s+="];"
print s
