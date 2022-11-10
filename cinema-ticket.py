from os import system
system ("cls")

#DATA
m_title_1 = "Avatar 2"
m_title_2 = "Terminator 9"
m_title_3 = "Titamic Zombie"

# HW 1 - variabile time
time_m_title_1_a = "18:00"
time_m_title_1_b = "20:00"
time_m_title_2_a = "16:00"
time_m_title_2_b = "23:00"
time_m_title_3   = "18:00"

m_1_ticket_cost_a = 100.00
m_1_ticket_cost_b = 120.00
m_2_ticket_cost_a = 90.00
m_2_ticket_cost_b = 110.00
m_3_ticket_cost   = 80.00


# Movie Board
print (
    f"""
    1. {m_title_1}
    2. {m_title_2}
    3. {m_title_3}
"""
)

movie_number = input ("Choose a movie: ") # "1"

if movie_number == "1":
    print (f"You've chosen '{m_title_1}'")
    time = input ("Choose time: ")
    if time == time_m_title_1_a:
        print (f"{time_m_title_1_a}, ticket cost {m_1_ticket_cost_a}")
        cost = m_1_ticket_cost_a
    if time == time_m_title_1_b:
        print (f"{time_m_title_1_b}, ticket cost {m_1_ticket_cost_b}")
        cost = m_1_ticket_cost_b    
    else:
        print ("Not valid")
    amount = int (input ("How many tickets: "))
    total = amount * cost
    print (f"{amount} * {cost} = {total}")

    

if movie_number == "2":
    print (f"You've chosen '{m_title_2}'")
    time = input ("Choose time: ")
    if time == time_m_title_2_a:
        print (f"{time_m_title_2_a}, ticket cost {m_2_ticket_cost_a}")
        cost = m_2_ticket_cost_a
    if time == time_m_title_2_b:
        print (f"{time_m_title_2_b}, ticket cost {m_2_ticket_cost_b}")
        cost = m_2_ticket_cost_b

    
    amount = int (input ("How many tickets: "))
    total = amount * cost
    print (f"{amount} * {cost} = {total}")

if movie_number == "3":
    print (f"You've chosen '{m_title_3}'")
    time = input ("Choose time: ")
    if time == time_m_title_3:
        print (f"{time_m_title_3}, ticket cost {m_3_ticket_cost}")
        cost = m_3_ticket_cost

    amount = int (input ("How many tickets: "))
    total = amount * cost
    print (f"{amount} * {cost} = {total}")