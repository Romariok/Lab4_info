input = open("input.yaml", "r", encoding="UTF-8")
output = open("output.xml", "w", encoding="UTF-8")
condition = True
lastline = ''
numdots = 0

output.write('<Расписание>\n')
for i in input.readlines():
    line = i.rstrip()
    if line == '':
        condition = True
        output.write("  </"+lastline+">\n\n")
    else:
        if condition == True:
            condition = False
            line = line[1:len(line)-2]
            line = line.replace('(', '.', -1).replace(')','.', -1).replace(' ', '', -1).replace(':', '', -1)
            output.write("  <"+line+">\n")
            lastline = line
        else:
            line = line[1:len(line)].replace('/', '', -1)
            numdots = line.find(':')
            tag1 = line[1:numdots].replace(' ', '', -1)
            tag2 = line[numdots+2:]
            output.write('    <'+tag1+'>\n')
            output.write('        '+tag2+'\n')
            output.write('    </'+tag1+'>\n')

output.write("  </"+lastline+">\n")
output.write('</Расписание>')

input.close()
output.close()
