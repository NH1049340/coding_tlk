print("Welcome to the Day of the Week Activity Recommender!")
# Store the day in a variable
day = input("What is the day today: ")
# Use conditional statements to recommend an activity based on the day.
if day == "monday":
    print("Start your week with a workout!")
elif day == "tuesday":
    print("It's a great day to read a book!")
elif day == "wednesday":
    print("Mid-week movie night!")
elif day == "thursday":
    print("Try a new recipe!")
elif day == "friday":
    print("Relax and enjoy the weekend!")
elif day == "saturday":
    print("Go for a hike!")
elif day == "sunday":
    print("Prepare for the week ahead with some self-care.")
else:
    print("Invalid input. Please enter a valid day of the week!")
