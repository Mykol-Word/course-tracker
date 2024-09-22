import wget
import os

def find_open_slots(page_text):
    open_index = page_text.find("Open: ")
    if (open_index == -1):
        print("Invalid url")
        exit(1)
    open_string = page_text[open_index:]
    open_string = open_string[:open_string.find("<")]

    return open_string


try: 
    os.remove("ClassDetail")
except:
    pass

url = input("Input the course page from the UCLA Registrar's Office Schedule of Classes:")

wget.download(url)

course = open("ClassDetail", encoding="utf8")
course_page = course.read()


print("")
print(find_open_slots(course_page))