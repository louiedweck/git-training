checklist = []

def create(item):
    checklist.append(item)

def test_create():
    item_count = len(checklist)

    create("one")
    create("two")
    create("three")

    if len(checklist) != item_count + 3:
        print("CREATE BROKEN: Item count does not increment.")
    if checklist[len(checklist)-1] != "three":
        print("CREATE BROKEN: Newest item is different than expected.")

def read(index):
    return checklist[index]

def test_read():
    if read(0) is not 'one':
        print('Read broken: expected "one", got', read(0))
    if read(1) is not 'two':
        print('Read broken: expected "two", got', read(1))
    if read(2) is not 'three':
        print('Read broken: expected "three", got', read(2))

def update(index, item):
    checklist[index] = item

def test_update():
    update(0, "updated one")
    update(1, "updated two")
    update(2, "updated three")

    if read(0) is not 'updated one':
        print('Read broken: expected "updated one", got', read(0))
    if read(1) is not 'updated two':
        print('Read broken: expected "updated two", got', read(1))
    if read(2) is not 'updated three':
        print('Read broken: expected "updated three", got', read(2))

def delete(index):
    checklist.pop(index)

def test_delete():
    delete(1)
    
    if read(1) == 'updated two':
        print("DELETE BROKEN: Expected 'updated two' to have been removed.")
    
    delete(1)
    if len(checklist) is not 1:
        print("DELETE BROKEN: Expected length of checklist to be 1")

def test_all():
    test_create()
    test_read()
    test_update()
    test_delete()

def list_all_items():
    for list_item in checklist:
        print(list_item)

    
def mark_completed(index): # Add code here that marks an item as completed# Add code here that marks an item as completed
    checked = "√ " + checklist[index]
    update(index,checked)
    return checklist[index]

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input
def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")
        if item_index not in range(len(checklist)):
            print('Go back, you messed up!')
        else:
            print(read(item_index))

        # Remember that item_index must actually exist or our program will crash.
        read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    elif function_code == "Q":
        return False

    # Catch all
    else:
        print("Unknown Option")

    return True
    
running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list and P to display list, Q to quit.")
    running = select(selection)
