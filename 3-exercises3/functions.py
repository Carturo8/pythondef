# 1. Library Book Tracker

library:dict = {}

def add_book(book_title:str = "", book_author:str = "", book_pages:int = 0) -> None:
    if book_title in library:
        print(f"The book {book_title} already exists.")
    else:
        library[book_title] = {"Author": book_author, "Pages": book_pages}
        print(f"The book '{book_title}' successfully added.")

def find_book(book_title:str = "") -> str:
    if book_title in library:
        return "Book found."
    else:
        return "Book not found."

def show_books() -> None:
    if library:
        print("Books in the library:")
        for book_title, book_info in library.items():
            print(f"'{book_title}' by {book_info['Author']}, {book_info['Pages']} pages")
    else:
        print(f"The library is empty.")

# 2. Student Grade Manager

grades:dict = {}

def add_student(student_name:str = "") -> None:
    if student_name in grades:
        print(f"The student '{student_name}' already exists.")
    else:
        grades[student_name] = []
        print(f"The student '{student_name}' successfully added.")

def add_grade(student_name:str = "", grade:float = 0) -> None:
    if student_name in grades:
        grades[student_name].append(grade)
        print(f"Student '{student_name}'s' grade '{grade}' was successfully added")
    else:
        print(f"The student '{student_name}' does not exist.")

def get_average(student_name:str = "") -> float:
    average:float = 0.0
    if student_name in grades:
        average = round(sum(grades[student_name]) / len(grades[student_name]), 2)
    else:
        print(f"The student '{student_name}' does not exist.")
    return average

# 3. Restaurant Menu Editor

menu:dict = {}

def add_dish(dish_name:str = "", price:float = 0.0, availability:bool = False) -> None:
    if dish_name in menu:
        print(f"The dish '{dish_name}' already exists.")
    else:
        menu[dish_name] = {"Price": price, "Availability": availability}
        print(f"The dish '{dish_name}' successfully added.")

def change_availability(dish_name:str = "", new_availability:bool = False) -> None:
    if dish_name in menu:
        menu[dish_name]["Availability"] = new_availability
        print(f"The availability ({new_availability}) of the dish '{dish_name}' was successfully changed.")
    else:
        print(f"The dish '{dish_name}' does not exist.")

def total_available_price() -> float:
    total:float = 0.0
    if menu:
        for dish in menu.values():
            if dish["Availability"]:
                total += dish["Price"]
    else:
        print("The menu is empty.")
    return total

# 4. Warehouse Box Counter

warehouse:dict = {}

def add_box(type_of_box:str = "", available_quantity:int = 0) -> None:
    if type_of_box in warehouse:
        print(f"The type of box '{type_of_box}' already exists.")
    else:
        warehouse[type_of_box] = available_quantity
        print(f"The type of box '{type_of_box}' was successfully added with a quantity of ({available_quantity}) units.")

def update_quantity(type_of_box:str = "", new_quantity:int = 0) -> None:
    if type_of_box in warehouse:
        quantity = warehouse[type_of_box] + new_quantity
        warehouse[type_of_box] = quantity
        print(f"The new quantity ({new_quantity}) of the type of box '{type_of_box}' was successfully updated.")
    else:
        print(f"The type of box '{type_of_box}' does not exist.")

def has_enough(type_of_box:str = "", quantity:int = 0) -> bool:
    condition:bool = False
    if type_of_box in warehouse:
        if warehouse[type_of_box] < quantity:
            condition = False
            print(f"There is not enough quantity of the type of box '{type_of_box}'.")
        else:
            condition = True
            print(f"There is enough quantity of the type of box '{type_of_box}'.")
    return condition

# 5. Movie Rating System

movies:dict = {}

def add_movie(movie_title:str = "") -> None:
    if movie_title in movies:
        print(f"The movie '{movie_title}' already exists.")
    else:
        movies[movie_title] = []
        print(f"The movie '{movie_title}' successfully added.")

def rate_movie(movie_title:str = "", rating:int = 0) -> None:
    if movie_title in movies:
        movies[movie_title].append(rating)
        print(f"Rating ({rating}) for the movie '{movie_title}' was successfully added.")
    else:
        print(f"The movie '{movie_title}' does not exist.")

