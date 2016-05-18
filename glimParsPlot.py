#! /usr/bin/env python
"""
Contains the function
"""
import sys
import getopt
from Tkinter import *

#Function for plotting glimmer output parsed with parse()
def plot(data,cutoff=1000):
    root = Tk()
    root.title(data[0][1]+", showing all predicted genes with more than " + repr(cutoff) + " bases") #Header of fasta
    length=len(data[0][2]) #length of whole sequence
    crd=getCoords([1,length])
    genes=data[1]
    try:
        canvas = Canvas(root, width=1000, height=600, bg = 'white')
        canvas.pack()
        Button(root, text='Back', command=root.quit).pack()
        for i in crd:
            canvas.create_line(i[0],i[1],i[2],i[3], width=8)
        for g in genes:
            start=g[1]
            stop=g[2]
            reverse=0
            if stop < start:
                reverse=start
                start=stop
                stop=reverse
            if (stop-start)>cutoff:
                crd=getCoords([start,stop])
                for i in crd:
                    if reverse:
                        canvas.create_line(i[0],i[1]+15,i[2],i[3]+15, width=4,fill='Blue')
                    else:
                        canvas.create_line(i[0],i[1]-15,i[2],i[3]-15, width=4,fill='Green')

     
    except:
        print "Error printing plot"
    root.mainloop()


#Function for getting coordinates for plotting in plot()
def getCoords(startstop):
    start=startstop[0]
    stop=startstop[1]
    startBin=start/1000000
    stopBin=stop/1000000
    coords=[]
    if startBin == stopBin:
        y=100+startBin*100
        x1=start-startBin*1000000
        x1=x1/1000.0
        x2=stop-startBin*1000000
        x2=x2/1000.0
        coords.append([x1,y,x2,y])
        return coords

    else:
        x1=start-startBin*1000000
        x1=x1/1000.0
        while startBin<stopBin:
            y=100+startBin*100
            coords.append([x1,y,1000,y])
            x1=1
            startBin+=1
    y=100+startBin*100
    x2=stop-startBin*1000000
    x2=x2/1000.0
    coords.append([x1,y,x2,y])
    return coords


#function for parsing glimmer output and combining it with a fasta file
def parse(fasta,glimmer):

    SEQUENCE_FILE = open(fasta).read()
    header,sequence=SEQUENCE_FILE.split('\n',1)
    sequence=sequence.strip()
    sequence=sequence.replace('\n','')
    seqData=[fasta,header,sequence]
    
    GLIMMER_FILE = open(glimmer,"r")
    header = GLIMMER_FILE.readline()
    genes=[]
    for line in GLIMMER_FILE:
        line=line.strip()
        items=line.split()
        genes.append([items[0],int(items[1]),int(items[2]),int(items[3].strip("+"))])
    return [seqData,genes]

