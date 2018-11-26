# AdultING Classes

class Human(object):
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.career = 10
        self.adventure = 10
        self.love = 10
        self.finance = 10
        self.growth = 10
        self.total = self.health + self.career + self.adventure + self.love + self.finance + self.growth
    def __repr__(self):
        return "Levels --> Health: %d, Career: %d, Adventure: %d, Love: %s, Finance: %d, Growth: %d " % (self.health, self.career, self.adventure, self.love, self.finance, self.growth)
    def health_adjust(self, health_change):
        self.health += health_change
    def career_adjust(self, career_change):
        self.career += career_change
    def adv_adjust(self, adventure_change):
        self.adventure = self.adventure + adventure_change
    def love_adjust(self, love_change):
        self.love += love_change
    def finance_adjust(self, finance_change):
        self.finance += finance_change
    def growth_adjust(self, growth_change):
        self.growth += growth_change
    def print_warning(self):
        print "Be careful about the choices you make, levels are getting low!"
    def print_congrats(self):
        print "Way to go, doll, you're doin' alright!"
    def update_total(self):
        self.total = self.health + self.career + self.adventure + self.love + self.finance + self.growth

# ====================================== #

class Life(object):
    def __init__(self, person):
        self.levels = 60
        self.person = person # CAN I PASS IT AN OBJ HERE? A HUMAN WHO IT AFFECTS
    def adjust_levels(self, adjust):
        self.levels += adjust
