from itertools import combinations, product
class player: 
	def __init__(self, hp, armor, damage): 
		self.hp  = hp
		self.armor = armor
		self.damage = damage
def part_1(): 
	weapons = {"Dagger":(       8    , 4       ,0), 
"Shortsword"  : (10   ,  5,       0),
"Warhammer"   :(25   ,  6   ,    0),
"Longsword"  :( 40   ,  7  ,     0),
"Greataxe"   : (74    , 8    ,   0)}
	armor = {
		"Leather"  :  (   13   ,  0    ,   1), 
"Chainmail"  :  (31 ,    0    ,   2),
"Splintmail"  :  (53   ,  0   ,    3),
"Bandedmail" : (  75  ,   0   ,    4),
"Platemail" :(  102  ,   0   ,    5), 
"None": (0,0,0)
	}
	rings= {
		"Damage +1": (   25  ,   1    ,   0),
"Damage +2":    (50 ,    2    ,   0),
"Damage +3":   (100  ,   3   ,    0),
"Defense +1":  ( 20  ,   0     ,  1),
"Defense +2":(  40   ,  0     ,  2),
"Defense +3":   (80  ,   0     ,  3)
	}
	min_cost = 0
	for w in weapons: 
		for a in armor: 
			for r in range(3): 
				comb = combinations(rings.keys(), r)
				for c in comb: 
					attr = [weapons[w], armor[a]] + [rings[k] for k in c]
					cost = sum(b[0] for b in attr)
					dam = sum(b[1] for b in attr)
					ar = sum(b[2] for b in attr)
					if not playout(player(100, ar, dam)): 
						min_cost=max(min_cost, cost)
	print(min_cost)

					 


def playout(p: player):
	boss = player(109, 2, 8)
	pd = max(p.damage-boss.armor, 1)
	bd = max(boss.damage-p.armor, 1)
	br = int(boss.hp/pd)+1 if boss.hp % pd else int(boss.hp/pd)
	pr = int(p.hp/bd)+1 if p.hp % bd else int(p.hp/bd)
	return pr >= br
	


part_1()