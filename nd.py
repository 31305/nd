#!/usr/bin/env python3
import sys
import curses
import random
from os import system
nds=open('nds','r').read().split('\n')
for k in range(0,len(nds)):
    if nds[k]=='':
        nds=nds[:-1]
        break
s=curses.initscr()
curses.noecho()
k=-1
if len(sys.argv)>1:
    k=int(sys.argv[1])
while 1:
    p=s.getch()
    if p==110:break
    if k==-1:
        l=nds[random.randint(0,len(nds)-1)]
    else:
        if random.randint(0,1):
            l=nds[k]
        else: l=nds[random.randint(0,len(nds)-2)]
    system('echo '+l.replace(',',' ')+' |../sv/sv 13')
curses.echo()
curses.endwin()
print(nds)
