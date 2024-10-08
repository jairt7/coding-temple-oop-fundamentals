# Task 2: Event Management System Enhancement
# Last time I referenced the video explaining how to do it. This time, though, I am committed to not doing that.

participants = {}

class Event:
    def __init__(self, name, date, participants):
        self.name = name
        self.date = date
        self.participants = participants

    def add_participant(self):
        how_many = int(input("How many participants would you like to add? Please enter a number: "))
        self.participants += how_many
    
    def get_participant_count(self):
        print(f"There are {self.participants} people participating in this event.")

party = Event("party", "Friday", 3)
party.add_participant()
party.get_participant_count()