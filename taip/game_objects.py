class Game():
    def __init__(self, intro="", goal=0, score=0):
        self._intro = intro
        self._goal = goal
        self._score = 0

    @property
    def intro(self):
        return self._intro

    @intro.setter
    def start(self, val):
        self._intro = val

    def start_game(self):
        if self._intro != ""
            print(intro)
        else:
            print("No intro set yet.")

    @property
    def goal(self):
        return self._goal

    @goal.setter
    def goal(self, val):
        self._goal = val

    @property
    def score(self):
        return self._score

    def incr_score(self):
        self._score += 1

    def check_win(self):
        return goal == score

class Room():
    def __init__(self, name, desc="", contains=[], n=None, e=None, s=None, w=None):
        self._name = name
        self._desc = desc
        self._contains = contains
        self._n = n
        self._s = s
        self._e = e
        self._w = w

    @property
    def name(self):
        return self._name

    @property
    def desc(self):
        return self._description

    @desc.setter
    def desc(self, val):
        self._desc = val

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
    def __init__(self, pos=None, inventory=[]):
        self._pos = pos
        self._inventory = inventory

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, val):
        self._pos = val

    def check(self, item):
        item.check()


    @property
    def inventory(self):
        return self._inventory

    def pickup(self, item):
        self._inventory.append(item)
        item.pickup()
    
class Items():
    def __init__(self, name, desc="", contains=[], checked=False, pickedup=False):
        self._name = name 
        self._desc = desc
        self._contains = contains
        self._visited = visited
        self._pickedup = pickedup

    @property
    def desc(self):
        return self._desc
    
    @desc.setter
    def desc(self, val):
        self._desc = val

    @property
    def contains(self):
        return self._contains
    
    @contains.setter
    def contains(self, val):
        self._contains = val

    @property
    def desc(self):
        return self._desc
    
    @desc.setter
    def desc(self, val):
        self._desc = val

    @property
    def contains(self):
        return self._contains

    def is_empty(self):
        return len(self._contains == 0)

    def add_child(self, item):
        self._contains.append(item)

    @property 
    def checked(self):
        return self._checked

    def check(self):
        self._checked = True

    @property
    def pickedup(self):
        return self._pickedup

    def pickup(self):
        self._pickedup = True    


    
