import os
import random

lines = open('messages.txt').read().splitlines()
random.shuffle(lines)
counter=0

for entry in os.scandir('rawimages'):
    if (entry.path.endswith(".jpg") and entry.is_file()):

        print(entry.path)
        a1=random.randint(0,255)
        a2=random.randint(0,255)
        a3=random.randint(0,255)
        smallint=random.randint(1,12)
        medint=random.randint(1,50)
        counter+=1

        myline = lines[counter]
        myline = myline.replace('{smallint}',str(smallint))
        myline = myline.replace('{medint}',str(medint))
        points = 350 - (len(myline) * 10)

        cmd = f"convert " + entry.path + f" -pointsize {points} -font Space-Mono-Nerd-Font-Complete-Mono "
        cmd +=f"-fill rgba\({a1},{a2},{a3},1\) -gravity center -annotate {medint}x{medint}+0+0 "
        cmd +=f'"{myline}" output/' + os.path.basename(entry.path)
        os.system(cmd)

