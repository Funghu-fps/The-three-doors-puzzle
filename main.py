from random import randint
import time
#The three doors puzzle experiment (poorly done)
run = True
#about doors
doorlist=[]
lastdoors=[]
lastdoor= None
#cool stuff
count = 0
repeat = None
repcount = 0
def main():
    #choosing doors
    chosendoor = randint(0,doornum-1)
    for i in range(doornum):
        doorlist.append(False)
    #prize door is what we want to get
    prize = randint(0,doornum-1)
    doorlist[prize]= True
    #if your door is empty the show runner will only left the one with prize
    if prize != chosendoor:
        lastdoors=[chosendoor,prize]
        for skr in range(doornum):
            if skr != prize and skr != chosendoor:
                doorlist[skr] = "closed"
    if prize == chosendoor:
        emptdoor= False
        while emptdoor == False or emptdoor == prize:
            emptdoor = randint(0,doornum-1)
        lastdoors = [chosendoor,emptdoor]

        for skr in range(doornum):
            if skr != prize and skr != emptdoor:
                doorlist[skr] = "closed"

    lastdoor = lastdoors[1]
    #print(lastdoors)
    #print(lastdoor)
    if lastdoor == prize:
        return True





## main loop
while run:
    repeat = int(input("repeat"))
    doornum = int(input("door number (bigger that 2)"))
    time1 = time.time()
    while repcount <= repeat:
        doorlist = []
        lastdoor = None
        if main() == True:
            count +=1
        repcount += 1
    time2=time.time()-time1
    print("it took {} seconds".format(time2))
    print ("%"+str((count/repeat)*100))
    repcount = 0
    count = 0
