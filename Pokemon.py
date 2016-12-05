#-*-coding:utf8;-*-
#qpy:3
#qpy:console

print("This is console module")
import random
import sys
import time

water_gun=5
scratch=3
ember=6
vine_whip=4
tackle=5
bite=4
razor_leaf=6
bubble_beam=5
fire_fang=6
pursuit=5
poison_sting=5
acid=5
pound=5

starterturn=False
enemyturn=False
randechoice=random.randrange(1,4)
ts=time.sleep
ty=time.sleep(1)
tu=time.sleep(1.5)
ti=time.sleep(2)

print("Hello, I am Professor Sanju.")
ts(1)
print("I welcome you in this world where we live with interesting creatures known as Pokemon.")
ts(2)
print("We all love Pokemon.")
ts(1.5)
print("As you are a beginner I will give you 3 starter Pokemon out of which you can choose one.")
ts(2)
print("Each Pokemon is unique and has its own special attack.")

sname=input("'Please tell me what is your name:'\n")
ename=input("'Please tell me what is your rivals name:'\n")

print("×"*41)
print(str(sname)+", please choose any one of the Pokemon.")

ts(1)
print("1-BULBASAUR.\n2-SQUIRTLE.\n3-CHARMANDER.")
ts(1.5)
print("Please choose your Pokemon carefully as you won't be able to change it later.")

choice=input("Choose your Pokemon:\n")

print("×"*41)
if(int(choice)==1):
    shp=50
    satk=40
    sdef=50
    sspd=45
    startername="BULBASAUR"
    move1=tackle
    move1name="Tackle"
    move2=vine_whip
    move2name="Vine Whip"
    move3=razor_leaf
    move3name="Razor Leaf"
elif(int(choice)==2):
    shp=40
    satk=40
    sdef=60
    sspd=40
    startername="SQUIRTLE"
    move1=bite
    move1name="Bite"
    move2=water_gun
    move2name="Water Gun"
    move3=bubble_beam
    move3name="Bubble Beam"
elif(int(choice)==3):
    shp=50
    satk=70
    sdef=35
    sspd=50
    startername="CHARMANDER"
    move1=scratch
    move1name="Scratch"
    move2=ember
    move2name="Ember"
    move3=fire_fang
    move3name="Fire Fang"
else:
    print("Please input proper values.")

print("You choosed level 10 "+startername+"!")

if(randechoice==1):
    ehp=40
    eatk=40
    edef=30
    espd=30
    enemyname="JIGGLYPUFF"
    emove1=pound
    emove1name="Pound"
    emove2=tackle
    emove2name="Tackle"
    emove3=scratch
    emove3name="Scratch"
elif(randechoice==2):
    ehp=30
    eatk=70
    edef=30
    espd=60
    enemyname="RATTATA"
    emove1=bite
    emove1name="Bite"
    emove2=tackle
    emove2name="Tackle"
    emove3=pursuit
    emove3name="Pursuit"
else:
    ehp=50
    eatk=60
    edef=30
    espd=40
    enemyname="EKANS"
    emove1=bite
    emove1name="Bite"
    emove2=poison_sting
    emove2name="Poison Sting"
    emove3=acid
    emove3name="Acid"
    
print("×"*41)
ts(1)

print("Oh, your rival "+str(ename)+" wants to have a battle with you.\nHe challenged you for a battle.")

ts(1)
print("="*41)
print("A BATTLE BEGAN") 
print("="*41)
ts(1)

print("You choosed level 10 "+startername+"!")
ts(1.5)
print("Your rival choosed level 10 " +enemyname+"!")
print("-"*41)
ts(1)

if(espd>sspd):
    enemyturn=True
else:
    starterturn=True

while(ehp>0 and shp>0):
    while(enemyturn==True):
        randmove=random.randrange(1,4)
        if(randmove==1):
            damage=(emove1*eatk)//sdef
            ts(1)
            print(enemyname+" used "+emove1name+" and dealt "+str(damage)+" damage")
            shp=shp-damage
            enemyturn=False
            starterturn=True
            if(shp<=0):
                ts(1)
                print(startername+" fainted!")
                ts(1.5)
                print(str(sname)+" is black out")
                sys.exit()
            else:
                ty
                print(startername+" has "+str(ehp)+"  hp left")
            print("="*41)
            break
        elif(randmove==2):
            damage=(emove2*eatk)//sdef
            ty
            print(enemyname+" used "+emove2name+" and dealt "+str(damage)+"  damage")
            shp=shp-damage
            enemyturn=False
            starterturn=True
            if(shp<=0):
                ty
                print(startername+", fainted!")
                print(str(sname)+", is black out!")
                sys.exit()
            else:
                tu
                print(startername+" has "+str(ehp)+"  hp left")
            print("="*41)
            break
        else:
            damage=(emove3*eatk)//sdef
            ty
            print(enemyname+" used "+emove3name+" and dealt "+str(damage)+" damage")
            shp=shp-damage
            enemyturn=False
            starterturn=True
            if(shp<=0):
                ty
                print(startername+" fainted!")
                print(str(sname) +", is black out!")
                sys.exit()
            else:
                tu
                print(startername+" has "+str(shp)+" hp left")
            print("="*41)
            break
        break
    while(starterturn==True):
        ty
        print("What will "+startername+" do?")
        print("1-"+move1name)
        print("2-"+move2name)
        print("3-"+move3name)
        wmove=input("Enter:\n")
        print("-"*41)
        ty
        if(wmove==1):
            damage=(move1*satk)//edef
            ty
            print(startername+" used "+move1name+" and dealt "+str(damage)+" damage")
            ehp=ehp-damage
            starterturn=False
            enemyturn=True
            if(ehp<=0):
                ty
                print(enemyname+" has fainted!")
                print("Congratulations, "+str(sname)+" you have defeated "+str(ename)+" and you are a winner!")
                sys.exit()
            else:
                tu
                print(enemyname+" has "+str(ehp)+" hp left")
            print("="*41)
            break
        elif(wmove==2):
            damage=(move2*satk)//edef
            ty
            print("{0} used {1} and dealt {2} damage" .format(startername,move2name,damage))
            ehp=ehp-damage
            starterturn=False
            enemyturn=True
            if(ehp<=0):
                ty
                print(enemyname+" has fainted!")
                print("Congratulations, {0} you have defeated {1} and you are the winner" .format(snake,ename))
                sys.exit()
            else:
                tu
                print(enemyname+" has "+str(ehp)+" hp left")
            print("="*41)
            break
        else:
            damage=(move3*satk)//edef
            ty
            print("{0} used {1} and dealt {2} damage" .format(startername,move3name,damage))
            ehp=ehp-damage
            starterturn=False
            enemyturn=True
            if(ehp<=0):
                ty
                print(enemyname+" has fainted!")
                print("Congratulations, {0} you have defeated {1} and you are the winner!" .format(sname,ename))
                sys.exit()
            else:
                tu
                print(enemyname+" has "+str(ehp)+"  hp left")
            print("="*41)
            break
        break