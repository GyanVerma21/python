import sys
import re
filename = sys.argv[1]
fd = open(filename,'r')
no_of_expressions = int(fd.readline().replace('\n',''))#first line gives the no of lines of expression to be evaluated
while no_of_expressions:
    expression = fd.readline().replace('\n','')
    result = re.search("\d+([\s\S]+)\d+([\s\S]+)\d+",expression)
    print result.group(),result.groups()
    no_of_expressions = no_of_expressions - 1
    
        
