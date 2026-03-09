%attenuation calc
%get inputs for conductivity, permeability, permitivity, frequency,material thickness

sigma = input('Enter conductivity (S/m): ');
mu = input('Enter permeability (H/m): ');
epsilon = input('Enter permitivity (F/m): ');
f = input('Enter frequency (Hz): ');
d = input('Enter material thickness (m): ');

omega = 2*pi*f;

alphaCalc = omega*sqrt((epsilon*mu)/2)*(sqrt(1+(sigma/(omega*epsilon))^2)-1)^(1/2);

attdB = 20*log10(exp(1))*alphaCalc*d

