def main():
    print("Welcome to the D&D 5e Inventory Weigher.")
    print("This only includes items in the basic rules.")
    print("However, you can type 'custom' to create a custom item")
    weight=0
    price=0
    done=False
    while done==False:
        print("")
        item=input("Enter an item to add to your inventory. ")
        if item=="custom":
            custom_weight=eval(input("Enter the item's weight. "))
            custom_price=eval(input("Enter the item's price in copper pieces. "))
            weight+=custom_weight
            price+=custom_price
        elif item=="padded":
            weight+=8
            price+=500
        elif item=="leather":
            weight+=10
            price+=1000
        elif item=="studded leather":
            weight+=13
            price+=4500
        elif item=="hide":
            weight+=12
            price+=1000
        elif item=="chain shirt":
            weight+=20
            price+=5000
        elif item=="scale mail":
            weight+=45
            price+=5000
        elif item=="breastplate":
            weight+=20
            price+=40000
        elif item=="half plate":
            weight+=40
            price+=75000
        elif item=="ring mail":
            weight+=40
            price+=3000
        elif item=="chain mail":
            weight+=55
            price+=7500
        elif item=="splint":
            weight+=60
            price+=20000
        elif item=="plate":
            weight+=65
            price+=150000
        elif item=="shield":
            weight+=6
            price+=1000
        elif item=="club":
            weight+=2
            price+=10
        elif item=="dagger":
            weight+=1
            price+=200
        elif item=="greatclub":
            weight+=10
            price+=20
        elif item=="handaxe":
            weight+=10
            price+=500
        elif item=="javelin":
            weight+=2
            price+=50
        elif item=="light hammer":
            weight+=2
            price+=200
        elif item=="mace":
            weight+=4
            price+=500
        elif item=="quarterstaff":
            weight+=4
            price+=20
        elif item=="sickle":
            weight+=2
            price+=100
        elif item=="spear":
            weight+=3
            price+=100
        elif item=="light crossbow":
            weight+=5
            price+=2500
        elif item=="dart":
            weight+=1/4
            price+=5
        elif item=="shortbow":
            weight+=2
            price+=25
        elif item=="sling":
            weight+=0
            price+=10
        elif item=="battleaxe":
            weight+=4
            price+=1000
        elif item=="flail":
            weight+=2
            price+=1000
        elif item=="glaive":
            weight+=6
            price+=20
        elif item=="greataxe":
            weight+=7
            price+=3000
        elif item=="greatsword":
            weight+=6
            price+=5000
        elif item=="halberd":
            weight+=6
            price+=20
        elif item=="lance":
            weight+=6
            price+=10
        elif item=="longsword":
            weight+=3
            price+=15
        elif item=="maul":
            weight+=10
            price+=1000
        elif item=="morningstar":
            weight+=4
            price+=1500
        elif item=="pike":
            weight+=18
            price+=500
        elif item=="rapier":
            weight+=2
            price+=2500
        elif item=="scimitar":
            weight+=3
            price+=2500
        elif item=="shortsword":
            weight+=2
            price+=1000
        elif item=="trident":
            weight+=4
            price+=500
        elif item=="warhammer":
            weight+=2
            price+=1500
        elif item=="whip":
            weight+=3
            price+=200
        elif item=="blowgun":
            weight+=1
            price+=1000
            print("Why do you even need this?")
        elif item=="hand crossbow":
            weight+=3
            price+=7500
            print("Ah, a metagamer.")
        elif item=="heavy crossbow":
            weight+=18
            price+=5000
        elif item=="longbow":
            weight+=2
            price+=5000
        elif item=="net":
            weight+=3
            price+=100
            print("Remember: You always have disadvantage using this without Crossbow Expert or Sharpshooter!")
        elif item=="arrows" or "arrow":
            weight+=1
            price+=100
        elif item=="needles" or "blowgun needles" or "needle" or "blowgun needle":
            weight+=1
            price+=100
        elif item=="bolts" or "crossbow bolts" or "bolt" or "crossbow bolt":
            weight+=3/2
            price+=100
        elif item=="sling bullets" or "sling bullet" or "bullets" or "bullet":
            weight+=3/2
            price+=4
        elif item=="crystal":
            weight+=1
            price+=1000
        elif item=="orb":
            weight+=3
            price+=2000
        elif item=="rod":
            weight+=2
            price+=1000
        elif item=="staff":
            weight+=4
            price+=5000
            print("This is the arcane focus.")
            print("If you're looking for the druidic focus, try 'wooden staff'.")
        elif item=="wand":
            weight+=1
            price+=1000
            print("This is the arcane focus.")
            print("If you're looking for the druidic focus, try 'yew wand'.")
        elif item=="sprig of mistletoe" or "mistletoe":
            weight+=0
            price+=100
        elif item=="totem":
            weight+=0
            price+=100
        elif item=="wooden staff":
            weight+=4
            price+=500
        elif item=="yew wand":
            weight+=1
            price+=1000
        elif item=="amulet":
            weight+=5
            price+=500
        elif item=="emblem":
            weight+=0
            price+=500
        elif item=="reliquary":
            weight+=2
            price+=500
        elif item=="abacus":
            weight+=2
            price+=200
        elif item=="vial of acid" or "acid vial" or "acid":
            weight+=1
            price+=2500
        elif item=="alchemist's fire" or "alchemists fire":
            weight+=1
            price+=5000