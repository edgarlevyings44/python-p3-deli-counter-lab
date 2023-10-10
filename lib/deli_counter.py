
katz_deli = []
def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        line_message = "The line is currently:"
        for i, person in enumerate(katz_deli, start=1):
            line_message += f" {i}. {person}"
        print(line_message)

line(["Lindsey","Liam", "Levy", "Lacey","Leroy"])  


def take_a_number(katz_deli, new_person):
    katz_deli.append(new_person)
    position = len(katz_deli)
    print(f"Welcome, {new_person}. You are number {position} in line.")
    
katz_deli = ['Liam', 'Levy', 'Lacey', 'Leroy']
take_a_number(katz_deli,'Lindsey' )


def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        serving = katz_deli.pop(0)
        print(f"Currently serving {serving}.")

katz_deli = ['Liam', 'Levy', 'Lacey', 'Leroy'] 
now_serving(katz_deli)       