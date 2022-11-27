import os
# from time import sleep

print("""
============  HOME  ============
Commands List:
To add entry - add
To edit entry - edit
To view entries - view
To remove entry - del
To go back home - back
To quit program - exit
""")


def clear():
    return os.system('cls')


def add_entry():
    with open('grocery.txt', 'a') as file:
        print("Note: Enter each unique entry on a new line.\nType 'exit' to finish")
        while True:
            new_entry = input("Enter grocery or exit: ").title()
            if new_entry.lower() == "exit":
                break
            file.write(new_entry)
            file.write('\n')
        print("New entry/entries added successfully")


def view_entries():
    with open('grocery.txt') as file:
        print(file.read())


def delete_entry():
    with open('grocery.txt', 'r') as file:
        file_items = file.readlines()
        index = 0
        for item in file_items:
            print(f'{index} -  {item}')
            index += 1
        try:
            delete_item = int(input("Enter the INDEX of item to be deleted: "))
            index = 0
            for item in file_items:
                if delete_item == file_items.index(item):
                    file_items.pop(index)
                    break
                index += 1
        except ValueError:
            print("Please enter a number - try again")
            return
    file = open("grocery.txt", 'w')
    for item in file_items:
        file.write(item)
    file.close()


def edit_entry():
    with open('grocery.txt', 'r') as file:
        file_items = file.readlines()
        index = 0
        for item in file_items:
            print(f'{index} -  {item}')
            index += 1
        try:
            edit_item = int(input("Enter the INDEX of item to be edited: "))
            index = 0
            for item in file_items:
                if edit_item == file_items.index(item):
                    replace_text = input("Enter new item: ")
                    file_items[index] = replace_text + '\n'
                    break
                index += 1
        except ValueError:
            print("Please enter a number - try again")
    file = open("grocery.txt", 'w')
    for item in file_items:
        file.write(item)
    file.close()


while True:
    # sleep(2)
    # clear()
    user_cmd = input(">>> ")
    if user_cmd.lower() == "exit":
        break
    elif user_cmd.lower() == "view":
        view_entries()
    elif user_cmd.lower() == "add":
        add_entry()
    elif user_cmd.lower() == "del":
        delete_entry()
    elif user_cmd.lower() == "edit":
        edit_entry()
