#!/usr/bin/env python
import os,sys
a = os.system('find ./ -name "*inverte*.jpg" | xargs rm'); 
files = os.popen("ls -1 image*.jpg").readlines();
for file in files:
  a = os.system("convert -negate "+file.strip()+" "+file.strip()+"-inverted.jpg");


