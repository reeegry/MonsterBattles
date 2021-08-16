from monsters import Flee, Cordelia
from natures import Fire
from environment import app

if "__main__" == __name__:
    f = Flee()
    c = Cordelia()
    f.enemy = c
    c.enemy = f
    f.abilities_list[0].use()
    c.abilities_list[0].use()
    app.run()