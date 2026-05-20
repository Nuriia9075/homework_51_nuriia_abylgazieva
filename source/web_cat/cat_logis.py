import random


class Cat:
    lv1 = "images/cat_angry.jpg"
    lv2 = "images/cat_sad.jpg"
    lv3 = "images/cat_happy.jpg"
    lv4 = "images/cat_super.jpg"

    def __init__(self, name):
        self.name = name
        self.age = 1
        self.lv_happy = 40
        self.lv_satiety = 40
        self.sleeping = False
        self.stat = self.get_stats()

    def get_stats(self):
        if 0 <= self.lv_happy <= 30:
            return self.lv1
        elif 30 < self.lv_happy <= 60:
            return self.lv2
        elif 60 < self.lv_happy <= 80:
            return self.lv3
        else:
            return self.lv4

    def validator(self, value):
        return min(100, max(0, value))

    def play(self):
        if self.sleeping:
            self.sleeping = False
            self.lv_happy = self.validator(self.lv_happy - 5)
            return
        if random.randint(1, 3) == 1:
            self.lv_happy = 0
            self.lv_satiety -= 10
        else:
            self.lv_happy += 15
            self.lv_satiety -= 10
        self.lv_happy = self.validator(self.lv_happy)
        self.lv_satiety = self.validator(self.lv_satiety)
        self.stat = self.get_stats()

    def sleep(self):
        if self.sleeping: self.sleeping = False
        else: self.sleeping = True
        self.stat = self.get_stats()

    def feed(self):
        if self.sleeping:
            return
        self.lv_happy += 5
        self.lv_satiety += 15
        if self.lv_satiety > 100:
            self.lv_happy -= 30
        self.lv_satiety = self.validator(self.lv_satiety)
        self.lv_happy = self.validator(self.lv_happy)
        self.stat = self.get_stats()
