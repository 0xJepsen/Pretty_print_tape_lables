import datetime


print('Example schedule: /usr/local/dumps/conf/bach')
fileName = raw_input("Enter backup schedule filename: ")
startDate = raw_input("Enter begin date (Example: Jan 01 1992): ")
startDate = 'Jan 01 1992'
fileName = 'conf/bach'
numberOfPages = input("Enter Number of pages (of 6 labels each): ")
outputFileName = raw_input("Enter output file name: ")
Server = fileName.split('/')[-1]
# print(Server)
data = []

startDateNum = datetime.datetime.strptime(startDate, '%b %d %Y')
tdelta = datetime.timedelta(days=1)


orderedDays = []
totalDays = 6*numberOfPages
for i in range(totalDays):
    orderedDays.append(startDateNum)
    startDateNum += tdelta
formatedOrderedDays = [day.strftime('%a %d %b %y') for day in orderedDays]

# reading the configuration file into list of lines and cleaning newline chars
lines = []
with open(fileName) as f:
    content = f.readlines()
    for line in content:
        lines.append(line.split(' '))
    for line in lines:
        line[-1] = line[-1].strip()
        while("" in line) :
            line.remove("")

# Absstacting schedules into a list
schedules = []
for line in lines:
    schedules.append(line[5])
# helper
def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

# 0111111 --> Sunday
# 1011111 --> Monday
# 1101111 --> Tuesdday
# 1110111 --> Wednesday
# ....

daySchedule = {
    'Sun': '0111111',
    'Mon': '1011111',
    'Tue': '1101111',
    'Wed': '1110111',
    'Thu': '1111011',
    'Fri': '1111101',
    'Sat': '1111110',
}


data.append(Server)
data.append(formatedOrderedDays)

zeroDumps = []
for day in data[1]:
    currentDay = day.split(' ')[0]
    startkey = daySchedule.get(currentDay)
    scheduleIndex = []
    for schedule in schedules:
        if list_duplicates_of(schedules, schedule) not in scheduleIndex:
            scheduleIndex.append(list_duplicates_of(schedules, schedule))

    ## ----Edge case for everyday zerosdumps ----##
    infoindex = []
    for schedule in schedules:
        for index in range(len(schedule)):
            if (startkey[index] == schedule[index]) and (schedule not in infoindex) and (startkey[index] == '0'):
                infoindex.append(schedule)

    dayZeroDumps = []
    for line in lines:
        for info in infoindex:
            if line[5] == info:
                dayZeroDumps.append(line[6] + ' ' + line[7])
    zeroDumps.append(dayZeroDumps)
for dump in zeroDumps:
    if len(dump) < 4:
        while len(dump) < 4:
            dump.append('                             ')
data.append(zeroDumps)

# Padding for dumps
dumpLineLength = len('                             ')
for index in range(len(data[2])):
    for jdex in range(len(data[2][index])):
        while len(data[2][index][jdex]) < dumpLineLength:
            data[2][index][jdex] += ' '

# Padding for Server
serverLength = len('Parsons')
while len(data[0]) < serverLength:
    data[0] += ' '

count = 0
i = 0
writtenPages = 0
while i < totalDays:
    linesleft = ['+--------------------------------------+',
    '|                                      |',
    '|  {} {}               |'.format(data[1][i],data[0]),
    '|                                      |',
    '|<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>|',
    '|                                      |',
    '|  {} {}               |'.format(data[1][i],data[0]),
    '|                                      |',
    '|  Zero Dumps:                         |',
    '|    {}     |'.format(data[2][i][0]),
    '|    {}     |'.format(data[2][i][1]),
    '|    {}     |'.format(data[2][i][2]),
    '|    {}     |'.format(data[2][i][3]),
    '|                                      |',
    '|                                      |',
    '|                                      |',
    '|                                      |',
    '|                                      |',
    '+--------------------------------------+']
    linesright = ['--------------------------------------+\n',
    '                                      |\n',
    '  {} {}               |\n'.format(data[1][(i+numberOfPages)%totalDays],data[0]),
    '                                      |\n',
    '<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>|\n',
    '                                      |\n',
    '  {} {}               |\n'.format(data[1][(i+numberOfPages)%totalDays],data[0]),
    '                                      |\n',
    '  Zero Dumps:                         |\n',
    '    {}     |\n'.format(data[2][(i+numberOfPages)%totalDays][0]),
    '    {}     |\n'.format(data[2][(i+numberOfPages)%totalDays][1]),
    '    {}     |\n'.format(data[2][(i+numberOfPages)%totalDays][2]),
    '    {}     |\n'.format(data[2][(i+numberOfPages)%totalDays][3]),
    '                                      |\n',
    '                                      |\n',
    '                                      |\n',
    '                                      |\n',
    '                                      |\n',
    '--------------------------------------+\n'
    ]
    label = list(zip(linesleft,linesright))
    f = open(outputFileName, 'a')
    for j in range(len(label)):
        f.writelines(label[j])
    i+= (2*numberOfPages)
    count += 1
    if count%3==0:
        f.writelines(['\n','\n','\n'])
        writtenPages +=1
        i = writtenPages
        if writtenPages == numberOfPages:
            break