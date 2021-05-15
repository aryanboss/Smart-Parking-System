import os
import RPi.GPIO as GPIO
import time
import module
import datetime
import linecache
import qrcode
import generate
import cc

GPIO.setwarnings(False)
  
class vehicle:
    def __init__(self,spot,type,time):
        self.spot = spot
        self.type = type
        self.time = time


def status():
    print("                          Searching for Spots...")
    print("\n")
    for i in range(1,5):
        x = module.distance(i)
        if x >= 4:
            print("Spot ",i,"is Empty")
        else:
            continue

def showstatus():
    for i in range(1,5):
        x = module.distance(i)
        if x >= 5:
            print("Spot ",i,"is Empty")
        else:
            continue

def mainmenu(count):
            y = str(count)+".jpg"
            spot = int(input("\nChoose Your Spot: "))
            cc.reserve(spot)
            type = input("Choose Your Vehicle Type Car/Bike: ")
            e = datetime.datetime.now()
            date = e.strftime("%d/%m/%Y")
            tym = e.strftime("%I:%M:%S %p")
            z = vehicle(spot,type,e)
            x = "Ticket No: " + str(count) + "\nSpot No: " + str(z.spot) + "\nVehical Type: " + str(z.type) + "\nArrival Time: " + tym + "\nDate: " + date + "\n"
            img = qrcode.make(x)
            img.save(y)
            fhand = open('data.txt','a')
            fhand.write(x)
            fhand.write("\n")
            fhand.close()
            print("\nPlease Wait! Your Ticket is being Generated!")
            generate.make(type,spot,tym,date,count)
            os.remove(y)

def arrival(count):
    status()
    mainmenu(count)
    print("Ticket generated successfully!\n")
    print("Opening Gate, Please Collect Your Ticket and Enter")
    module.servo(0)
    module.servo(90)
    time.sleep(4)
    print("Closing Gate")
    module.servo(0)
    
    

def departure(tn):
    file = open("data.txt")
    for line in file:
        line = line.rstrip()
        if line.startswith('Arrival '):
            fhand = open("a.txt",'a')
            fhand.write(line)
            fhand.write("\n")
            fhand.close()
        else:
            continue
    ml = linecache.getline('a.txt',tn)
    file = open("a.txt","r+")
    file.truncate(0)
    file.close()
    ahr = int(ml[14:16])
    amin = int(ml[17:19])
    asec = int(ml[20:22])
    #print(ahr,amin,asec)

    t = datetime.datetime.now()
    dtym = t.strftime("%I:%M:%S %p")
    dtym = "Departure Time: " + dtym
    print(dtym)
    dhr = int(dtym[16:18])
    dmin = int(dtym[19:21])
    dsec = int(dtym[22:24])
    #print(dhr,dmin,dsec)

    hr = dhr-ahr
    if amin > dmin:
        min = amin - dmin
        totaltime = hr*60 - min
    else:
        min = dmin - amin
        totaltime = hr*60 + min

    fare = totaltime*0.2
    print("Your Vehicle Was Parked for: ",totaltime," Minutes")
    print("\nYour Bill amount is: ",round(fare,2), "Rs")
    print("\n            ===========>Thank You!<===========")
    print("\n")


while(True):
        print("1.Arrival\n2.Status Check\n3.Departure\n")
        x = int(input("Choose Option: "))
        print("\n")
        if x == 1:
            fhand = open("data.txt")
            for line in fhand:
                line = line.rstrip()
                if line.startswith('Ticket '):
                    fhand1 = open("a.txt",'a')
                    fhand1.write(line)
                    fhand1.write("\n")
                    fhand1.close()
                else:
                    continue
            fhand2 = open("a.txt")
            count = 0
            for i in fhand2:
                count = count + 1
            arrival(count+1)
            file = open("a.txt","r+")
            file.truncate(0)
            file.close()
            
        if x == 2:
            showstatus()
            
        if x == 3:
            tn = int(input("Enter Your Ticket Number: "))
            sn = int(input("Enter Your Spot Number: "))
            cc.empty(sn)
            departure(tn)