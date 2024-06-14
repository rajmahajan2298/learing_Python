# Class & Object

import datetime


class CricketPlayer:
    def __init__(self, fname, lname, birth_year, team):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birth_year
        self.team = team
        self.scores = []

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year

    def add_score(self, score):
        self.scores.append(score)

    def get_average_score(self):
        return sum(self.scores) / len(self.scores)

    def get_max_score(self):
        return max(self.scores)

    def get_min_score(self):
        return min(self.scores)

    def get_total_score(self):
        return sum(self.scores)

    def __lt__(self, other):
        my_score = self.get_average_score()
        other_score = other.get_average_score()
        return my_score < other_score

    def __gt__(self, other):
        my_score = self.get_average_score()
        other_score = other.get_average_score()
        return my_score > other_score

    def __str__(self):
        return f"{self.first_name} {self.last_name} the cricket player from {self.team}"


virat = CricketPlayer('virat', 'kohli', 1988, 'India')
virat.add_score(89)
virat.add_score(100)
virat.add_score(120)

david = CricketPlayer('david', 'warner', 1985, 'Australia')
david.add_score(85)
david.add_score(98)
david.add_score(105)

print(virat.get_average_score())
print(virat.get_age())

print(david.get_average_score())
print(david.get_age())

print(virat < david)
print(virat > david)

print(virat)
print(david)

print(virat.get_max_score())
print(david.get_max_score())

print(virat.get_min_score())
print(david.get_min_score())

print(virat.get_total_score())
print(david.get_total_score())