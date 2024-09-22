import wget
import os
import time

FILE_NAME = "ClassDetail"

def get_reloaded_page(url):
    try: 
        os.remove(FILE_NAME)
    except:
        pass

    wget.download(url)

    course = open(FILE_NAME, encoding="utf8")
    return course.read()

def find_open_slots(page_text):
    open_index = page_text.find("Open: ")
    if (open_index == -1):
        print("Invalid url")
        exit(1)
    open_string = page_text[open_index:]
    open_string = open_string[:open_string.find("<")]

    return open_string

url = input("Input the course page from the UCLA Registrar's Office Schedule of Classes:")
course_page = get_reloaded_page(url)

open_slots = find_open_slots(course_page)
old_open_slots = open_slots

while open_slots == old_open_slots:
    os.system('cls' if os.name == 'nt' else 'clear')

    print("")
    print(open_slots)

    time.sleep(1)

    course_page = get_reloaded_page(url)
    open_slots = find_open_slots(course_page)

print("")
print("Slots changed to: ")
print("")
print(open_slots)