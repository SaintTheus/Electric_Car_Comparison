from math import *
import matplotlib.pyplot as plt
import copy
import numpy as np


# all the lists I need

list = []


time = []
x = []
y = []
inclination = []
speed = []


dragforce_tesla_atv = []
dragforce_devolopment_atv = []


tangentialweight_tesla = []
tangentialweight_development = []

total_force_developflat = []
total_force_develop_notflat = []
total_force_tesla_notflat = []


power_development_flat = []
power_development_notflat = []
power_tesla_notflat = []


# all constants

density = 1.225  # kg/m^3

mass_tesla = 1847.3  # kg
weight_tesla = (mass_tesla) * (9.8)
Area_tesla = 2.668  # m^2
dragcoef_tesla = .230

mass_devolopment = 1901.1  # kg
weight_development = (mass_devolopment) * (9.8)
Area_devolopment = 2.843  # m^2
dragcoef_devolopment = .239


# Reads file and appends list - Removes first element that not needed


def readfile():
    datafile = open("simulated_lap.txt", 'r')
    for data in datafile:
        list.append(data.rstrip().split('&'))
    list.pop(0)
    datafile.close()


######################################################################### Extracting from list ################################################################################

# Extracts time from list and appends a list called time


def extract_time():

    for i in range(len(list)):
        time.append(list[i][0])
    for i in range(len(time)):
        time[i] = float(time[i])

# Extracts x from list and appends a list called x


def extract_x():

    for i in range(len(list)):
        x.append(list[i][1])
    for i in range(len(x)):
        x[i] = float(x[i])


# Extracts y from list and appends a list called y


def extract_y():

    for i in range(len(list)):
        y.append(list[i][2])
    for i in range(len(y)):
        y[i] = float(y[i])


# Extracts inclination from list and appends a list called inclination


def extract_inclination():

    for i in range(len(list)):
        inclination.append(list[i][3])
    for i in range(len(inclination)):
        inclination[i] = float(inclination[i])
        inclination[i] = (inclination[i] * 0.0174533)  # degrees --> radians


# Extracts speed from list and appends a list called speed


def extract_speed():

    for i in range(len(list)):
        speed.append(list[i][4])
    for i in range(len(speed)):
        speed[i] = float(speed[i])
        speed[i] = (speed[i] * (1609.34 / 3600))  # mph --> meters/sec

# ------------------------------------------------------------------------------------- EndExtracting from list -----------------------------------------------------------------------------------------------


# Calculates drag force


def dragforce_calc(p, A, Cd, which):
    ''' This function is responsible for calculating the dragforce for each of the cars with there specific arguments '''

    for i in range(len(speed)):
        dragforce = (.5) * (p) * (A) * (Cd) * (speed[i])
        which.append(dragforce)

 ######################################################################### Development Flat ################################################################################


# This function calculates power for the development car on a flat track

def Power_calc_develop_flat():

    for i in range(len(dragforce_devolopment_atv)):
        total_force_developflat.append(
            dragforce_devolopment_atv[i] + weight_development)

    for i in range(len(dragforce_devolopment_atv)):
        power_development_flat.append(
            (total_force_developflat[i] * speed[i])/(735.5))


######################################################################### Development Not Flat ################################################################################

def Power_calc_develop_notflat():
    for i in range(len(speed)):
        total_force_develop_notflat.append(
            dragforce_devolopment_atv[i] * (weight_development * sin(inclination[i])))

    for i in range(len(speed)):
        power_development_notflat.append(
            (total_force_develop_notflat[i] * speed[i]) / (735.5))


######################################################################### Tesla Not Flat ################################################################################

def Power_calc_tesla_notflat():
    for i in range(len(speed)):
        total_force_tesla_notflat.append(
            dragforce_tesla_atv[i] * (weight_development * sin(inclination[i])))

    for i in range(len(speed)):
        power_tesla_notflat.append(
            (total_force_tesla_notflat[i] * speed[i])/(735.5))

# ######################################################################### Finding Max Power for each of the three scenarios ################################################################################


# print("The max power for the development car on a flat track is:",
#       max(power_development_flat))


def main():
    # Read file
    readfile()
    # Read file end

    # Setting up arrays
    extract_time()
    extract_x()
    extract_y()
    extract_inclination()
    extract_speed()
    # Setting up arrays end

    # Calculating drag force for both cars
    dragforce_calc(density, Area_devolopment,
                   dragcoef_devolopment, dragforce_devolopment_atv)
    dragforce_calc(density, Area_tesla, dragcoef_tesla, dragforce_tesla_atv)
    # Calculating drag force for both cars end

    # Calling power functions
    Power_calc_develop_flat()
    Power_calc_develop_notflat()
    Power_calc_tesla_notflat()

    # Calling power functions end


main()

######################################################################## Finding Max Power for each of the three scenarios ################################################################################

# Table for three scenarios
print("\t\t| Development car(Flat Track)\t| Development car(Real track)\t| Tesla (Real track)\t|")
print("Max Power\t|", floor(max(power_development_flat)), "\t\t\t\t|", floor(max(
    power_development_notflat)), "\t\t\t\t|\t", floor(max(power_tesla_notflat)), "\t\t|")
print("(x,y)\t\t|", "(", floor(x[13]), floor(y[13]), ")\t\t\t|",
      "(", floor(x[99]), floor(y[99]), ")\t\t\t|", "(", floor(
          x[99]), floor(y[99]), ")\t\t|")


# # max power for development flat
# print("The max power for the development car on a flat track is:",
#       max(power_development_flat))

# print("This max power for a development car on a flat track occurs at x =",
#       x[13], "and y =", y[13])


