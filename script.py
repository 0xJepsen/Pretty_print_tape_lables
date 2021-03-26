import datetime


# print('Example schedule: /usr/local/dumps/conf/bach')
# fileName = input("Enter backup schedule filename: ")
# startDate = input("Enter begin date (Example: Jan 01 1992): ")
startDate = 'Jan 01 1992'
# numberOfPages = input("Enter Number of pages (of 6 labels each): ")
# outputFileName = input("Enter output file name: ")
# Server = fileName.split('/')[-1]
# print(Server)

startDateNum = datetime.datetime.strptime(startDate, '%b %d %Y')
print(startDateNum)
formatedStartDate = startDateNum.strftime('%a %d %b %y')
startDay = formatedStartDate.split(' ')[0]
Server = 'chopin'

tdelta = datetime.timedelta(days=1)

if (Server=='chopin'):
    print('+--------------------------------------+--------------------------------------+')
    print('|                                      |                                      |')
    print('|  {} Chopin                |  {} Chopin                |').format(formatedStartDate,formatedStartDate)
    print('|                                      |                                      |')
    print('|<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>|<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>|')
    print('|                                      |                                      |')
    print('|  {} Chopin                |  {} Chopin                |').format(formatedStartDate,formatedStartDate)
    print('|                                      |                                      |')
    print('|  Zero Dumps:                         |  Zero Dumps:                         |')
    print('|                                      |                                      |')
    print('|                                      |                                      |')
    print('|                                      |                                      |')
    print('|                                      |                                      |')
    print('|                                      |                                      |')
    print('|                                      |                                      |')
    print('|                                      |                                      |')
    print('|                                      |                                      |')
    print('|                                      |                                      |')
    print('+--------------------------------------+--------------------------------------+')



elif (Server=='bach'):
    print('+--------------------------------------+--------------------------------------+')
    print('|                                      |                                      |')
    print('|  {} Bach                  |  {} Bach                  |').format(formatedStartDate,formatedStartDate)
    print('|                                      |                                      |')
    print('|<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>|<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>|')
    print('|                                      |                                      |')
    print('|  {} Bach                  |  {} Bach                  |').format(formatedStartDate,formatedStartDate)
    print('|                                      |                                      |')
    print('|  Zero Dumps:                         |  Zero Dumps:                         |')
    print('|                                      |                                      |')
    print('|                                      |                                      |')
    print('|                                      |                                      |')
    print('|                                      |                                      |')
    print('|                                      |                                      |')
    print('|                                      |                                      |')
    print('|                                      |                                      |')
    print('|                                      |                                      |')
    print('|                                      |                                      |')
    print('+--------------------------------------+--------------------------------------+')

elif (Server=='parsons'):
    print('+--------------------------------------+--------------------------------------+')
    print('|                                      |                                      |')
    print('|  {} Parsons               |  {} Parsons               |').format(formatedStartDate,formatedStartDate)
    print('|                                      |                                      |')
    print('|<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>|<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>|')
    print('|                                      |                                      |')
    print('|  {} Parsons               |  {} Parsons               |').format(formatedStartDate,formatedStartDate)
    print('|                                      |                                      |')
    print('|  Zero Dumps:                         |  Zero Dumps:                         |')
    print('|                                      |                                      |')
    print('|                                      |                                      |')
    print('|                                      |                                      |')
    print('|                                      |                                      |')
    print('|                                      |                                      |')
    print('|                                      |                                      |')
    print('|                                      |                                      |')
    print('|                                      |                                      |')
    print('|                                      |                                      |')
    print('+--------------------------------------+--------------------------------------+')
else:
    print('ERROR: Invalid Entry')