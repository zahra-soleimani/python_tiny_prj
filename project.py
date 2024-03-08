# if number 1 push
def power(first_num, second_num):
    p = first_num ** second_num
    print(first_num, "^", second_num, "=", p)

# if number 2 push
def count_char(txt):
    letters = {}
    for i in txt:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    print(letters)

# if number 3 push
def personal_info(num):
    people = []
    for i in range (0, num):
        new_person = input("enter ID, Firstname, Lastname (use ',' between each other): ")
        new_item = new_person.split(",")
        people.insert(i, new_item)
    people.sort(key = lambda people:people[2])
    print(people)

# if number 4 push
def draw_square(num):
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            if i == 1 or i == num or j == 1 or j == num:
                print("* ", end = "")
            else:
                print("  ", end = "")
        print()

# if number 5 push
def computer_system_info(num):
    class System:
        def __init__(self, model, cpu, ram, price):
            self.model = model
            self.cpu = cpu
            self.ram = ram
            self.price = price

        def __str__(self):
            return f"{self.model}: CPU = {self.cpu}, RAM = {self.ram}, Price = {self.price}"
    systems = []
    for i in range(num):
        print(f"Enter the information for system {i+1}:")
        model = input("Model: ")
        cpu = int(input("CPU amount: "))
        ram = int(input("RAM amount: "))
        price = int(input("Price: "))
        system = System(model, cpu, ram, price)
        systems.append(system)

    cheapest = systems[0]

    for system in systems[1:]:
        if system.price < cheapest.price:
            cheapest = system
    print("The cheapest system is:")
    print(cheapest)

while True:
    print()
    print("****************************")
    print("1- Power")
    print("2- String")
    print("3- Personal info")
    print("4- Draw Square")
    print("5- Ceapest computer system")
    print("6- Exit")
    print("****************************")
    number = int(input("Please enter number(1-6): "))

    match number:
        case 1:
            x = int(input("enter first number: "))
            y = int(input("enter second number: "))
            power(x, y)
        case 2:
            text = input("enter a string: ")
            count_char(text)
        case 3:
            n = int(input("please enter number of people: "))
            personal_info(n)
        case 4:
            n = int(input("please enter a number: "))
            draw_square(n)
        case 5:
            n = int(input("please enter number of computer systems: "))
            computer_system_info(n)
        case 6:
            break
