import os
import re
import subprocess
from pathlib import Path
import glob
import random

file = open('productnames-output.txt', 'r')
productnames = file.readlines()
file.close()
random.shuffle(productnames)

file = open('cities.txt','r')
cities = file.readlines()
file.close()
random.shuffle(cities)

file = open("prepositions.txt","r")
prepositions = file.readlines()
file.close()

printtechniques = ["daisy wheel","inkjet","bubble jet","impact matrix print head","dot matrix","none","proprietary","impact-cylindrical wheel","moving head matrix","rotating belt","thermal","electro sensitive"]
yesno = ["yes","no"]
codes = ["8-bit ASCII","7-bit ASCII","EBCDIC","Hex","binary","TTY","numeric","RTTY","Baudot"]
cpl = ["40","80","132","136","40","80","132","136","40","80","132","136","infinite"]
compares = ["Compare to","Obsoleted by","Closest competition","Better specs than","Stolen concept from","Almost as good as","Product we hate most"]

out = open('pages-output.md',"w")

pix = glob.glob(os.path.join('productimages', '*'))
random.shuffle(pix)
print("Found " + str(len(pix)) + " images")

#Sentence plucker stolen from
#https://stackoverflow.com/questions/35973422/get-random-sentences-from-a-set-of-text-files
sentences = []
with open('rawtext.txt') as f:
    sentences += re.findall(r".*?[\.\!\?]+", f.read())

counter = 0

for f in pix:
    #print(f)
    out.write("# " + productnames[counter].replace(","," "))
    out.write("![](" + pix[counter] + ")" + "\n\n")

    out.write("Find us at booth " + str(random.randint(-1,10000)))
    out.write(" (" + random.choice(prepositions).strip() + " booth " + str(random.randint(-1,10000)) + ")\n")

    out.write("## Specifications\n\n")
    out.write("Manufacturer: " + productnames[counter].split(',')[0] + " (" + cities[counter].split(",")[1] + ", " + cities[counter].split(",")[2]+ ")")
    out.write("\n\nModel name: " + productnames[counter].split(',')[1])
    out.write("\nPrinting technique: " + random.choice(printtechniques))
    out.write("\n\nPrinting speed: " + str(random.randint(0,240)) + "0 characters per second")
    out.write("\n\nLower case available: " + random.choice(yesno))
    out.write("\n\nTransmission code: " + random.choice(codes))
    out.write("\n\nCharacters per line: " + random.choice(cpl))
    out.write("\n\nInternal buffer: " + random.choice(yesno))
    out.write("\n\nWeight: " + str(random.randint(1,500)) + " lbs.")
    out.write("\n\nPrice: $" + str(random.randint(33,10000)))
    out.write("\n\nMonthly service contract: $" + str(random.randint(0,5000)))
    out.write("\n\nYear introduced: " + str(random.randint(1959,1982)))
    out.write("\n\nApproximate number installed: " + str(random.randint(0,2000)))
    out.write("\n\n" + random.choice(compares) + ": " + random.choice(productnames).replace(","," "))
    out.write("\n")

    out.write('## Key Features\n\n')
    selected = random.sample(sentences, 2)
    out.write(''.join(selected))

    out.write('\n\n## Product Notes\n\n')
    selected = random.sample(sentences, 12)
    out.write(''.join(selected))

    out.write("\n\n## Sample Output\n\n    ")
    sample = subprocess.run(['fortune', '-s', "-n65"], stdout=subprocess.PIPE).stdout.decode('utf-8')
    sample = sample.replace("\n", "\n    ")
    sample += "\n\n"
    out.write(sample)

    counter += 1