def average_rating(movie_title:str = "") -> float:
    average:float = 0.0
    if movie_title in movies:
        average = round(sum(movies[movie_title]) / len(movies[movie_title]), 2)
        print(f"The average rating for the movie '{movie_title}' is ({average}).")
    else:
        print(f"The movie '{movie_title}' does not exist.")
    return average

# 6. Online Course Tracker

courses:dict = {}

def add_course(course_title:str = "", hours:int = 0, enrollments:int = 0) -> None:
    if course_title in courses:
        print(f"The course '{course_title}' already exists.")
    else:
        courses[course_title] = {"Hours": hours, "Enrollments": enrollments}
        print(f"The course '{course_title}' with ({hours}) hours and ({enrollments}) enrollments was successfully added.")

def update_enrollment(course_title:str = "", new_enrollments:int = 0) -> None:
    if course_title in courses:
        courses[course_title]["Enrollments"] = new_enrollments
        print(f"The new number of enrollments ({new_enrollments}) for the course '{course_title}' was successfully updated.")

def filter_by_hours(hours:int = 0) -> list:
    filtered:list = []
    for course_title, course_info in courses.items():
        if course_info["Hours"] >= hours:
            filtered.append(course_title)
    return filtered

# 7. To-Do List Organizer

todos:dict = {}

def add_task(task_name:str = "", priority:str = "") -> None:
    if task_name in todos:
        print(f"The task '{task_name}' already exists.")
    else:
        todos[task_name] = {"Priority": priority, "Status": "pending"}
        print(f"The task '{task_name}' with priority ({priority}) was successfully added.")

def complete_task(task_name:str = "") -> None:
    if task_name in todos:
        todos[task_name]["Status"] = "completed"
        print(f"The task '{task_name}' was successfully marked as completed.")
    else:
        print(f"The task '{task_name}' does not exist.")

def filter_tasks(priority:str = "", status:str = "") -> list:
    filtered:list = []
    for task_name, task_info in todos.items():
        if task_info["Priority"] == priority and task_info["Status"] == status:
            filtered.append(task_name)
    return filtered

# 8. Digital Wallet

wallet:dict = {}

def add_expense(category:str = "", amount:float = 0) -> None:
    if category in wallet:
        print(f"The expense category '{category}' already exists.")
    else:
        wallet[category] = amount
        print(f"The expense category '{category}' with amount ({amount}) was successfully added.")

def total_spent() -> float:
    total:float = 0.0
    if wallet:
        total = sum(wallet.values())
    else:
        print("The wallet is empty.")
    return total

def expense_percentages() -> dict:
    percentages:dict = {}
    total:float = total_spent()
    for category, expense_amount in wallet.items():
        percentages[category] = round(expense_amount / total * 100, 1)
    return percentages

# 9. Pet Adoption Center

pets:dict = {}

def add_pet(pet_name:str = "", species:str = "", age:int = 0) -> None:
    if pet_name in pets:
        print(f"The pet '{pet_name}' already exists.")
    else:
        pets[pet_name] = {"Species": species, "Age": age}
        print(f"The pet '{pet_name}' with species ({species}) and age ({age}) was successfully added.")

def find_by_species(species:str = "") -> list:
    filtered:list = []
    for pet_name, pet_info in pets.items():
        if pet_info["Species"] == species:
            filtered.append(pet_name)
    return filtered

def older_than(age:int = 0) -> list:
    older:list = []
    for pet_name, pet_info in pets.items():
        if pet_info["Age"] > age:
            older.append({"name": pet_name})
    return older

# 10. Gym Membership System

members:dict = {}

def register_member(member_name:str = "", plan:str = "", status:str = "") -> None:
    if member_name in members:
        print(f"The member '{member_name}' already exists.")
    else:
        members[member_name] = {"Plan": plan, "Status": status}
        print(f"The member '{member_name}' with plan ({plan}) and status ({status}) was successfully added.")

def change_plan(member_name:str = "", new_plan:str = "") -> None:
    if member_name in members:
        members[member_name]["Plan"] = new_plan
        print(f"The new plan ({new_plan}) for the member '{member_name}' was successfully changed.")
    else:
        print(f"The member '{member_name}' does not exist.")

def unpaid_members() -> list:
    unpaid:list = []
    for member_name, member_info in members.items():
        if member_info["Status"] == "late":
            unpaid.append(member_name)
    return unpaid