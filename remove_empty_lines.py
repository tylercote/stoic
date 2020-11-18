import sys

input = sys.argv[1]
output = 'clean_' + input;

read = open(input, 'r')
write = open(output, 'w')

lines = read.readlines()

for line in lines:
    if line != '\n':
        write.write(line)
