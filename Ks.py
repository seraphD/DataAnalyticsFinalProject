class Ks:
    name = ""
    category = ""
    mainCategory = ""
    day = 0
    goal = 0
    state = True
    
    def __init__(self, name, category, mainCategory, day, goal, state):
        self.name = name
        self.category = category
        self.mainCategoty = mainCategory
        self.day = day
        self.goal = goal
        self.state = state