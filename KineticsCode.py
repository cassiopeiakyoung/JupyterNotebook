# kinetics lab report

import matplotlib.pyplot as plt          #IMPORT EVERYTHING
from matplotlib import rc                #JUST IN CASE
import numpy as np

# various data for burning of the candle, including data modelling the 0th, 1st and 2nd reactions
candleData=[
  [0,1.17],[15,1.159],[30,1.147],[45,1.13],[60,1.112],[75,1.096],[90,1.081],[105,1.066],[120,1.05],[135,1.025],[150,1.02],[165,1.005],[180,0.99],[195,0.973],[210,0.956],[225,0.936],[240,0.916],[255,0.895],[270,0.876],[285,0.852],[300,0.838],[315,0.822],[330,0.805],[345,0.796],[360,0.787],[375,0.759],[390,0.741],[405,0.723],[420,0.707],[435,0.688],[450,0.675],[465,0.657],[480,0.636],[495,0.611],[510,0.6],[525,0.58],[540,0.555],[555,0.536],[570,0.519],[585,0.497],[600,0.485],[615,0.466],[630,0.452],[645,0.43],[660,0.415],[675,0.396],[690,0.381],[705,0.363],[720,0.347],[735,0.332],[750,0.312],[765,0.293],[780,0.277],[795,0.262],[810,0.242],[825,0.223],[840,0.206],[855,0.179],[870,0.166],[885,0.149],[900,0.132],[915,0.108],[930,0.09],[945,0.08],[960,0.074],[975,0.054],[990,0.034],[1005,0.025],[1020,0.013],[1035,0.001]
]

lnCandleData=[
  [0,	0.157003749],[15,0.147557564],[30,0.137149838],[45,0.122217633],[60,0.106160196],[75,0.091667189],[90,0.077886539],[105,0.063913326],[120,0.048790164],[135,0.024692613],[150,0.019802627],[165,0.004987542],[180,-0.010050336],[195,-0.027371197],[210,-0.044997366],[225,-0.066139803],[240,-0.087738914],[255,-0.110931561],[270,-0.132389188],[285,-0.160168752],[300,-0.176737179],[315,-0.196014884],[330,-0.216913002],[345,-0.228156093],[360,-0.239527031],[375,-0.275753502],[390,-0.299754654],[405,-0.324346057],[420,-0.346724613],[435,-0.373966441],[450,-0.393042588],[465,-0.42007126],[480,-0.452556716],[495,-0.49265832],[510,-0.510825624],[525,-0.544727175],[540,-0.588787165],[555,-0.623621118],[570,-0.655851396],[585,-0.699165253],[600,-0.723606388],[615,-0.763569645],[630,-0.794073099],[645,-0.84397007],[660,-0.879476759],[675,-0.926341068],[690,-0.964955904],[705,-1.013352445],[720,-1.058430499],[735,-1.10262031],[750,-1.164752091],[765,-1.22758267],[780,-1.283737773],[795,-1.339410775],[810,-1.418817553],[825,-1.500583508],[840,-1.57987911],[855,-1.720369473],[870,-1.795767491],[885,-1.903808973],[900,-2.024953356],[915,-2.225624052],[930,-2.407945609],[945,-2.525728644],[960,-2.603690186],[975,-2.918771232],[990,-3.381394754],[1005,-3.688879454],[1020,-4.342805922],[1035,-6.907755279]
]
invCandleData=[
  [0,0.854700855],[15,0.86281277],[30,0.871839582],[45,0.884955752],[60,0.899280576],[75,0.912408759],[90,0.92506938],[105,0.938086304],[120,0.952380952],[135,0.975609756],[150,0.980392157],[165,0.995024876],[180,1.01010101],[195,1.027749229],[210,1.046025105],[225,1.068376068],[240,1.091703057],[255,1.117318436],[270,1.141552511],[285,1.17370892],[300,1.193317422],[315,1.216545012],[330,1.242236025],[345,1.256281407],[360,1.27064803],[375,1.317523057],[390,1.349527665],[405,1.383125864],[420,1.414427157],[435,1.453488372],[450,1.481481481],[465,1.522070015],[480,1.572327044],[495,1.636661211],[510,1.666666667],[525,1.724137931],[540,1.801801802],[555,1.865671642],[570,1.926782274],[585,2.012072435],[600,2.06185567],[615,2.145922747],[630,2.212389381],[645,2.325581395],[660,2.409638554],[675,2.525252525],[690,2.624671916],[705,2.754820937],[720,2.88184438],[735,3.012048193],[750,3.205128205],[765,3.412969283],[780,3.610108303],[795,3.816793893],[810,4.132231405],[825,4.484304933],[840,4.854368932],[855,5.586592179],[870,6.024096386],[885,6.711409396],[900,7.575757576],[915,9.259259259],[930,11.11111111],[945,12.5],[960,13.51351351],[975,18.51851852],[990,29.41176471],[1005,40],[1020,76.92307692],[1035,1000]
]


