# game objects used in the game

class Room():
    def __init__(self, name, desc="", n=None, e=None, s=None, w=None):
        self._name = name
        self._desc = desc
        self._contains = []
        self._n = n
        self._s = s
        self._e = e
        self._w = w

    def __repr__(self):
        return self._name

    @property
    def name(self):
        return self._name

    @property
    def desc(self):
        return self._desc

    @property
    def contains(self):
        return self._contains

    def contain(self,item):
        self._contains.append(item)

    def is_empty(self):
        return len(self._contains == 0)

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, val):
        self._n = val

    @property
    def s(self):
        return self._s

    @s.setter
    def s(self, val):
        self._s = val

    @property
    def e(self):
        return self._e

    @e.setter
    def e(self, val):
        self._e = val

    @property
    def w(self):
        return self._w

    @w.setter
    def w(self, val):
        self._w = val

class Player():
    def __init__(self, pos=None):
        self._pos = pos
        self._inventory = set()
        self._env = []
        self._commands = ''

    @property
    def env(self):
        return self._env

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, val):
        self._pos = val
    
    @property
    def commands(self):
        return self._commands
    def add_comm(self, comm):
        self._commands += comm
        self._commands += '\n'

    @property
    def inventory(self):
        return self._inventory

    def inventory_dict(self):
        inventory = dict()
        for i in self._inventory:
            inventory[i.name] = i.desc
        return inventory

    def pickup(self, item):
        self._inventory.add(item)
        item.pickup()

    def add_env(self, item):
        self._env += item.contains

    def reset_env(self):
        self._env = []

    def n(self):
        self._pos = self._pos.n

    def e(self):
        self._pos = self._pos.e

    def w(self):
        self._pos = self._pos.w

    def s(self):
        self._pos = self._pos.s
    
    
class Item():
    def __init__(self, name, desc=""):
        self._name = name 
        self._desc = desc
        self._contains = []

    def __repr__(self):
        return self._name

    @property
    def name(self):
        return self._name

    @property
    def desc(self):
        return self._desc

    @property
    def contains(self):
        return self._contains

    def is_empty(self):
        return len(self._contains == 0)

    def contain(self, item):
        self._contains.append(item)

    def pickup(self):
        self._pickedup = True    


    
