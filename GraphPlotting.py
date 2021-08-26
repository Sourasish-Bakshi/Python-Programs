import matplotlib.pyplot as plot
import numpy as np
import pandas as pd
list = ["Roll","MCS401","M401","CS401","CS402","CS403","HU481","MCS491","CS491","CS492","CS493","SGPA3","SGPA4","YGPA","DGPA","RESULT"]
r2013 = pd.read_csv("2013.csv", names=list)
r2014 = pd.read_csv("2014.csv", names=list)
r2015 = pd.read_csv("2015.csv", names=list)
O=E=A=B=C=F=0
list1 = r2013.MCS401.to_list()
mcs401_2013 = np.array(list1)
for i in mcs401_2013:
    t=i
    if t.startswith('O'):
        O+=1
    elif t.startswith('E'):
        E+=1
    elif t.startswith('A'):
        A+=1
    elif t.startswith('B'):
        B+=1
    elif t.startswith('C'):
        C+=1
    elif t.startswith('F'):
        F+=1
d2013 = {"Grade O":O, "Grade E":E, "Grade A":A, "Grade B":B, "Grade C":C, "Grade F":F}
keys= d2013.keys()
values= d2013.values()
plot.bar(keys,values)
plot.ylabel('<--Num of Students-->')
plot.xlabel('<--Grade of the Students-->')
plot.title('Bar Chart showing the Grade distribution of MCS401 2013')
plot.show() 


O=E=A=B=C=F=0
list2 = r2014.MCS401.to_list()
mcs401_2014 = np.array(list2)
for i in mcs401_2014:
    t=i
    if t.startswith('O'):
        O+=1
    elif t.startswith('E'):
        E+=1
    elif t.startswith('A'):
        A+=1
    elif t.startswith('B'):
        B+=1
    elif t.startswith('C'):
        C+=1
    elif t.startswith('F'):
        F+=1
d2014 = {"Grade O":O, "Grade E":E, "Grade A":A, "Grade B":B, "Grade C":C, "Grade F":F}
keys= d2014.keys()
values= d2014.values()
plot.bar(keys,values)
plot.ylabel('<--Num of Students-->')
plot.xlabel('<--Grade of the Students-->')
plot.title('Bar Chart showing the Grade distribution of MCS401 2014')
plot.show()


O=E=A=B=C=F=0
list3 = r2015.MCS401.to_list()
mcs401_2015 = np.array(list3)
for i in mcs401_2015:
    t=i
    if t.startswith('O'):
        O+=1
    elif t.startswith('E'):
        E+=1
    elif t.startswith('A'):
        A+=1
    elif t.startswith('B'):
        B+=1
    elif t.startswith('C'):
        C+=1
    elif t.startswith('F'):
        F+=1
d2015 = {"Grade O":O, "Grade E":E, "Grade A":A, "Grade B":B, "Grade C":C, "Grade F":F}
keys= d2015.keys()
values= d2015.values()
plot.bar(keys,values)
plot.ylabel('<--Num of Students-->')
plot.xlabel('<--Grade of the Students-->')
plot.title('Bar Chart showing the Grade distribution of MCS401 2015')
plot.show()
