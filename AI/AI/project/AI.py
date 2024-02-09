def is_valid(schedule, section, classroom, day, time_slot):
    for key in schedule:
        s, d, t = key  # Adjust here to unpack only day and time_slot
        if d == day and t == time_slot and schedule[key] == classroom:
            return False
    return True

def allocate_classrooms(sections, classrooms, time_slots, days):
    schedule = {}

    def backtrack(section_index):
        nonlocal schedule
        if section_index == len(sections):
            return True  # All sections are scheduled

        section = sections[section_index]
        for day in days:
            for time_slot in time_slots:
                for classroom in classrooms:
                    if is_valid(schedule, section, classroom, day, time_slot):
                        schedule[day, time_slot] = classroom  # Update key structure

                        if backtrack(section_index + 1):
                            schedule[section, day, time_slot] = classroom  # Store section-classroom mapping
                            return True

                        del schedule[day, time_slot]  # Backtrack

        return False  # No solution found

    if backtrack(0):
        return schedule
    else:
        return None  # No valid schedule found

# Rest of the code remains unchanged


# Sample input
num_classes = int(input("Enter the number of classes: "))
classes = [input(f"Enter class {i+1}: ") for i in range(num_classes)]

num_sections = int(input("Enter the number of sections: "))
sections = [input(f"Enter section {i+1}: ") for i in range(num_sections)]

time_slots = ["9:00 to 11:00", "11:00 to 13:00", "14:00 to 15:00", "15:00 to 16:00"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

result = allocate_classrooms(sections, classes, time_slots, days)

if result:
    print("Classroom Allocation Schedule:")
    for key, value in result.items():
        section, day, time_slot = key
        print(f"{section} -> {value} on {day} at {time_slot}")
else:
    print("No valid schedule found")
