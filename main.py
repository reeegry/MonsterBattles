from monsters import Flee, Cordelia
from natures import Fire
f = Flee()
c = Cordelia()
f.enemy = c
c.enemy = f
print(c.__dict__)
print(f.__dict__)
f.abilities_list[0].use()
print(c.__dict__)
c.abilities_list[0].use()
print(f.__dict__)
print(f.hp)