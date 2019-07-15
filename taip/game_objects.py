class Game():
    def __init__(self, entry=None, goal=0, score=0):
        self._entry = entry
        self._goal = goal
        self._score = 0

    @property
    def entry(self):
        return self._entry

    @entry.setter
    def entry(self, val):
        self._entry = val

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

class Room():

    def __init__(self, name, description=None, detail=None, neighbors=None, children=None):
        self._name = name
        self._description = description
        self._detail = detail
        self._neighbors = neighbors
        self._children = children

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
    def detail(self):
        return self._detail

    @detail.setter
    def detail(self, val):
        self._detail = val

    @property
    def neighbors(self):
        return self._neighbors

    @neighbors.setter
    def neighbors(self, val):
        self._neighbors = val

    def has_children(self):
        return self._children is not None

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, val):
        self._children = val

class Item():

    def __init__(self, name, description, children=None):
        self._name = name
        self._description = description
        self._children = children
        self._checked = False
    
    @property
    def name(self):
        return self._name

    @property
    def desc(self):
        return self._description

    @desc.setter
    def desc(self, val):
        self._description = val

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, val):
        self._children = val

    @property
    def checked(self):
        return self._checked
    
    def check(self):
        self._checked = True

