with open("conf_bach") as f:
    content = f.readlines()
lines = []
for line in content:
    lines.append(line.split(' '))
for line in lines:
    line[-1] = line[-1].strip()
    for info in line:
        if info == '':
            line.pop(line.index(info))

schedules = []
for line in lines:
    schedules.append(line[5])

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
daySchedule = {
    'Sun': '0111111',
    'Mon': '1011111',
    'Tue': '1101111',
    'Wed': '1110111',
    'Thu': '1111011',
    'Fri': '1111101',
    'Sat': '1111110',
}
startDay = 'Wed'
startkey = daySchedule.get(startDay)
print(startkey)
scheduleIndex = []
for schedule in schedules:
    if list_duplicates_of(schedules, schedule) not in scheduleIndex:
        scheduleIndex.append(list_duplicates_of(schedules, schedule))
print(schedules)