import re

input = open("input.yaml", "r", encoding="UTF-8")
output = open("output2.xml", "w", encoding="UTF-8")

pat1 = r'"[а-яА-я():\s\w]+":$'
pat2 = r'(?<=^\s\s)[а-яА-Я\.\/\s]+(?<!:)'
pat3 = r'(?<=[а-я]{2}:\s).+$'
lastline = ''

output.write('<Расписание>\n')

condition = True

for i in input.readlines():
    line = i.rstrip()
    if line == '':
        condition = True
        output.write("  </"+lastline+">\n\n")
    else:
        if condition == True:
            condition = False
            line = re.search(pat1, line)
            line = line.group().replace('(', '.', -1).replace(')','.', -1).replace(' ', '', -1).replace(':', '', -1).replace('"', '', -1)
            output.write("  <"+line+">\n")
            lastline = line
        else:
            tag1 = re.search(pat2, line)
            tag1 = tag1.group().replace('/', '', -1).replace(' ', '', -1)
            tag2 = re.search(pat3, line)
            tag2 = tag2.group()

            output.write('    <' + tag1 + '>\n')
            output.write('        ' + tag2 + '\n')
            output.write('    </' + tag1 + '>\n')

output.write("  </"+lastline+">\n")
output.write('</Расписание>')

input.close()
output.close()
