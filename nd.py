#!/usr/bin/env python3
import sys
import curses
import random
nds=open('nds','r').read().split('\n')
s=curses.initscr()
k=-1
if len(sys.argv)>1:
    k=int(sys.argv[1])
while 1:
    p=s.getch()
    if p=='n':break
    if k==-1:
        l=nds[random.randint(0,len(nds))]
    else:
        if random.randint(0,2):
            l=nds[k]
        else: l=nds[random.randint(0,len(nds)-1)]
curses.endwin()
