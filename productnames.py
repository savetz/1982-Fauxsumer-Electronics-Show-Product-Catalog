import random
import sys

company = open('companywords.txt').read().splitlines()
product = open('productwords.txt').read().splitlines()
postfix = open('postfixes.txt').read().splitlines()

if len(sys.argv) == 1:
    max = 10
else:
    max = int(sys.argv[1])

for x in range (0,max):
        name = random.choice(company).strip().title()
        name += random.choice(company).strip().title()
        if(random.randint(1,3) == 1):
            name += random.choice(postfix).strip()
        #name = name.title()
        name += "," + random.choice(product).strip().title()
        if(random.randint(1,3) == 1):
            name += random.choice(postfix).strip()
        if(random.randint(1,3) == 1):
            name += " " + str(random.randint(1,99))
            while(random.randint(1,2) == 1):
                name += "0"
        print(name)

