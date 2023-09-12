progress_data = {}

def log_progress():
    exercise = input("Enter the name of the exercise: ")
    weight = float(input("Enter the weight lifted (in kg): "))
    sets = int(input("Enter the number of sets: "))
    reps = int(input("Enter the number of reps: "))
    
    total_weight_lifted = weight * sets * reps
    
    if exercise in progress_data:
        progress_data[exercise]["Total Weight Lifted"] += total_weight_lifted
        progress_data[exercise]["Total Sets"] += sets
        progress_data[exercise]["Total Reps"] += reps
    else:
        progress_data[exercise] = {
            "Total Weight Lifted": total_weight_lifted,
            "Total Sets": sets,
            "Total Reps": reps
        }

def display_progress():
    print("\nProgress Tracker")
    print("-----------------")
    
    if not progress_data:
        print("No progress data available.")
    else:
        for exercise, data in progress_data.items():
            print(f"\nExercise: {exercise}")
            print(f"Total Sets: {data['Total Sets']}")
            print(f"Total Reps: {data['Total Reps']}")
            print(f"Total Weight Lifted: {data['Total Weight Lifted']} kg")

while True:
    print("\nOptions:")
    print("1. Log Progress")
    print("2. Display Progress")
    print("3. Quit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        log_progress()
    elif choice == "2":
        display_progress()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
