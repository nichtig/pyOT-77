instant = spell.Spell("Divine Healing", "exura san", icon=125, target=TARGET_SELF, group=HEALING_GROUP)
instant.require(mana=160, level=35, maglevel=0, learned=0, vocations=(3, 7))
instant.cooldowns(1, 1)
instant.effects(target=EFFECT_MAGIC_BLUE)
instant.targetEffect(callback=spell.heal(10, 20, 60, 90))