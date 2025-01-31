#!/usr/bin/env python3
# Author ID: 151649225

import subprocess

def free_space():
    result = subprocess.run("df -h | grep '/$' | awk '{print $4}'", 
                            shell=True, capture_output=True, text=True)
    return result.stdout.strip()

print(free_space())