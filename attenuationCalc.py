#attenuation calc
#get inputs for conductivity, permeability, permitivity, frequency,material thickness
import math

sigma = float(input('Enter conductivity (S/m): '))
mu = float(input('Enter permeability (H/m): '))
epsilon = float(input('Enter permitivity (F/m): '))
f = float(input('Enter frequency (Hz): '))
d = float(input('Enter material thickness (m): '))

omega = float(2*(math.pi)*(f))

alphaCalc = float(omega*(math.sqrt((epsilon*mu)/2))*((math.sqrt(1+(sigma/(omega*epsilon))**2))-1)**(1/2))

attdB = 20*(math.log10(math.e))*alphaCalc*d

print(attdB)