# jesus that's a lot of data
# for anyone wondering how i converted all my data to the array format used by python (no i did not do it manually)
# i used a program called Notepad++ to record a "macro", a series of keyboard inputs, and used this feature to put
# all my data in these neat arrays. doing it manually takes way too lang and i'm too lazy for that lmao
# i always have a way to get around work

# extract x- & y- values from data (candle, regular)
time=[]
for i in range(len(candleData)):
  time.append(candleData[i][0])
  
candleYValuesNormal=[]
for i in range(len(candleData)):
  candleYValuesNormal.append(candleData[i][1])
  
# beginning to graph first set of data
  
plt.scatter(time,candleYValuesNormal, marker="*")

plt.xlim(0,1050)                                   # set x-axis range
plt.ylim(0,1.2)                                   # set y-axis range

plt.xlabel("time", fontsize=16)                # label x-axis title & its font size
plt.ylabel("weight of cangle (g)", fontsize=16)                # label y-axis title

plt.tick_params(labelsize=16)                     # set axis number font size

plt.plot()
plt.title('0th order Rxn',fontsize=16)

plt.show()                                       # show plot
  
# extract x- & y- values from data (candle, ln)

# x_value=[]
# for i in range(len(lnCandleData)):
#   x_value.append(lnCandleData[i][0])

# this code is superfluous because the x-values (time) remain the same within a trial
  
lnCandleYValues=[]
for i in range(len(lnCandleData)):
  lnCandleYValues.append(lnCandleData[i][1])
  
# beginning to graph second set of data
  
plt.scatter(time,lnCandleYValues, marker="*")

plt.xlim(0,1050)                                   # set x-axis range
plt.ylim(-7,0.2)                                   # set y-axis range

plt.xlabel("time", fontsize=16)                # label x-axis title & its font size
plt.ylabel("ln(weight of cangle (g))", fontsize=16)                # label y-axis title

plt.tick_params(labelsize=16)                     # set axis number font size

plt.plot()
plt.title('1st order Rxn',fontsize=16)

plt.show()                                       # show plot

  
# extract x- & y- values from data (candle, inv)
  
invCandleYValues=[]
for i in range(len(invCandleData)):
  invCandleYValues.append(invCandleData[i][1])
  
# beginning to graph third set of data
  
plt.scatter(invCandleTime,invCandleYValues, marker="*")

plt.xlim(0,1050)                                   # set x-axis range
plt.ylim(0,1000)                                   # set y-axis range

plt.xlabel("time", fontsize=16)                # label x-axis title & its font size
plt.ylabel("1/(weight of cangle (g))", fontsize=16)                # label y-axis title

plt.tick_params(labelsize=16)                     # set axis number font size

plt.plot()
plt.title('2nd order Rxn',fontsize=16)

plt.show()                                       # show plot
