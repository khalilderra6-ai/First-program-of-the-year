#work_sheet1
age = 17
name = "Khalil"

print("Age:", age)
print("Name:", name)


price = 19.99
integer_price = int(price)

print(f"Price: {price}")
print(f"Integer price: {integer_price}")

global_count = 0

def increment_count():
    global global_count
    global_count += 1

increment_count()
increment_count()

print(f"Global count: {global_count}")

#work_sheet2
school_name = "UWC Changshu China"

def show_user_info():
    user_name = "Khalil"
    user_age = 17
    is_student = True

    print(f"Name: {user_name}")
    print(f"Age: {user_age}")
    print(f"Student: {is_student}")
    print(f"School: {school_name}")

show_user_info()