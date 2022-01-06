# -*- coding: UTF-8 -*-
# DNA tollset/code testing file
from DNAToolkits import *
import random

# 大写转化，输出结果
#rndDNAStr = "ATTTCGttt"
#print(validateSeq(rndDNAStr))

# creating a random DNA sequence for testing:
randDNAStr = ''.join([random.choice(Nucleotides)
                    for nuc in range(50)])
print(validateSeq(randDNAStr))

# 碱基计数
print(countNucFrequency(randDNAStr))

