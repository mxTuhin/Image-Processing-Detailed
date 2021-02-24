from time import ctime
while True:
    print(ctime())

    disTime = ctime().split(" ")
    discreteTime = disTime[3]
    alChecker = discreteTime.split(":")
    alarmChecker = (alChecker[1])

    if(alarmChecker=='31'):
        print('ayayya')
        break