Mushroom_Sniffer = genMonster("Mushroom Sniffer", 60, 6000)
Mushroom_Sniffer.health(250)
Mushroom_Sniffer.type("blood")
Mushroom_Sniffer.defense(armor=15, fire=0.1, earth=0.1, energy=0.1, ice=0.1, holy=0.1, death=0.1, physical=0.1, drown=0.1)
Mushroom_Sniffer.experience(0)
Mushroom_Sniffer.speed(100)
Mushroom_Sniffer.behavior(summonable=0, hostile=True, illusionable=False, convinceable=0, pushable=True, pushItems=False, pushCreatures=False, targetDistance=1, runOnHealth=74)
Mushroom_Sniffer.walkAround(energy=0, fire=0, poison=0)
Mushroom_Sniffer.immunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
Mushroom_Sniffer.voices("Oink", "Sniff sniff", "Uuuoink") #made up
Mushroom_Sniffer.melee(0)