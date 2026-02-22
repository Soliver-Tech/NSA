import math


def NSA_round(number, decimals=1):
    rounded_abs = round_half_up(abs(number), decimals)
    return math.copysign(rounded_abs,number)


def round_half_up(n, decimals=1):
    multiplier = 10**decimals
    return math.floor(n * multiplier + 0.5) / multiplier


def calc_wavelength(frequency):
    return 299.702547 / frequency


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
        i = round(i, 2)
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
    NSA = (NSA_round((48.92 - (20 * math.log(frequency, 10)) - e_max), 1))

    return NSA


if __name__ == "__main__":
    R = 3 # Measurement Distance
    h1 = 1 # Tx height above GRP
    ant_pol = 'H' # Antenna polarity H or V
    write_data = False

    # Create frequency list in MHz
    freq = []
    swept = True
    if swept:
        step_low = 2
        step_high = 5
    else:
        step_low = 5
        step_high =15
    for x in range(30, 200, step_low):
        freq.append(x)
    for x in range(200, 1000, step_high):
        freq.append(x)
    freq.append(1000)

    #Create An_ideal
    An_ideal = []

    # Calculate Edvmax or Edhmax at frequency
    for x in freq:
        An_ideal.append(an_ideal(R, h1, x, ant_pol))

    for i in range(len(freq)):
        print(str(freq[i]) + ', ' + str(An_ideal[i]))


    if write_data==True:
        if swept:
            sweep_type = 'Swept'
        else:
            sweep_type = 'Discrete'
        An_file_name = sweep_type + ' Pol ' + ant_pol + ' Dis ' + str(R) + 'm Tx ' + str(h1) + 'm'
        print(An_file_name)
        f = open(An_file_name, 'w')
        write_string = 'R = ' + str(R) + 'm\nh1 = ' + str(h1) + 'm\npolarity = ' + ant_pol + '\n'
        f.write(write_string)
        write_string = 'Freq (MHz), An (dB)'
        for i in range(len(freq)):
            f.write(str(freq[i]) + ', ' + str(An_ideal[i]) + '\n')
        f.close()