# DOTA2 GRAPH DATA
The file dota2graph.pickle contains a graph of hero characters as nodes that are connected to each other.
An edge is created if two heroes have a Jaccard Similarity over 0.4 between the combined set of top 5 items often bought in each game state {game_start, early_game, mid_game, late_game}. 

Heroes with no edges have been removed from the graph.

Data has been collected from https://docs.opendota.com/

# DOTA2 DATA
The file dota2.csv contains a table with various attributes of hero characters from the video games Dota2.

The data has been collected from following sources:
https://dota2.fandom.com/wiki/Table_of_hero_attributes
https://liquipedia.net/dota2/


Each row represents one hero, and each column a specific attribute.   

Collumns contains the following information:

**HERO**: Name of the character
<br>
**A**: Main attribute (Class) type of the character {Strength, Agility, Intelligence, Universal}
<br>
**STR**: Base Strength value
<br>
**STR+**: Strength growth per level
<br>
**STR30**: Strength at level 30 (Max level)
<br>
**AGI**: Base Agility value
<br>
**AGI+**: Agility growth per level
<br>
**AGI30**: Agility at level 30 (Max level)
<br>
**INT**: Base Intelligence value
<br>
**INT+**: Intelligence growth per level
<br>
**INT30**: Intelligence at level 30 (Max level)
<br>
**T**: Total sum of base Strength, Agility and Intelligence.
<br>
**T+**: Total growth per level of Strength, Agility and Intelligence.
<br>
**T30**: Total sum of of Strength, Agility and Intelligence at level 30 (Max level)
<br>
**MS**: Movement speed of character
<br>
**AR**: Starting Armor
<br>
**DMG_MIN**: Starting minimum of Attack damage
<br>
**DMG_MAX**: Starting maximum of Attack damage
<br>
**RG**: Attack range
<br>
**AS**: Attack speed
<br>
**BAT**: Base Attack time
<br>
**ATK_PT**: Attack point
<br>
**ATK_BS**: Attack back swing
<br>
**VS-D**: Vison range during daytime
<br>
**VS-N**: Vison range during nightime
<br>
**TR**: Turn rate of character
<br>
**COL**: Collision size
<br>
**HP/S**: Base health regeneration per second
<br>
**MP/S**: Base mana regeneration per second
<br>
**Complexity**: Difficulty rating of character {1,2,3}
<br>
**Legs**: The character's number of legs (Not including mounts)
<br>
**Release**: First release year of the character
<br>
**Artifact**: Character was included in the initial release of the very popular and well received game Artifact (Binary)
