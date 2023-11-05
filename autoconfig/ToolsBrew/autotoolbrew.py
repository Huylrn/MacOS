#!/usr/bin/env python3
import subprocess
def print_text():
    file = open('docs/help_brew.txt', 'r')
    print(file.read())
    file.close()

# check if brew installed or not
check_true = subprocess.call(['sh', 'cmd.sh', 'check'])
# 
if check_true == 0:
    import fn
else: 
    print_text()
