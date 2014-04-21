import sys
import re
filename = sys.argv[1]
fd = open(filename,'r')
no_of_expressions = int(fd.readline().replace('\n',''))#first line gives the no of lines of expression to be evaluated
while no_of_expressions:
    expression = fd.readline().replace('\n','')

    result = re.search("(\d+)([\s\S]+)(\d+)([\s\S]+)(\d+)",expression)
    no_of_expressions = no_of_expressions - 1
    first_pattern = '('+result.groups()[0]+result.groups()[1]+result.groups()[2]+')'+result.groups()[3]+result.groups()[4]
    second_pattern = result.groups()[0]+result.groups()[1]+'('+result.groups()[2]+result.groups()[3]+ result.groups()[4]+')'
    print first_pattern,second_pattern
    if eval(first_pattern) > eval(second_pattern):
        print eval(first_pattern)
    else:
        print eval(second_pattern)
    
    
        
