import yaml
output = open("output1.xml", "w", encoding="UTF-8")
output.write('<Расписание>\n')
with open('input.yaml', "r", encoding="UTF-8") as fh:
    read_data = yaml.load(fh, Loader=yaml.SafeLoader)
    for i in read_data.keys():
        output.write('  <'+i.replace('(', '.', -1).replace(')', '.', -1).replace(' ', '', -1).replace(':', '', -1)+'>\n')
        for j in read_data.get(i):
            output.write('      <'+j.replace('/', '', -1).replace(' ', '', -1)+'>\n')
            output.write('          '+str(read_data.get(i).get(j))+'\n')
            output.write('      </'+j.replace('/', '', -1).replace(' ', '', -1)+'>\n')
        output.write('  </' + i.replace('(', '.', -1).replace(')', '.', -1).replace(' ', '', -1).replace(':', '', -1) + '>\n')

output.write('</Расписание>\n')
output.close()
