# create a classs that have user meal plan, and weight/height and the user's goal
import json


class User:
    # create the attributes of the user
    def __init__(self, json_path):
        self.json_path = json_path
        if json_path.exists():
            with open(self.json_path) as f:
                data = json.load(f)
                self.weight = data['weight']
                self.height = data['height']
                self.goal = data['goal']
                self.meal_plan = data['meal_plan']
                self.workouts_plan = data['workouts_plan']
        else:
            self.weight = ''
            self.height = ''
            self.goal = ''
            self.meal_plan = ''
            self.workouts_plan = ''

    # generate teh getter and setter methods for the user's attributes
    # create a method that will set the user's weight
    def set_weight(self, weight):
        self.weight = weight

    # create a method that will set the user's height
    def set_height(self, height):
        self.height = height

    # create a method that will set the user's goal
    def set_goal(self, goal):
        self.goal = goal

    # create a method that will set the user's meal plan
    def set_meal_plan(self, meal_plan):
        self.meal_plan = meal_plan

    # create a method that will set the user's workouts plan
    def set_workouts_plan(self, workouts_plan):
        self.workouts_plan = workouts_plan

    # create a method that will return the user's weight
    def get_weight(self):
        return self.weight

    # create a method that will return the user's height
    def get_height(self):
        return self.height

    # create a method that will return the user's goal
    def get_goal(self):
        return self.goal

    # create a method that will return the user's meal plan
    def get_meal_plan(self):
        return self.meal_plan
