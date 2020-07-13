#!/usr/bin/env python3

import sys, subprocess

txt_file = sys.argv[1]
cmnd = []
with open(txt_file) as arg:
    for line in arg.readlines():
        old = line.strip()
        new = old.replace("jane", "jdoe")
        cmnd.append("mv {} {}".format(old, new))
for i in range(2):
    subprocess.run(cmnd[i], shell=True)