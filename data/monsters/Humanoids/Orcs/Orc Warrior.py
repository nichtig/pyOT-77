
orc_warrior = genMonster("Orc Warrior", 7, 5979)
orc_warrior.health(125)
orc_warrior.type("blood")
orc_warrior.defense(armor=17, fire=1, earth=1.1, energy=0.7, ice=1, holy=0.9, death=1.1, physical=1, drown=1)
orc_warrior.experience(50)
orc_warrior.speed(190)
orc_warrior.behavior(summonable=360, hostile=True, illusionable=True, convinceable=360, pushable=False, pushItems=True, pushCreatures=True, targetDistance=1, runOnHealth=11)
orc_warrior.walkAround(energy=1, fire=1, poison=1)
orc_warrior.immunity(paralyze=0, invisible=0, lifedrain=0, drunk=0)
orc_warrior.voices("Alk!", "Trak grrrr brik.", "Grow truk grrrr.")
orc_warrior.melee(60)
orc_warrior.loot( (2148, 100, 15), ("meat", 15.75), ("chain armor", 7.25), ("skull belt", 1.25), ("orc tooth", 0.75), ("orc leather", 4.0), ("broken helmet", 10.25), ("copper shield", 0.5), ("poison dagger", 0.0025) )