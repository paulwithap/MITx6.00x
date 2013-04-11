import pylab

inFile = open('julyTemps.txt')

high = []
low = []

for line in inFile:
    fields = line.split(' ')
    if len(fields) < 3 or not fields[0].isdigit():
        pass
    else:
        high.append(int(fields[1]))
        low.append(int(fields[2].rstrip()))

def producePlot(lowTemps, highTemps):
    diffTemps = map(lambda x,y: x-y, highTemps, lowTemps)
    print diffTemps
    pylab.figure(1)
    pylab.plot(range(1, 32), diffTemps)
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.show()

producePlot(low, high)
