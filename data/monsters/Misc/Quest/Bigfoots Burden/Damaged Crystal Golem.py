damaged_crystal_golem = genMonster("Damaged Crystal Golem", 508, 18466)  #unknown blood, heal 10
damaged_crystal_golem.health(500, healthmax=500)
damaged_crystal_golem.type("blood")
damaged_crystal_golem.defense(armor=30, fire=0, earth=1, energy=1, ice=0, holy=1, death=1, physical=0.8, drown=1)
damaged_crystal_golem.experience(0)
damaged_crystal_golem.speed(350)
damaged_crystal_golem.behavior(summonable=0, hostile=True, illusionable=False, convinceable=0, pushable=False, pushItems=True, pushCreatures=True, targetDistance=1, runOnHealth=500)
damaged_crystal_golem.walkAround(energy=0, fire=0, poison=0)
damaged_crystal_golem.immunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
damaged_crystal_golem.melee(150)