# print("#" * 100)

# # max power development not flat
# print("The max power for the development car on a track that is not flat is:",
#       max(power_development_notflat))

# print("This max power for a development car that not on a flat track occurs at x =",
#       x[99], "and y =", y[99])

# print("#" * 100)

# # max power tesla not flat
# print("The max power for the development car on a track that is not flat is:",
#       max(power_tesla_notflat))

# print("This max power for a tesla car that not on a flat track occurs at x =",
#       x[99], "and y =", y[99])

# print("#" * 100)


######################################################################### Plotting the track ################################################################################
plt.plot(x, y, "b-")
plt.plot(x[13], y[13], marker="o", label='Development(Flat Track)')
plt.plot(x[99], y[99], marker="D", label='Development(Real Track)')
plt.plot(x[99], y[99], marker="X", label='Tesla(Real Track)')
plt.plot(x[0], y[0], marker="8", label='Start/Finish Line')

plt.legend()
plt.title("Locations of Maxiumum Power Required")
plt.xlabel("Distance East [ft]")
plt.ylabel("Distance North [ft]")

plt.show()


######################################################################### Realistic track positive power values ################################################################################


# print(power_development_notflat)
# print(power_tesla_notflat)
positivepower_development = []
positivepower_tesla = []
positivepower_time = []
positivepower_time = copy.deepcopy(time)

for i in range(len(power_development_notflat)):
    if power_development_notflat[i] > 0:
        positivepower_development.append(power_development_notflat[i])
    elif power_development_notflat[i] <= 0:
        positivepower_development.append(0)

for i in range(len(power_development_notflat)):
    if power_tesla_notflat[i] > 0:
        positivepower_tesla.append(power_tesla_notflat[i])
    elif power_tesla_notflat[i] <= 0:
        positivepower_tesla.append(0)


# used this to see what indices I had to pop
# indices_needtobepopped = [
#     i for i, x in enumerate(positivepower_tesla) if x == 0]

# Used stack overflow to figure out how to properly configure this data to get it to where I can graph it
positivepower_time_index = [
    i for (i, x) in enumerate(positivepower_tesla) if x > 0]
positivepower_time = [x for (i, x) in enumerate(
    positivepower_time) if i in positivepower_time_index]

positivepower_tesla = [x for x in positivepower_tesla if x > 0]
positivepower_development = [x for x in positivepower_development if x > 0]

xtime = [5, 11, 19, 20, 40, 70, 75]
positivepower_time_sub = [x for i, x in enumerate(
    positivepower_time) if i in xtime]
positivepower_development_sub = [x for i, x in enumerate(
    positivepower_development) if i in xtime]
positivepower_tesla_sub = [x for i, x in enumerate(
    positivepower_tesla) if i in xtime]


######################################################################### plotting bar graph with power comparison ################################################################################

x = np.arange(len(positivepower_time_sub))
fig, ax = plt.subplots()
rects1 = ax.bar(x - .35/2, positivepower_development_sub, .35,
                label='Development')
rects2 = ax.bar(x + .35/2, positivepower_tesla_sub, .35, label='Tesla')
plt.xlabel("Time [s]")
plt.ylabel("Power Required[hp]")
plt.title("Max power comparison at 8 different times on the track")
plt.legend(loc='upper center')
plt.xticks(np.arange(len(xtime)), [
           floor(positivepower_time[x]) for x in xtime])
plt.show()

######################################################################### Calculating how many kgs we have to reduce ################################################################################

part1 = (2778.595 * .99)/51.06
part2 = part1 - 21.25
part3 = part2 / (9.8 * .0019547675)

kgtoreducefromdevelopment = 1901.1 - part3

print("For the development car to properly compete with the tesla model S we will need to reduce the mass by:",
      kgtoreducefromdevelopment, "kg")

######################################################################### Determining power of development car after a reduction in mass ################################################################################
Newtotal_force_develop_notflat = []
Newpower_development_notflat = []
New_weight = part3 * 9.8


def NewPower_calc_develop_notflat():
    for i in range(len(speed)):
        Newtotal_force_develop_notflat.append(
            dragforce_devolopment_atv[i] * (New_weight * sin(inclination[i])))

    for i in range(len(speed)):
        Newpower_development_notflat.append(
            (Newtotal_force_develop_notflat[i] * speed[i]) / (735.5))


NewPower_calc_develop_notflat()

######################################################################### New bar graph comparing New power to old power of development ################################################################################

xNd = [Newpower_development_notflat[99]]
xOd = [power_development_notflat[99]]

plt.bar(time[99], xOd, color="red", label='Development car at old mass')
plt.bar(time[99], xNd, color="blue", label='Development car at new mass')
plt.xlabel("Approximately the time the max power occured")
plt.legend(loc="lower right")
plt.ylabel("Max power on the track")
plt.title("Comparison of max power after changing the mass of the car")
plt.show()

######################################################################### Writing (original mass development car) to a csv ################################################################################
# Things to write:
# List index number
# Speed(in meters per second)
# Drag Force in Newtons
# Power required on flat track[hp]
# Power required in realistic track[hp]


# Opening a file
file1 = open('mecatti_matheus_MyCar.csv', 'w')

# Writing a string to file
#dregforce_development_atv, power_development_flat, power_development_notflat
file1.write(
    "index,speed, drag force[N],power required on flat track[hp],power required in realistic track[hp]\n")
for i in range(len(power_development_flat)):
    file1.write(str(i)+',' + str(speed[i]) + ',' + str(dragforce_devolopment_atv[i]) + ',' + str(
        power_development_flat[i]) + ',' + str(power_development_notflat[i]) + '\n')

file1.close()
