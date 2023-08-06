area = int(input("Enter the Area of the building (in square meters): "))

num_of_occupants = int(input("Enter the number of occupants: "))

type_of_building = input("Enter the type of building (residential, commercial, etc): ")

t_outdoor = int(input("Enter the outdoor temperature (in Celsius) "))

t_indoor = int(input("Enter the desired indoor temperature (in Celsius) "))

if type_of_building == 'residential':
    cooling_load = 100*num_of_occupants
elif type_of_building == 'commercial':
    cooling_load = 150*num_of_occupants
    
T_diff = t_outdoor-t_indoor
    
q_conduction = 30*area*T_diff

sensible_cooling_load = q_conduction + cooling_load

print("The sensible cooling load is: ", sensible_cooling_load, "Watts")