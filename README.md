# BioPunkRL
BioPunk Roguelike. First attempt at making a real game.

# Story
Post apocalyptic world, with several factions vying for control. Remnants of the old, technologically advanced civilization exist, and are highly sought after.

## Goal
I have no idea! Will try to figure this out.

## Factions
1. ?Name? Necromancers that believe they have mastered life and death. They largely forgo the cybernetic enhancements in favor of re-animating corpses, and fusing body parts together. They believe death is simply the next step, and not the end.
2. ?Name? Magic worshippers, that believe the technology of the old-world is what destroyed them, and using those technologies will result in the destruction of everything.
3. ?Name? Hoarders of technology and knowledge. They believe they're the saviors of the wasteland, but they are extremely protective of their knowledge, and do not share with others. Very untrusting of strangers.

### Reputation
The player has a reputation score with each faction. This can be influenced by the player's build, and by completing quests for the faction. Completing quests for rival factions can decrease your faction reputation, however.
  
## Quests
Main quests will be hand-crafted, but will be chosen at random. The goal is to have a large variety of quests so the player isn't just repeating the same static quests. I might try to set up some procedural quest generation in the future for some minor quests, but want to avoid the standard fetch quest / kill x enemies quests.

# Progression
There are no levels or experience points, per se, but you will find vials of genetic material <need to flesh this part out> that will grant "genetic points" that can be spent either creating/upgrading your minions, grafting cybernetic/genetic enhancements onto yourself, or used for magic power. Creating minions is optional, but can be very powerful. The player can also spread these points between an army of minions or one or two very powerful minions. Genetic points for destroyed minions or parts will be refunded, but they can't be spent during combat. Would like some permanency in upgrade decisions, but don't want to punish the player too harshly if their minions die. Perhaps the points are permanently spent on specific aspects of a minion, but that minion can be rebuilt with new parts that fit the points you already spent.

# Combat
Ranged and melee combat should be viable. The player should have very powerful offense, but unless they spend a lot of points upgrading themselves, rather than their minions, they should be fairly fragile. The intention is that the minions will help deal with threats before they can reach the player, or defend the player from attack.

## Magic
Magic will be very short ranged, but minions can be equipped with a device that allows the player to channel magic through them. This allows the spell range to be greatly extended, especially with multiple minions using these devices. They are expensive, however, so minions using them will generally be much weaker than those focused solely on combat. Magic should primarily be focused on battlefield control, rather than simple ranged damage. Still need to figure out if I will use MP or 

## Minion AI
The minion's AI will be set by the player, using something similar to the Gambit system from Final Fantasy XII. The conditions and actions must be discovered in the world before they can be used. Ideally, the player should eventually be able to create a state machine with more advanced options. Since the player will be controlling movement as well as actions, it will necessarily be more complicated than the FFXII Gambit system. I'll need to prototype this to make it manageable.
