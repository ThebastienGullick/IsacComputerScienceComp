# This is the calculation I made to work in PYTHON
#You can copy and paste to test



################################
###Carbon Emission calculator###
################################

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
TrolleyBusesEF = 1.25
TaxisEF = 0.20806
TramsEF = 0.02121
FerriesEF = 0.113
CableCarsEF = 0.03


#Fuel Efficiencies
PetrolCarFE = 16
DieselCarFE = 18.5
ElectricCarFE = 6.5 
######                            #for electric cars, it is Km/KWh
LongHaulPlaneFE = 0.033
ShortHaulPlaneFE = 0.0375
######                            #Also /person
BussesFE = 3.75
TrainsFE = 0.305
CoachesFE = 2.75
TrolleyBusesFE = 5.75
TaxisFE = 17
TramsFE = 2.5
FerriesFE = 0.6
CableCarsFE = 0.11

#Because it is hard to know how far you flew in a plane, I decided to just ask how long they flew and then use the distance = speed * time equation
#I have taken the average speeds of long haul and short haul flights
#IT IS IN KM NOT MILES

LongHaulPlaneAvSpeed = 925
ShortHaulPlaneAvSpeed = 850


#The equation to calculate vehicle emissions is distance / Fuel Efficiency * Emission Factor


#####
###Attempting to try and recieve an input for number of cars so I can multiply by emission factor###
###I had to do it sepeartely from the while loop because I couldnt figure out how to store the first variable :/ ###
#####

numcars = int(input("How many cars have you driven today?(Put 0 if none)"))

if numcars < 0:
    print("Try Again")
    numcars = int(input("How many cars have you driven today?(Put 0 if none)"))

if numcars > 0:
    print(" Electric = 1, Petrol = 2, Diesel = 3")
    cartype = int(input("Please enter the number for your car type"))

    if cartype == 1:
        distance = int(input("How far did you drive today, in km(Include time in traffic), you can estimate"))
        C02carnocars = distance / ElectricCarFE * ElectricCarEF
        totC02carnocar = C02carnocars

    elif cartype == 2:
        distance = int(input("How far did you drive today, in km(Include time in traffic), you can estimate"))
        C02carnocars = distance / PetrolCarFE * PetrolCarEF
        totC02carnocar = C02carnocars

    elif cartype == 3:
        distance = int(input("How far did you drive today, in km(Include time in traffic), you can estimate"))
        C02carnocars = distance / DieselCarFE * DieselCarEF
        totC02carnocar = C02carnocars

    else:
        print("Please input a valid number")
        print(" Electric = 1, Petrol = 2, Diesel = 3")
        cartype = int(input("Please enter the number for your car type"))

    numcars = numcars - 1

#############################################################################

#############################################################################

#####
###Loop for number of cars###
#####

while numcars > 0:
    print(" Electric = 1, Petrol = 2, Diesel = 3")
    cartype = int(input("Please enter the number for your car type"))

    if cartype == 1:
        distance = int(input("How far did you drive today, in km(Include time in traffic), you can estimate"))
        C02carnocars = distance / ElectricCarFE * ElectricCarEF
        totC02carnocar = C02carnocars + totC02carnocar

    elif cartype == 2:
        distance = int(input("How far did you drive today, in km(Include time in traffic), you can estimate"))
        C02carnocars = distance / PetrolCarFE * PetrolCarEF
        totC02carnocar = C02carnocars + totC02carnocar

    elif cartype == 3:
        distance = int(input("How far did you drive today, in km?(Include time in traffic), you can estimate"))
        C02carnocars = distance / DieselCarFE * DieselCarEF
        totC02carnocar = C02carnocars + totC02carnocar

    numcars = numcars - 1

##########################
### END OF CAR SECTION ###
##########################
### Now starting Public Transport Section

_____ = str(input("Did you go on Public transport today? (Yes or No)"))
if _____ == "yes" or _____ == "YES" or _____ == "Yes":
    ___ = int(input("How many types of public transport did you go on today?"))

    if ___ < 0:
        print("Try Again")
        ___ = int(input("How many types of public transport did you go on today?"))


    if ___ == 1:
        print("Train = 1, Bus = 2, Coaches = 3, Trolley Buses = 4, Taxis = 5, Trams = 6, Ferries = 7, Cable Cars = 8")
        typeofpt = int(input("Please choose the number"))

        #####
        ### I had to type out every single possiblity because I am not that good on Python :/
        #####

        if typeofpt == 1:
            distance = int(input("How far did you travel today, in km?, you can estimate"))
            C02nopt = distance / TrainsFE * TrainsEF
            totC02pt = C02nopt

        elif typeofpt == 2:
            distance = int(input("How far did you travel today, in km?, you can estimate"))
            C02nopt = distance / BussesFE * BussesEF
            totC02pt = C02nopt

        elif typeofpt == 3:
            distance = int(input("How far did you travel today, in km?, you can estimate"))
            C02nopt = distance / CoachesFE * CoachesEF
            totC02pt = C02nopt

        elif typeofpt == 4:
            distance = int(input("How far did you travel today, in km?, you can estimate"))
            C02nopt = distance / TrolleyBusesFE * TrolleyBusesEF
            totC02pt = C02nopt

        elif typeofpt == 5:
            distance = int(input("How far did you travel today, in km?, you can estimate"))
            C02nopt = distance / TaxisFE * TaxisEF
            totC02pt = C02nopt

        elif typeofpt == 6:
            distance = int(input("How far did you travel today, in km?, you can estimate"))
            C02nopt = distance / TramsFE * TramsEF
            totC02pt = C02nopt

        elif typeofpt == 7:
            distance = int(input("How far did you travel today, in km?, you can estimate"))
            C02nopt = distance / FerriesFE * FerriesEF
            totC02pt = C02nopt

        elif typeofpt == 8:
            distance = int(input("How far did you travel today, in km?, you can estimate"))
            C02nopt = distance / CableCarsFE * CableCarsEF
            totC02pt = C02nopt


        typeofpt = typeofpt - 1

