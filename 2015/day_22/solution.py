import heapq

class player: 
	def __init__(self, hp, armor, damage, mana=500):
		self.mana = mana
		self.hp  = hp
		self.armor = armor
		self.damage = damage 
		self.shield_cd = 0 
		self.pois_cd = 0 
		self.mana_cd = 0 
		self.mana_spent = 0
		self.names = []
	
	def copy(self): 
		p2 = player(self.hp, self.armor, self.damage, self.mana)
		p2.shield_cd =self.shield_cd
		p2.pois_cd = self.pois_cd
		p2.mana_cd = self.mana_cd
		p2.mana_spent = self.mana_spent
		p2.names = self.names.copy()
		return p2
	
	def __lt__(self, other): 
		return True
	
	def __gt__(self, other): 
		return True




def do_move(p, b, spell, name): 
	play:player = p.copy()
	play.names.append(name)
	boss:player = b.copy() 
	play.hp -= 1
	if play.hp < 1: 
		return None
	#return None if illegal Move
	if spell[3] and play.shield_cd > 1: 
		return None
	if spell[4] and play.pois_cd > 1: 
		return None	
	if spell[5] and play.mana_cd > 1: 
		return None
	
	## Player turn starts
	if play.mana_cd: 
		play.mana += 101
		play.mana_cd -= 1
	
	if play.mana < spell[0]: 
		return None 
	
	if play.pois_cd: 
		boss.hp -= 3
		play.pois_cd -= 1

	if play.shield_cd: 
		play.armor = 7
		play.shield_cd -= 1
	else: 
		play.armor = 0

	play.shield_cd += spell[3]
	play.pois_cd += spell[4]
	play.mana_cd += spell[5]
	play.mana_spent+= spell[0]
	play.mana -= spell[0]
	boss.hp -= spell[1]
	play.hp += spell[2]

	## Boss turn starts

	if play.mana_cd: 
		play.mana += 101
		play.mana_cd -= 1
	
	if play.pois_cd: 
		boss.hp -= 3
		play.pois_cd -= 1

	if play.shield_cd: 
		play.armor = 7
		play.shield_cd -= 1

	if not play.shield_cd: 
		play.armor = 0

	if boss.hp > 0: 
		play.hp -= max(1, boss.damage - play.armor)
	
	return (play.mana_spent, play, boss)

def part_1(): 
	#Name: (cost, damage, healing, armor_cd, poison_cd, mana_cd)
	spells = {
		"Magic": (53, 4, 0, 0, 0, 0), 
		"Drain": (73, 2, 2, 0, 0, 0), 
		"Shield": (113, 0, 0, 6, 0, 0), 
		"Poison": (173, 0, 0, 0, 6, 0), 
		"Recharge": (229, 0, 0, 0, 0, 5)
	}
	frontier = []
	boss:player = player(71, 0, 10)
	p: player = player(50, 0, 0, 500)
	heapq.heappush(frontier, (p.mana_spent, p, boss))
	while len(frontier): 
		cost, p, boss = heapq.heappop(frontier)
		if p.hp <= 0: 
			continue
		if boss.hp <= 0: 
			break
		for name, spell in spells.items(): 
			a = do_move(p, boss, spell, name)
			if a is not None: 
				heapq.heappush(frontier, a)

	print(p.mana_spent)
	print(p.names)
part_1()

#1102 too low
