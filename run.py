from people import Passenger
from flight import Flight


from aircraft import *


airplane_list = []
passenger_list = []
flight_list = []
# start empty list of what you want to track:
# airplanes
# passenger - select one and add to flight
# flights - need to list all flights

# initialise 6 passengers (append to list)
passenger1 = passenger_list.append(Passenger('harry'))
passenger2 = passenger_list.append(Passenger('jack'))
passenger3 = passenger_list.append(Passenger('louisa'))
passenger4 = passenger_list.append(Passenger('natalie'))
passenger5 = passenger_list.append(Passenger('henry'))
passenger6 = passenger_list.append(Passenger('simone'))

# initalise 3 planes (append to list)
plane1 = airplane_list.append('plane 1')
plane2 = airplane_list.append('plane 2')
plane3 = airplane_list.append('plane 3')
# create 3 flights (append to list)
flight_tokyo = flight_list.append('tokyo')
flight_arizona = flight_list.append('arizona')
flight_new_york = flight_list.append('new york')

# add 2 passengers to each flight
flight_arizona.add_passenger(passenger1, passenger2)
flight_new_york.add_passenger(passenger3, passenger4)
# list passengers in one flight
for passenger in passenger_list:
    print(passenger_list)

    # save it to a vairbale
    #iterate
    # display passenger