########################################################################################

########################################################################################

    while ___ > 0:
        print("Train = 1, Bus = 2, Coaches = 3, Trolley Buses = 4, Taxis = 5, Trams = 6, Ferries = 7, Cable Cars = 8")
        typeofpt = int(input("Please choose the number, you will need to choose 1 first, then you can choose others after you have filled in your informtion about a single one"))

        #####
        ### I copy and pasted this part though :)
        #####

        if typeofpt == 1:
            distance = int(input("How far did you travel today, in km?, you can estimate"))
            C02nopt = distance / TrainsFE * TrainsEF
            totC02pt = C02nopt + totC02pt

        elif typeofpt == 2:
            distance = int(input("How far did you travel today, in km?, you can estimate"))
            C02nopt = distance / BussesFE * BussesEF
            totC02pt = C02nopt + totC02pt

        elif typeofpt == 3:
            distance = int(input("How far did you travel today, in km?, you can estimate"))
            C02nopt = distance / CoachesFE * CoachesEF
            totC02pt = C02nopt + totC02pt

        elif typeofpt == 4:
            distance = int(input("How far did you travel today, in km?, you can estimate"))
            C02nopt = distance / TrolleyBusesFE * TrolleyBusesEF
            totC02pt = C02nopt + totC02pt

        elif typeofpt == 5:
            distance = int(input("How far did you travel today, in km?, you can estimate"))
            C02nopt = distance / TaxisFE * TaxisEF
            totC02pt = C02nopt + totC02pt

        elif typeofpt == 6:
            distance = int(input("How far did you travel today, in km?, you can estimate"))
            C02nopt = distance / TramsFE * TramsEF
            totC02pt = C02nopt + totC02pt

        elif typeofpt == 7:
            distance = int(input("How far did you travel today, in km?, you can estimate"))
            C02nopt = distance / FerriesFE * FerriesEF
            totC02pt = C02nopt + totC02pt

        elif typeofpt == 8:
            distance = int(input("How far did you travel today, in km?, you can estimate"))
            C02nopt = distance / CableCarsFE * CableCarsEF
            totC02pt = C02nopt + totC02pt

        typeofpt = typeofpt - 1

#######################################
### END OF PUBLIC TRANSPORT SECTION ###
#######################################
### Start of Plane/Flight Section

answer = int(input("Did you go on a flight today?, Yes = 1 and No = 2"))
if answer == 1:
    ansansanswer = int(input("How many?"))

    if ansansanswer == 1:
        ansanswer = int(input("Please choose: Long Haul = 1, Short Haul = 2 (Long Haul is more than 3700km or 6-7 hours)"))

        if ansanswer < 0 and ansanswer >=3:
            print("Try Again")
            ansanswer = int(input("Please choose: Long Haul = 1, Short Haul = 2 (Long Haul is more than 3700km or 6-7 hours)"))

        if ansanswer == 1:
            flightlength = int(input("How long (in hours), you can estimate"))
            lengthoflightsecs = flightlength * 3600
            distance = lengthoflightsecs * LongHaulPlaneAvSpeed
            C02planes = distance / LongHaulPlaneFE * LongHaulPlaneEF
            totC02planes = C02planes
        if ansanswer == 2:
            lengthoflightsecs = flightlength * 3600
            distance = lengthoflightsecs * ShortHaulPlaneAvSpeed
            C02planes = distance / ShortHaulPlaneFE * ShortHaulPlaneEF
            totC02planes = C02planes

    while answer > 0:
        ansanswer = int(input("Please choose: Long Haul = 1, Short Haul = 2 (Long Haul is more than 3700km or 6-7 hours)"))

        if ansanswer < 0 and ansanswer >=3:
            print("Try Again")
            ansanswer = int(input("Please choose: Long Haul = 1, Short Haul = 2 (Long Haul is more than 3700km or 6-7 hours)"))

        if ansanswer == 1:
            flightlength = int(input("How long (in hours), you can estimate"))
            lengthoflightsecs = flightlength * 3600
            distance = lengthoflightsecs * LongHaulPlaneAvSpeed
            C02planes = distance / LongHaulPlaneFE * LongHaulPlaneEF
            totC02planes = C02planes + totC02planes

        if ansanswer == 2:
            lengthoflightsecs = flightlength * 3600
            distance = lengthoflightsecs * ShortHaulPlaneAvSpeed
            C02planes = distance / ShortHaulPlaneFE * ShortHaulPlaneEF
            totC02planes = C02planes + totC02planes

        ansanswer = ansanswer - 1

print("Your Carbon Emissions for your cars are", totC02carnocar, "kgCO2e")
print("Your total Carbon Emissions for your public transport are", totC02pt, "kgCO2e")
print("Your total Carbon Emissions for your plane rides are", totC02planes, "kgCO2e")
