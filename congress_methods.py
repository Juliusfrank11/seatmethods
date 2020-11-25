import math
import random
import pandas as pd
# globals
#number_of_states = 50
state_populations = [1655000,1335000,665000,345000,53212]
number_of_states = len(state_populations)
#state_populations = [random.randint(100000,1000000) for i in range(number_of_states)] #p_k
total_population = sum(state_populations) # p
total_seats = 100 # h
d = total_population/total_seats

def Jefferson_method(d):
    seats  = list(map(lambda p : math.floor(p/d),state_populations))
    if sum(seats) > total_seats:
        while sum(seats) != total_seats:
            d += 1
            seats  = list(map(lambda p : math.floor(p/d),state_populations))
        return seats
    else:
        while sum(seats) != total_seats:
            d -= 1
            seats  = list(map(lambda p : math.floor(p/d),state_populations))
        return seats
            
def Adam_method(d):
    seats  = list(map(lambda p : math.ceil(p/d),state_populations))
    if sum(seats) > total_seats:
        while sum(seats) != total_seats:
            d += 1
            seats  = list(map(lambda p : math.ceil(p/d),state_populations))
        return seats
    else:
        while sum(seats) != total_seats:
            d -= 1
            seats  = list(map(lambda p : math.ceil(p/d),state_populations))
        return seats

def geometric_rounding(n):
    m = 1 # math.floor(n)
    found = False
    while not found:
        if n >= math.sqrt(m * (m - 1)) and n < math.sqrt(m * (m + 1)):
            found = True
        else:
            m += 1
    return m

def Hill_method(d):
    seats  = list(map(lambda p : geometric_rounding(p/d),state_populations))
    if sum(seats) > total_seats:
        while sum(seats) != total_seats:
            d += 1
            seats  = list(map(lambda p : geometric_rounding(p/d),state_populations))
        return seats
    else:
        while sum(seats) != total_seats:
            d -= 1
            seats  = list(map(lambda p : geometric_rounding(p/d),state_populations))
        return seats

def harmonic_rounding(n):
    m = 1 # math.floor(n)
    found = False
    while not found:
        if n >= (2*m*(m-1))/(2*m - 1) and n < (2*m*(m+1))/(2*m + 1):
            found = True
        else:
            m += 1
    return m

def Dean_method(d):
    seats  = list(map(lambda p : harmonic_rounding(p/d),state_populations))
    if sum(seats) > total_seats:
        while sum(seats) != total_seats:
            d += 1
            seats  = list(map(lambda p : harmonic_rounding(p/d),state_populations))
        return seats
    else:
        while sum(seats) != total_seats:
            d -= 1
            seats  = list(map(lambda p : harmonic_rounding(p/d),state_populations))
        return seats

def Webster_method(d):
    seats  = list(map(lambda p : round(p/d),state_populations))
    if sum(seats) > total_seats:
        while sum(seats) != total_seats:
            d += 1
            seats  = list(map(lambda p : round(p/d),state_populations))
        return seats
    else:
        while sum(seats) != total_seats:
            d -= 1
            seats  = list(map(lambda p : round(p/d),state_populations))
        return seats
    
jeff = Jefferson_method(d)
adam = Adam_method(d)
web = Webster_method(d)
dean = Dean_method(d)
hill = Hill_method(d)
state_names = ["State " + str(i+1) for i in range(number_of_states)]
precentage_of_populations = list(map(lambda p : round(p/total_population * 100,2),state_populations))
dic = {"Name" : state_names, "Population": state_populations, "Precentage of Popluation": precentage_of_populations, "Seats under Jefferson": jeff, "Seats under Adam": adam, "Seats under Webster": web, "Seats under Dean": dean,"Seats under Hill": hill}
df = pd.DataFrame(data=dic)
    