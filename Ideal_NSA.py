import math
from math import floor, ceil
import NSA_functions
from decimal import Decimal, ROUND_HALF_UP

def NSA_round(number, digits=1):
    factor = 10 ** digits
    shifted = number * factor
    if shifted > 0:
        rounded = floor(shifted + 0.5)
    else:
        rounded = ceil(shifted - 0.5)

    return rounded / factor


def round_half_up(n, decimals=1):
    multiplier = 10**decimals
    return floor(n * multiplier + 0.5) / multiplier

def calc_wavelength(frequency):
    #return 299.702547 / frequency
    return 299.792458 / frequency

def calc_B(frequency):
    return (2*math.pi)/calc_wavelength(frequency)

def calc_d1(l_h1, l_h2, l_R):
    return math.sqrt(l_R ** 2 + (l_h1 - l_h2) ** 2)

def calc_d2(l_h1, l_h2, l_R):
    return math.sqrt(l_R ** 2 + (l_h1 + l_h2) ** 2)

def calc_ev(R, d1, d2, frequency):
    step_1 = (R**2) * math.sqrt(49.2)
    step_2 = math.sqrt(d1**6 + d2**6 + 2*d1**3*d2**3*math.cos((calc_B(frequency) * (d2 - d1))))
    ev = 20*math.log(step_1 * step_2 / (d1**3*d2**3), 10)
    return ev

def calc_eh(R, d1, d2, frequency):
    step_1 = math.sqrt(49.2)
    step_2 = math.sqrt(d1**2 + d2**2 - 2*d1*d2*math.cos((calc_B(frequency) * (d2 - d1))))
    eh = 20*math.log(step_1 * step_2 / (d1*d2), 10)
    return eh

def create_h2():
    # Rx height above GRP h2 1m to 4m
    h2 = []
    i = 1
    count = 0
    while i <= 4:
        h2.append(i)
        i += 0.01
        i = round(i, 3)
    return h2

def an_ideal(R, h1, frequency, polarity):
    # Calculate Edvmax or Edhmax at frequency
    e_max = -999999
    h2 = create_h2() #Rx height above GRP swept 1-4m step 0.001m
    for h_2 in h2:
        # calc d1 and d2
        d1 = calc_d1(h1, h_2, R)
        d2 = calc_d2(h1, h_2, R)
        if polarity == 'V':
            e = calc_ev(R, d1, d2, frequency)
        else:
            e = calc_eh(R, d1, d2, frequency)
        if e > e_max:
            e_max = e
            d1_max = d1
            d2_max = d2
            h2_max = h_2

    #NSA = NSA_round((48.92 - (20 * math.log(frequency, 10)) - e_max), 2)
    NSA = NSA_round((20*math.log10(279.1) - (20 * math.log10(frequency)) - e_max), 3)
    return NSA

if __name__ == "__main__":

    R = 3 # Measurement Distance
    h1 = 1 # Tx height above GRP
    ant_pol = 'H' # Antenna polarity H or V
    write_data = True
    start_freq = 30
    stop_freq = 200
    step_size = 2

    # Create frequency list in MHz
    freq_list = NSA_functions.build_freq_list(start_freq,stop_freq,step_size)


    #Create An_ideal
    An_ideal = []

    # Calculate Edvmax or Edhmax at frequency
    for x in freq_list:
        An_ideal.append(an_ideal(R, h1, x, ant_pol))

    for i in range(len(freq_list)):
        print(str(freq_list[i]) + ', ' + str(An_ideal[i]))

    if write_data==True:
        """
        if swept:
            sweep_type = 'Swept'
        else:
            sweep_type = 'Discrete'
        """
        An_file_name = str(start_freq) + '-' + str(stop_freq) + ' Pol ' + ant_pol + ' Dis ' + str(R) + 'm Tx ' + str(h1) + 'm.txt'
        print(An_file_name)
        f = open(An_file_name, 'w')
        write_string = 'R = ' + str(R) + 'm\nh1 = ' + str(h1) + 'm\npolarity = ' + ant_pol + '\n'
        f.write(write_string)
        write_string = 'Freq (MHz), An (dB)'
        for i in range(len(freq_list)):
            f.write(str(freq_list[i]) + ', ' + str(An_ideal[i]) + '\n')
        f.close()