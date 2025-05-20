#!/usr/bin/env python3
##Author: Ricky Tang
##Author ID: 104448246
# Date Created: 2025/05/25
import sys
if len(sys.argv) !=2: #checks amt of args (1 for script name, 2 for number)
    timer = 3 #default count is 3
else:
    timer = int(sys.argv[1]) #set timer variable to argument as integer
while timer > 0:

    print(timer) #print count
    timer -= 1 # count down 1 per loop
print('blast off!')
