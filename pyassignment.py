
# QUESTION 1

import random

# Base class
class Superhero:
    def __init__(self, name, alias, power_level):
        self.name = name
        self.alias = alias
        self.power_level = power_level

    def display_info(self):
        print(f"\nName: {self.name}")
        print(f"Alias: {self.alias}")
        print(f"Power Level: {self.power_level}")

    def use_power(self):
        print(f"{self.alias} uses their generic superhero powers!")

# FlyingHero subclass
class FlyingHero(Superhero):
    def __init__(self, name, alias, power_level, flight_speed):
        super().__init__(name, alias, power_level)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.alias} soars through the sky at {self.flight_speed} mph!")

# StrengthHero subclass
class StrengthHero(Superhero):
    def __init__(self, name, alias, power_level, lifting_capacity):
        super().__init__(name, alias, power_level)
        self.lifting_capacity = lifting_capacity

    def use_power(self):
        print(f"{self.alias} lifts {self.lifting_capacity} tons with super strength!")

# Team class
class SuperheroTeam:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def team_power(self):
        return sum(hero.power_level for hero in self.heroes)

    def show_team(self):
        print(f"\n🛡️ Team {self.name} Roster:")
        for hero in self.heroes:
            hero.display_info()

    def battle(self, other_team):
        print(f"\n🔥 Battle Begins: Team {self.name} VS Team {other_team.name} 🔥")
        power1 = self.team_power()
        power2 = other_team.team_power()

        print(f"\nTeam {self.name} Total Power: {power1}")
        print(f"Team {other_team.name} Total Power: {power2}")

        if power1 > power2:
            print(f"\n🏆 Team {self.name} WINS the battle!")
        elif power2 > power1:
            print(f"\n🏆 Team {other_team.name} WINS the battle!")
        else:
            print("\n🤝 It's a TIE!")

# --- Create Heroes ---
supergirl = FlyingHero("Kara Zor-El", "Supergirl", 95, 1200)
hulk = StrengthHero("Bruce Banner", "Hulk", 98, 100)
ironman = Superhero("Tony Stark", "Iron Man", 85)
thor = StrengthHero("Thor Odinson", "Thor", 90, 150)
falcon = FlyingHero("Sam Wilson", "Falcon", 75, 600)
captain_marvel = FlyingHero("Carol Danvers", "Captain Marvel", 96, 1300)
black_widow = Superhero("Natasha Romanoff", "Black Widow", 70)
spiderman = Superhero("Peter Parker", "Spider-Man", 80)

# --- Create Teams ---
team_alpha = SuperheroTeam("Alpha Avengers")
team_beta = SuperheroTeam("Beta Defenders")

# Add heroes to Team Alpha
team_alpha.add_hero(supergirl)
team_alpha.add_hero(ironman)
team_alpha.add_hero(spiderman)
team_alpha.add_hero(black_widow)

# Add heroes to Team Beta
team_beta.add_hero(hulk)
team_beta.add_hero(thor)
team_beta.add_hero(falcon)
team_beta.add_hero(captain_marvel)

# --- Display Team Info ---
team_alpha.show_team()
team_beta.show_team()

# --- Start the Battle ---
team_alpha.battle(team_beta)


# QUESTION 2

# Base class
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

# Subclass 1
class Car(Vehicle):
    def move(self):
        print("🚗 The car is driving on the road.")

# Subclass 2
class Plane(Vehicle):
    def move(self):
        print("✈️ The plane is flying in the sky.")

# Subclass 3
class Boat(Vehicle):
    def move(self):
        print("🚤 The boat is sailing on the water.")

# Subclass 4
class Bicycle(Vehicle):
    def move(self):
        print("🚴‍♂️ The bicycle is pedaling down the path.")

# Function that accepts any vehicle and calls its move method
def travel(vehicle):
    vehicle.move()

# --- Create vehicle instances ---
my_car = Car()
my_plane = Plane()
my_boat = Boat()
my_bike = Bicycle()

# --- Use the same function for different vehicle types ---
print("Travel Log:")
travel(my_car)
travel(my_plane)
travel(my_boat)
travel(my_bike)
