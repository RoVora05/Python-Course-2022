from random import *
import math

class monster():
    def __init__(self,name,attributes,abilityList,level,exp,damageInfo):
        self.name=name
        self.attributeList=attributes
        self.abilityList=[abilityList]
        self.skillCooldown=0
        self.level=level
        self.exp=exp # means exp yield
        self.damageRange=damageInfo[0]
        self.acc=damageInfo[1]
        self.attackType=damageInfo[2]

    def getAttributes(self): return self.attributeList
    def editAttribute(self,index,statIndex,amount): self.attributeList[index][statIndex]+=amount
    def takeDamage(self,damage): self.abilityList[1][0]-=damage
    def heal(self,heal): self.abilityList[1][0]+=heal
    def getName(self): return self.name
    def getLevelData(self): return [self.level, self.exp]
    def takeAction(self):
        if randint(1,round(len(self.abilityList)*1.5))>len(self.abilityList):
            return "regular attack"
        else:
            return self.abilityList[randint(0,len(self.abilityList)-1)]
    def regularAttack(self,target):
        if self.acc>randint(1,100)-self.attributeList[2][3]:
            if self.attackType=="physical": return randint(self.damageRange[0],self.damageRange[1])+self.attributeList[2][0]-target.getAttributes()[3]
            else: return randint(self.damageRange[0],self.damageRange[1])+self.attributeList[2][1]
            
        else:
            print("Miss")
            return 0


class character(monster):
    def __init__(self,name):
        self.name=name
        self.baseAttributeList=[[20,10],[20,10],[1,1,1,1,1],0]
        self.attributeList=self.baseAttributeList
        self.level=1
        self.exp=10 # means exp left to level up
        self.equipment={"weapon":weapon("Rusty Knife",[0,0,0,0,0],[1,2],80),"armor":armor("Broken Chainmail",[0,0,0,0,0],0),"accessory":accessory("Coin",["Lucky ",[0,0,0,0,1],[[0,0],0,0]])}
        self.abilityList=[]
        self.skillCooldown=0
        self.updateAttributeList()

    def getBaseAttributes(self): return self.baseAttributeList
    def editBaseAttribute(self,index,statIndex,amount): self.baseAttributeList[index][statIndex]+=amount
    def updateAttributeList(self):
        self.attributeList=self.baseAttributeList
        for i in range(5): self.attributeList[2][i]+=self.equipment["weapon"].getModifierList()[i]
        for i in range(5): self.attributeList[2][i]+=self.equipment["armor"].getModifierList()[i]
        self.attributeList[3]+=self.equipment["armor"].armor()
        for i in range(5): self.attributeList[2][i]+=self.equipment["accessory"].getModifierList()[i]

    def levelUp(self):
        self.level+=1
        self.exp+=10*(self.level**2)
        for i in range(2): self.editAttribute(2,int(input()),1)
        self.editAttribute(2,randint(1,5),1)
        self.baseAttributeList[0][0]+=round(1.25**self.level)+self.baseAttributeList[2][2]
        self.baseAttributeList[1][0]+=round(1.125**self.level)
        if self.level in [2,5,9,14,20]:
            if input()=="Yes":
                self.newAbility()
            else:
                for i in range(2): self.editAttribute(2,int(input()),round(self.level/3))
    
    def newAbility(self,ability):
        self.abilityList.append(ability)
    
    def giveExp(self,exp):
        self.exp-=exp
        if self.exp<=0: self.levelUp()
    def equip(self,newItem):
        if type(newItem)==weapon:
            temp=self.equipment["weapon"]
            self.equipment["weapon"]=newItem
            inventory.giveItem(temp)
        elif type(newItem)==armor:
            temp=self.equipment["armor"]
            self.equipment["armor"]=newItem
            inventory.giveItem(temp)
        elif type(newItem)==accessory:
            temp=self.equipment["accessory"]
            self.equipment["accessory"]=newItem
            inventory.giveItem(temp)
        else:
            print("Not an equipable item")        

class inventory():
    def __init__(self):
        self.invList=[None for i in range(8)]
    
    def giveItem(self,item):
        noSpace=True
        for i,e in enumerate(self.invList):
            if e==None:
                self.invList[i]=item
                noSpace=False
                break
        if noSpace: print("No Space")

    def useHealItem(self,itemIndex,target):
        target.heal(self.invList[itemIndex].getHeal())

class healItem():
    def __init__(self,heal,value):
        self.heal=heal
        self.value=value
    def getHeal(self): self.heal
    def getValue(self): self.value

class equipment():
    def __init__(self):
        self.modiferList=0
        self.enchantment=0
        self.name=0
        self.enchanted=True
    def getName(self): return self.name
    def getModifierList(self): return self.modiferList
    def checkEnchanted(self): return self.enchanted

class weapon(equipment):
    def __init__(self,name,modiferList,dR,acc): # enchantment=["name",[modifierList],[[damageRange],accuracy,armor]]
        self.name=name
        self.damageRange=dR
        self.accuracy=acc
        self.modiferList=modiferList
        self.enchanted=False
    def dR(self): return self.damageRange
    def acc(self): return self.accuracy
    def enchant(self,enchantment):
        self.name=enchantment[0]+self.name
        for i in range(5): self.modiferList[i]+=enchantment[1][i]
        self.damageRange+=enchantment[2][0]
        self.accuracy+=[2][1]
        self.enchanted=True

class armor(equipment):
    def __init__(self,name,modifierList,defense):
        self.name=name
        self.modiferList=modifierList
        self.defense=defense
        self.enchanted=False
    def armor(self): return self.defense
    def enchant(self,enchantment):
        self.name=enchantment[0]+self.name
        for i in range(5): self.modiferList[i]+=enchantment[1][i]
        self.defense+=enchantment[2][2]
        self.enchanted=True

class accessory(equipment):
    def __init__(self,name,enchantment):
        self.name=enchantment[0]+name
        self.modiferList=[0,0,0,0,0]
        for i in range(5): self.modiferList[i]=round(math.floor(1.5*enchantment[1][i]))
        self.enchanted=True

def combat(alliesList,enemiesList):
    if determineFirst(alliesList,enemiesList): turnOrder=["player",alliesList,enemiesList]
    else: turnOrder=[enemiesList,"player",alliesList]
    enemyCount=len(enemiesList)
    while player.getAttributes()[1][0]>0 or enemyCount>0:
        for e in turnOrder:
            if e=="player":
                "player action"
            else:
                for e2 in e:
                    e2.takeAction()
    
def determineFirst(alliesList,enemiesList):
    alliesAverage=player.getAttributes()[2][3]
    for e in alliesList:alliesAverage+=e.getAttributes()[2][3]
    alliesAverage/=1+len(alliesList)
    enemiesAverage=0
    for e in enemiesList:enemiesAverage+=e.getAttributes()[2][3]
    enemiesAverage/=len(enemiesList)
    if alliesAverage>=enemiesAverage: return True
    else: return False

def generateRandomEnemies(enemyRangeStart,enemyRangeEnd):
    enemyList=[]
    for i in range(randint(1,4)): enemyList.append(allEnemiesList[randint(enemyRangeStart,enemyRangeEnd)])
    return enemyList

allEnemiesList=[]
player=character(input("What is this character's name?\n"))