# This is the calculation I made to work in PYTHON
#You can copy and paste to test
#The only reason it MIGHT not work is because the lines are too long or trailing whitespace


##################################
### Carbon Emission calculator ###
##################################

#please note that these measurements are in kg and are the average numbers /km
#IT IS IN KM NOT MILES

#Emission factors
PetrolCarEF = 0.175
DieselCarEF = 0.173
ElectricCarEF = 0.035
######
LongHaulPlaneEF = 0.15282
ShortHaulPlaneEF = 0.12576
######                              #note that this is per passenger, the total is alot higher. I also used the factor for a mid range flight. Might change it later on
BussesEF = 0.10151          #This is also /passenger
TrainsEF = 0.0036
CoachesEF = 0.03948
TrolleyBusesEF = 0.0225
TaxisEF = 0.20806
TramsEF = 0.02121
FerriesEF = 0.113
CableCarsEF = 0.03


#Because it is hard to know how far you flew in a plane, I decided to just ask how long they flew and then use the distance = speed * time equation
#I have taken the average speeds of long haul and short haul flights
#IT IS IN KM NOT MILES

LongHaulPlaneAvSpeed = 925
ShortHaulPlaneAvSpeed = 850


#The equation to calculate vehicle emissions is distance * Emission Factor (The Fuel Efficiency is built in) I had to rewrite a bunch of codes and delete variables because I didn't know that ;(


#####
###Attempting to try and recieve an input for number of cars so I can multiply by emission factor###
###I had to do it sepeartely from the while loop because I couldnt figure out how to store the first variable :/ ###

### I have learnt how to use the define function (24/11/26) fancy stuff
### I am now using it so I don't have to repeat questions and its also foolproof hopefully :)
#####

def ask_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
        except ValueError:
            pass
        print("Please enter a valid number"   )

##################################################################################
# Define Function for Cars
##################################################################################

def ask_cartype():
    while True:
        cartype = ask_int("Please enter the number for your car type   "   )
        if cartype in (1, 2, 3):
            return cartype
        print("Please input a valid number   "   )
        print(" Electric = 1, Petrol = 2, Diesel = 3   "   )

def ask_distance_cars():
    while True:
        try:
            value = float(input("\nHow far did you drive today, in km (include time in traffic), you can estimate   "   ))
            if value >= 0:
                return value
        except ValueError:
            pass
        print("Please enter a valid number   "   )

############################################################################################
# Define Function for Public transport
############################################################################################

def ask_pttype():
    while True:
        pttype = ask_int("Please enter the number for your type of public transport   "   )
        if pttype in (1,2,3,4,5,6,7,8):
            return pttype
        print("Please enter a valid number")
        print("Train = 1, Bus = 2, Coaches = 3, Trolley Buses = 4, Taxis = 5, Trams = 6, Ferries = 7, Cable Cars = 8   "   )

def ask_distance_pt():
    while True:
        try:
            value = float(input("\nHow far did you travel today, in km (include time in traffic), you can estimate   "   ))
            if value >= 0:
                return value
        except ValueError:
            pass
        print("Please enter a valid number   "   )

############################################################################################
# Define Function for planes
############################################################################################

def ask_planetype():
    while True:
        ansanswer = ask_int("Please enter the number for your type of plane ride   "   )
        if ansasnwer in (1,2):
            return ansanswer
        print("Please enter a valid number   "   )
        print("Please choose: Long Haul = 1, Short Haul = 2 (Long Haul is more than 3700km or 6-7 hours)   "   )

def ask_plane_distance():
    while True:
        try:
            value = float(input("How long (in hours), you can estimate   "   ))
            if value >= 0:
                return value
            except ValueError:
                pass
            print("Please enter a valid number   ")

############################################################################################
# Car Section
############################################################################################

numcars = ask_int("How many cars have you driven today?(Put 0 if none)   ")
totC02carnocar = 0


if numcars >= 1:
    print(" Electric = 1, Petrol = 2, Diesel = 3   ")
    cartype = ask_cartype()

    if cartype == 1:
        distance = ask_distance_cars()
        C02carnocars = distance * ElectricCarEF
        totC02carnocar = C02carnocars

    elif cartype == 2:
        distance = ask_distance_cars()
        C02carnocars = distance  * PetrolCarEF
        totC02carnocar = C02carnocars

    elif cartype == 3:
        distance = ask_distance_cars()
        C02carnocars = distance  * DieselCarEF
        totC02carnocar = C02carnocars


    numcars = numcars - 1

#############################################################################

#############################################################################

#####
###Loop for number of cars###
#####

    while numcars > 0:
        print(" Electric = 1, Petrol = 2, Diesel = 3   ")
        cartype = ask_cartype()
    
        if cartype == 1:
            distance = ask_distance_cars()
            C02carnocars = distance * ElectricCarEF
            totC02carnocar = C02carnocars + totC02carnocar
    
        elif cartype == 2:
            distance = ask_distance_cars()
            C02carnocars = distance * PetrolCarEF
            totC02carnocar = C02carnocars + totC02carnocar
    
        elif cartype == 3:
            distance = ask_distance_cars()
            C02carnocars = distance * DieselCarEF
            totC02carnocar = C02carnocars + totC02carnocar
      
    
        numcars = numcars - 1

    print("Your Carbon Emissions for your cars are", totC02carnocar, "kgC02e")
else:
    print("Your Carbon Emissions for your cars are 0 kgCO2e")


##########################
### END OF CAR SECTION ###
##########################

#############################################################
# Public Transport Section
#############################################################

ptanswer = ask_int(input("\nDid you go on Public transport today? (Put 0 if you haven't)   "))
totC02pt = 0


