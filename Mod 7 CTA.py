course_info = {
    "CSC101": ["Room Number: 3004", "Instructor: Haynes", "Meeting Time: 8:00am"],
    "CSC102": ["Room Number: 4501", "Instructor: Alvarado", "Meeting Time: 9:00am"],
    "CSC103": ["Room Number: 6755", "Instructor: Rich", "Meeting Time: 10:00am"],
    "NET110": ["Room Number: 1244", "Instructor: Burke", "Meeting Time: 11:00am"],
    "COM241": ["Room Number: 1411", "Instructor: Lee", "Meeting Time: 1:00pm"]
}

course_number = input("Enter a course number: ")

try:
    info = course_info[course_number]
    print(info[0])  # Room Number
    print(info[1])  # Instructor
    print(info[2])  # Meeting Time
# Message if invalid course number was entered   
except KeyError:
    print("Error: Invalid course number.")
