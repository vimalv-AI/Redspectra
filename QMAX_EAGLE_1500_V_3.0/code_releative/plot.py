import sys
import numpy as np
import glob, os
import matplotlib.pyplot as plt
os.chdir(".")
for file in glob.glob("tight/*.txt"):
    print(file)
    #print(str(sys.argv))
    f = open(file, "r")
    y= np.arange(1,24001,1)
    CapData =f.readlines()
    print(len(CapData))
    CapData = [int(i) for i in CapData]
    #print(type(CapData))
    #print(CapData[1])
    m = np.zeros(len(CapData))
    n=0
    m[1]=0.0
    for n in range(1,len(CapData),1):
        #print(CapData[n],n,(CapData[n]-16383+1)/8192)
        if CapData[n]>8191:
            m[n]=(CapData[n]-16383+1)/8192
        else:
            m[n]=CapData[n]/8192
        #print(m[n])
    npa = np.asarray(y, dtype=np.float32)
    x =  np.arange(1, 24001,1);
    #print(type(y))
    #print(type(x))
    #y = np.sin (x);
    plt.figure(1)
    plt.subplot(211)
    plt.plot(x, m)
    plt.xlabel('sample(n)')
    plt.ylabel('voltage(V)')
    plt.subplot(212)
    plt.plot(x[1:1500],m[1:1500])
    plt.xlabel('sample(n)')
    plt.ylabel('voltage(V)')
    plt.savefig(file+'_2.png')
    plt.close()
    plt.show()

import glob
import shutil
for file in glob.glob('tight/*.png'):
    print(file)
    shutil.move(file, 'tight/plot/')



for file in glob.glob("lose/*.txt"):
    print(file)
    #print(str(sys.argv))
    f = open(file, "r")
    y= np.arange(1,24001,1)
    CapData =f.readlines()
    print(len(CapData))
    CapData = [int(i) for i in CapData]
    #print(type(CapData))
    #print(CapData[1])
    m = np.zeros(len(CapData))
    n=0
    m[1]=0.0
    for n in range(1,len(CapData),1):
        #print(CapData[n],n,(CapData[n]-16383+1)/8192)
        if CapData[n]>8191:
            m[n]=(CapData[n]-16383+1)/8192
        else:
            m[n]=CapData[n]/8192
        #print(m[n])
    npa = np.asarray(y, dtype=np.float32)
    x =  np.arange(1, 24001,1);
    #print(type(y))
    #print(type(x))
    #y = np.sin (x);
    plt.figure(1)
    plt.subplot(211)
    plt.plot(x, m)
    plt.xlabel('sample(n)')
    plt.ylabel('voltage(V)')
    plt.subplot(212)
    plt.plot(x[1:1500],m[1:1500])
    plt.xlabel('sample(n)')
    plt.ylabel('voltage(V)')
    plt.savefig(file+'_2.png')
    plt.close()
    plt.show()

import glob
import shutil
for file in glob.glob('lose/*.png'):
    print(file)
    shutil.move(file, 'lose/plot/')
