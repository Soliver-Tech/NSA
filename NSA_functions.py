import time

def location_press(location, range_length, vol_diameter, axis_angle, tx_height, rx_min_height, rx_max_height, ant_polarity):
    print(location, range_length, vol_diameter, axis_angle, tx_height, rx_min_height, rx_max_height, ant_polarity)

    # load antenna factor needs range length, tx height, antenna polarity
    rx_mast_set_pol(ant_polarity)
    rx_mast_set_initial_height(rx_min_height)
    # get and set analyzer settings
    # initiate analyzer max hold
    rx_mast_sweep(rx_max_height)

def rx_mast_set_initial_height(rx_target_height):
    # get rx current height
    print('Setting height to ' + rx_target_height + 'm')

def rx_mast_set_pol(ant_polarity):
    if ant_polarity == 'V':
        print('Antenna set to V')
    else:
        print('Antenna set to H')

def rx_mast_sweep(rx_target_height):
    # get rx current height
    rx_current_height = 10
    for y in range(rx_current_height, (int(rx_target_height)*10)+1, 1):
        print('Height = ' + str(y/10) + 'm')
        time.sleep(0.2)

def build_freq_list(start_freq, stop_freq, step_size):
    freq_list = []
    for x in range(start_freq, stop_freq, step_size):
        freq_list.append(x)
    freq_list.append(stop_freq)
    return freq_list

if __name__ == "__main__":
    print('Building frequency list')
    frequency_list = build_freq_list(200, 1000, 5)
    print(len(frequency_list))
    print(frequency_list)

