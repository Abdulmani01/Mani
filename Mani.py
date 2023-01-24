import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://facebook.com/groups/1110694166194022/')
 
bit = platform.architecture()[0]
if bit == '64bit':
    import M1
elif bit == '32bit':
    import M2
 