if ptanswer >= 1:
    print("Train = 1, Bus = 2, Coaches = 3, Trolley Buses = 4, Taxis = 5, Trams = 6, Ferries = 7, Cable Cars = 8   ")
    typeofpt = ask_pttype()

        #####
        ### I had to type out every single possiblity because I am not that good on Python :/
        #####

    if typeofpt == 1:
        distance = ask_distance_pt()
        C02nopt = distance * TrainsEF
        totC02pt = C02nopt

    elif typeofpt == 2:
        distance = ask_distance_pt()
        C02nopt = distance * BussesEF
        totC02pt = C02nopt

    elif typeofpt == 3:
        distance = ask_distance_pt()
        C02nopt = distance * CoachesEF
        totC02pt = C02nopt

    elif typeofpt == 4:
        distance = ask_distance_pt()
        C02nopt = distance * TrolleyBusesEF
        totC02pt = C02nopt

    elif typeofpt == 5:
        distance = ask_distance_pt()
        C02nopt = distance * TaxisEF
        totC02pt = C02nopt

    elif typeofpt == 6:
        distance = ask_distance_pt()
        C02nopt = distance * TramsEF
        totC02pt = C02nopt

    elif typeofpt == 7:
        distance = ask_distance_pt()
        C02nopt = distance * FerriesEF
        totC02pt = C02nopt

    elif typeofpt == 8:
        distance = ask_distance_pt()
        C02nopt = distance * CableCarsEF
        totC02pt = C02nopt


        typeofpt = typeofpt - 1

########################################################################################

########################################################################################

        while ptanswer > 0:
            print("Train = 1, Bus = 2, Coaches = 3, Trolley Buses = 4, Taxis = 5, Trams = 6, Ferries = 7, Cable Cars = 8   ")
            typeofpt = ask_pttype()
    
            #####
            ### I copy and pasted this part though :)
            #####
    
            if typeofpt == 1:
                distance = ask_distance_pt()
                C02nopt = distance * TrainsEF
                totC02pt = C02nopt + totC02pt
    
            elif typeofpt == 2:
                distance = ask_distance_pt()
                C02nopt = distance * BussesEF
                totC02pt = C02nopt + totC02pt
    
            elif typeofpt == 3:
                distance = ask_distance_pt()
                C02nopt = distance * CoachesEF
                totC02pt = C02nopt + totC02pt
    
            elif typeofpt == 4:
                distance = ask_distance_pt()
                C02nopt = distance * TrolleyBusesEF
                totC02pt = C02nopt + totC02pt
    
            elif typeofpt == 5:
                distance = ask_distance_pt()
                C02nopt = distance * TaxisEF
                totC02pt = C02nopt + totC02pt
    
            elif typeofpt == 6:
                distance = ask_distance_pt()
                C02nopt = distance * TramsEF
                totC02pt = C02nopt + totC02pt
    
            elif typeofpt == 7:
                distance = ask_distance_pt()
                C02nopt = distance * FerriesEF
                totC02pt = C02nopt + totC02pt
    
            elif typeofpt == 8:
                distance = ask_distance_pt()
                C02nopt = distance * CableCarsEF
                totC02pt = C02nopt + totC02pt
    
            ptanswer = ptanswer - 1

    print("Your total Carbon Emissions for your public transport are", totC02pt, "kgCO2e")
else:
    print("Your total Carbon Emissions for your public transport are 0 kgCO2e")

#######################################
### END OF PUBLIC TRANSPORT SECTION ###
#######################################

#####################################################################################
### Plane/Flight Section
#####################################################################################

planeanswer = ask_int(input("\nHow many flights did you go on today? (Put 0 if you haven't)   "   ))
totC02planes = 0


    if numplanes >= 1:
        print("Please choose: Long Haul = 1, Short Haul = 2 (Long Haul is more than 3700km or 6-7 hours)   ")

        if ansanswer == 1:
            flightlength = ask_plane_distance()
            distance = flightlength * LongHaulPlaneAvSpeed
            C02planes = distance * LongHaulPlaneEF
            totC02planes = C02planes


        if ansanswer == 2:
            flightlength = ask_plane_distance()
            distance = flightlength * ShortHaulPlaneAvSpeed
            C02planes = distance * ShortHaulPlaneEF
            totC02planes = C02planes
            
##########################################################################################################

###########################################################################################################

        while numplanes > 0:
            print("Please choose: Long Haul = 1, Short Haul = 2 (Long Haul is more than 3700km or 6-7 hours)   ")
            ansanswer = ask_planetype()
    
    
            if ansanswer == 1:
                flightlength = ask_plane_distance()
                distance = flightlength * LongHaulPlaneAvSpeed
                C02planes = distance * LongHaulPlaneEF
                totC02planes = C02planes + totC02planes
    

            if ansanswer == 2:
                flightlength = ask_plane_distance()
                distance = flightlength * ShortHaulPlaneAvSpeed
                C02planes = distance * ShortHaulPlaneEF
                totC02planes = C02planes + totC02planes
    
            numplanes = numplanes - 1

    print("Your total Carbon Emissions for your plane rides are", totC02planes, "kgCO2e")
else:
    print("Your total Carbon Emissions for your plane rides are 0 kgCO2e")

#############################
#### END OF PLANE SECTION ###
#############################

###############################################################################################
# Start of Final Calculations
###############################################################################################

print("\nIn Conclusion:")
print("Your Carbon Emissions for your cars are", totC02carnocar, "kgCO2e")
print("Your total Carbon Emissions for your public transport are", totC02pt, "kgCO2e")
print("Your total Carbon Emissions for your plane rides are", totC02planes, "kgCO2e")
    
totaltoday = totC02planes + totC02pt + totC02carnocar
print("\nYour total Carbon Emissions today are", totaltoday)

#25/11/26 I think I have finally finished it, if I haven't Ill be here later - Adam
