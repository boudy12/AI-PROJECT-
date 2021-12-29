import random
from prettytable import PrettyTable
import numpy as np
c1 =["Amr","Ai",135]
c2 =["Saied","Cs",145]
c3=["Shamrdan","IT",65]
c4=["Manal","Project",90]
c5 =["Pierre","Meme",60]
c6 =["body","oop",145]
c7=["mod","LOL",133]
c8=["hussin","Mangment",69]
c9=["atef","DS",96]
c10=["ashraf","Logic",110]
couresList=[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
hall1=["h1",100]
hall2=["h2",125]
hall3=["h3",140]
hall4=["h4",160]
hall5=["h5",155]
hallList=[hall1,hall2,hall3,hall4,hall5]
# class gen:
# class conflict:
#     def __init__(self,population):
#         self.pop = population
#         self.newpop = []
#
#         for i in self.pop:
#             self.table = i
#             for j in i:
#                 self.day = j
#                 self.con = 0
#                 if len(self.day) > 1:
#                     ln = len(j)
#                     for l in range(1,ln-1):
#                         cor = j[l][0][1]
#                         hl  = j[l][0][2]
#                         nos = cor[2]
#                         cap = hl[1]
#                         if cap >= nos:
#                         else:
#                             self.con = self.con +1
#
#
#







class pop:
    def __init__(self,i):
        self.ittartion = i
        self.bigList = []
        self.conlist = 0


        for j in range(0,i):
            self.smallList = []
            self.table = table()
            self.conprop  = self.table.daycon() + self.table.daycon()
            self.smallList.append(self.table.daycon())
            self.smallList.append(self.table.dayCompine())
            self.bigList.append(self.smallList  )

        self.conlist = self.conprop/10
    def getPOP(self):
        return self.bigList
    def getPOPcon(self):
        return self.conlist

class table:
    def __init__(self):
        self.randomDayList = []
        self.dayValues = [['sun'], ['mon'], ['tue'], ['wed'], ['ths']]
        self.com = timeCompine()

    def dayCompine(self):


            timeList = self.com.getRandomTimeCourseList()




            randomDayInd = []
            for i in self.dayValues:
                randomDayInd.append(i)

            for i in timeList:
                randomDayInd[random.randint(0, 4)].append(i)

            return randomDayInd
    def daycon(self):
        return self.com.getRandomTimeCourseCon()
class day:
    def __init__(self):
        self.coursecompine = []
        self.daycon = 0
        for i in couresList:
            randomcourse = course(i,hallList).getCourseData()
            if len(randomcourse) > 2:
                self.daycon = self.daycon + 1

            self.coursecompine.append(randomcourse)



    def getDay(self):
        return self.coursecompine

    def getDayCon(self):
        return  self.daycon

class time:
    def __init__(self,timeValue,courseData):
        self.timeValue = []
        self.timeValue.append(timeValue)
        self.courseData = courseData

        self.randomTimeCourse = [self.timeValue+self.courseData]


    def getTimeData(self):
         return self.randomTimeCourse
class course:
   def __init__(self,course,hallList):
       self.coursedata = [course,hallList[random.randint(0,len(hallList)-1)]]
       if self.coursedata[0][2] >= self.coursedata[1][1]:
           self.coursedata.append(1)


   def getCourseData(self):
        return self.coursedata
class timeCompine:
    def __init__(self):
        timeValues = [8, 10, 12, 14, 16]
        self.list = day()
        self.randomTimeCourseList = []
        for i in self.list.getDay():
            courseTimeCompine = time(timeValues[random.randint(0, len(timeValues)-1)], i)
            self.randomTimeCourseList.append(courseTimeCompine.getTimeData())

    def getRandomTimeCourseList(self):
        return self.randomTimeCourseList

    def getRandomTimeCourseCon(self):
        return self.list.getDayCon()






class evolve:
    def __init__(self,sortedPop):
        self.sortedpop = sortedPop
        self.list = random.sample(range(len(sortedPop)-1),4)
        self.a = self.list[0]
        self.b = self.list[1]
        self.c = self.list[2]
        self.target = self.list[3]


    def defrintil(self):


           if len(self.sortedpop[self.a][1]) > 1:
               dayslist = self.sortedpop[self.a][1][random.randint(0, len(self.sortedpop[self.a][1]) - 1)]
               if len(dayslist) > 1:
                   temp1 = dayslist[random.randint(1, len(dayslist) - 1)]
                   self.sortedpop[self.a][1][random.randint(0, len(self.sortedpop[self.a][1]) - 1)] = \
                   self.sortedpop[self.b][1][random.randint(0, len(self.sortedpop[self.a][1]) - 1)]
                   self.sortedpop[self.b][1][random.randint(0, len(self.sortedpop[self.a][1]) - 1)] = temp1
               else:
                   temp1 = None

           if len(self.sortedpop[self.a][1]) > 1:
               dayslist = self.sortedpop[self.a][1][random.randint(0, len(self.sortedpop[self.a][1]) - 1)]
               if len(dayslist) > 1:
                   temp2 = dayslist[random.randint(1, len(dayslist) - 1)]
                   self.sortedpop[self.b][1][random.randint(0, len(self.sortedpop[self.b][1]) - 1)] = \
                       self.sortedpop[self.c][1][random.randint(0, len(self.sortedpop[self.b][1]) - 1)]
                   self.sortedpop[self.c][1][random.randint(0, len(self.sortedpop[self.b][1]) - 1)] = temp2
               else:
                   temp1 = None









           return self.sortedpop














print('this is your random  population')

x = pop(5)
p = x.getPOP()
z = sorted(p, key=lambda x: x[0],reverse=True)

for i in z:

    for j in i:
        print(j)



print('your generation fittness is ')
print(x.getPOPcon())


print('######################################################')
print('this is your new population')
print('######################################################')

o = evolve(z)


for n in o.defrintil():

    print(n)






