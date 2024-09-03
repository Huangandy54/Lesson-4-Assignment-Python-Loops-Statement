# Objective:
# The aim of this assignment is to practice using nested loops in Python. You will correct a nested loop code snippet, simulate a mood tracker, and generate a multiplication table.

# Task 1: Your Mood Tracker
# Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week. Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day. For each time, randomly select a mood from a predefined list and print it.

# Example Outcome: An example would be "On Tuesday afternoon you were sad" "On Tuesday night you were happy" "On Wednesday morning you were tired"

import random
moods = ["Happy", "Sad", "Energetic", "Calm"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time_of_day = ["Morning", "Afternoon", "Evening"]

for day in range(7):
    for time in range(3):
        mood= random.choice(moods)
        print(f"On {days_of_week[day]} {time_of_day[time]} you were feeling {mood}")

