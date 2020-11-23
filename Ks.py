class Ks:
    name = ""
    category = ""
    bigCategory = ""
    day = 0
    goal = 0
    pleged = 0
    state = True
    
    def __init__(self, name, category, bigCategory, day, goal, pleged, backers, state):
        self.name = name
        self.category = category
        self.bigCategory = bigCategory
        self.day = day
        self.goal = goal
        self.state = state
        self.pleged = pleged
        self.backers = backers