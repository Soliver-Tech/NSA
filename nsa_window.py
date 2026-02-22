import tkinter as tk
from tkinter import ttk

# nsa window
window = tk.Tk()
window.title('NSA Window')
window.geometry('1400x800')

# tab_control = ttk.Notebook(window, style='lefttab.TNotebook')
tab_control = ttk.Notebook(window)
print(tab_control.winfo_class())

analyzer_tab = ttk.Frame(tab_control)
site_tab = ttk.Frame(tab_control)
run_test = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)

tab_control.add(site_tab, text='Site Information')
tab_control.add(analyzer_tab, text='Analyzer Settings')
tab_control.add(run_test, text='Run Test')
tab_control.add(tab4, text='Communications')

tab_control.pack(expand=1, fill='both')

# Frequency Frame
freq_frame = ttk.Frame(analyzer_tab, relief = 'sunken')
freq_frame.columnconfigure(0, weight = 1)
freq_frame.columnconfigure(1, weight = 1)
freq_frame.pack(pady = 5, ipady = 3)

# Bandwidth Frame
bw_frame = ttk.Frame(analyzer_tab, relief = 'sunken')
bw_frame.columnconfigure(0, weight = 1)
bw_frame.columnconfigure(1, weight = 1)
bw_frame.pack(pady = 5, ipady = 3)

# Data Points Frame
dp_frame = ttk.Frame(analyzer_tab, relief = 'sunken')
dp_frame.columnconfigure(0, weight = 1)
dp_frame.columnconfigure(1, weight = 1)
dp_frame.pack(pady = 5, ipady = 3)

# Amplitude Frame
amp_frame = ttk.Frame(analyzer_tab, relief = 'sunken')
amp_frame.columnconfigure(0, weight = 1)
amp_frame.columnconfigure(1, weight = 1)
amp_frame.pack(pady = 5, ipady = 3)

# Site Name Frame
customer_frame = ttk.Frame(site_tab, relief = 'sunken')
customer_frame.columnconfigure(0, weight = 1)
customer_frame.columnconfigure(1, weight = 1)
customer_frame.pack(pady = 5, ipady = 3)

# Run Test Tab Frames
run_info_frame = ttk.Frame(run_test, relief = 'sunken')
run_info_frame.columnconfigure(0, weight = 1)
run_info_frame.columnconfigure(1, weight = 4)
run_info_frame.pack()

# Site Geometery Frame
site_geo_frame = ttk.Frame(run_info_frame, relief = 'sunken')
site_geo_frame.columnconfigure(0, weight = 1)
site_geo_frame.columnconfigure(1, weight = 1)
site_geo_frame.grid(column = 0, row = 0)

# Antenna Frame
antenna_frame = ttk.Frame(run_info_frame, relief = 'sunken')
antenna_frame.grid(column = 0, row = 1)

# Position Frame
pos_frame = ttk.Frame(run_info_frame, relief= 'sunken')
pos_frame.grid(column = 0, row = 2, padx = 6, pady = 6)

line_num = 0
font_size = '14'
font_normal = 'Calibri ' + font_size
font_bold = 'Calibri ' + font_size + ' bold'

# start frequency field
frequency_label = ttk.Label(freq_frame, text = "Frequency (MHz)", font = font_bold)
frequency_label.grid(column = 0, row = 0, columnspan = 5, pady = 5)

start_frequency_label = ttk.Label(freq_frame, text ='Start', font = font_bold)
start_frequency_label.grid(column = 0, row = 1, padx = 5)

start_frequency_dbl = tk.DoubleVar
start_frequency_entry = ttk.Entry(freq_frame, justify ='center', font = font_normal, textvariable = start_frequency_dbl)
start_frequency_entry.insert(0, '80')
start_frequency_entry.grid(column = 0, row = 2, padx = 5, pady = 2)

# stop frequency field
stop_frequency_label = ttk.Label(freq_frame, text = 'Stop', font = font_bold)
stop_frequency_label.grid(column = 1, row = 1, padx = 5)

stop_frequency_dbl = tk.DoubleVar
stop_frequency_entry = ttk.Entry(freq_frame, justify = 'center', font = font_normal, textvariable = stop_frequency_dbl)
stop_frequency_entry.insert(0,'200')
stop_frequency_entry.grid(column = 1, row = 2, padx = 5, pady = 2)

# Bandwidth Label
bandwidth_label = ttk.Label(bw_frame, text = "Bandwidth (Hz)", font = font_bold)
bandwidth_label.grid(column = 0, row = 0, columnspan = 2, padx=5, pady = 5)

# Resolution BW in Hz
rbw_label = ttk.Label(bw_frame, text = 'Resolution', justify = 'center', font = font_bold)
rbw_label.grid(column = 0, row = 1, padx = 5, pady= 5)

rbw_int = tk.IntVar
rbw_entry = ttk.Entry(bw_frame, font = font_normal, justify = 'center', textvariable = rbw_int)
rbw_entry.insert(0,'10,000')
rbw_entry.grid(column = 0, row = 2, padx = 5, pady = 1)

# Video BW in Hz
vbw_label = ttk.Label(bw_frame, text = 'Video', justify = 'center', font = font_bold)
vbw_label.grid(column = 1, row = 1, padx = 5, pady = 5)

vbw_int = tk.IntVar
vbw_entry = ttk.Entry(bw_frame, font = font_normal, justify = 'center', textvariable = vbw_int)
vbw_entry.insert(0,'10,000')
vbw_entry.grid(column = 1, row = 2, padx = 5, pady = 1)

# number of data points
data_points_label = ttk.Label(dp_frame, text = 'Analyzer Data Points', font = font_bold )
data_points_label.grid(column = 0, row = 0, padx = 5, pady = 5)

data_points_int = tk.IntVar # entry_int = tk.IntVar()
data_points_entry = ttk.Entry(dp_frame, justify = 'center', font = font_normal, textvariable = data_points_int)
data_points_entry.insert(0,'201')
data_points_entry.grid(column = 0, row = 1, sticky ='sw', padx = 5, pady = 1)

# number of ranges
ranges_label = ttk.Label(dp_frame, text = 'Number of Ranges', font = font_bold )
ranges_label.grid(column = 1, row = 0, padx = 5, pady = 5)

ranges_int = tk.IntVar # entry_int = tk.IntVar()
ranges_entry = ttk.Entry(dp_frame, justify = 'center', font = font_normal, textvariable = data_points_int)
ranges_entry.insert(0,'2')
ranges_entry.grid(column = 1, row = 1, sticky ='sw', padx = 5, pady = 1)

# Drive Level in dBm
drive_label = ttk.Label(amp_frame, text = 'Drive Level (dBm)', font = font_bold)
drive_label.grid(column = 0, row = 0, padx = 5, pady = 5)

drive_int = tk.IntVar
drive_entry = ttk.Entry(amp_frame, justify = 'center', font = font_normal, textvariable = drive_int)
drive_entry.insert(0,'-10')
drive_entry.grid(column = 0, row = 1, padx = 5, pady = 2)

# Reference Level in dBm
reference_level_label = ttk.Label(amp_frame, text = 'Reference Level (dBm)', font = font_bold)
reference_level_label.grid(column = 1, row = 0, padx = 5, pady = 5)

reference_level_int = tk.IntVar
reference_level_entry = ttk.Entry(amp_frame, justify = 'center', font = font_normal, textvariable = reference_level_int)
reference_level_entry.insert(0,'10')
reference_level_entry.grid(column = 1, row = 1, padx = 5, pady = 2)

# Attenuation in dB
attenuation_label = ttk.Label(amp_frame, text = 'Attenuation (dB)', font = font_bold)
attenuation_label.grid(column = 2, row = 0, padx = 5, pady = 5)

attenuation_int = tk.IntVar
attenuation_entry = ttk.Entry(amp_frame, justify = 'center', font = font_normal, textvariable = attenuation_int)
attenuation_entry.insert(0,'10')
attenuation_entry.grid(column = 2, row = 1, padx = 5, pady = 2)

# Site Name
site_name_label = ttk.Label(customer_frame, text ='Site', font = font_bold)
site_name_label.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = 'e')

site_name_str = tk.StringVar
site_name_entry = ttk.Entry(customer_frame, justify ='left', font = font_normal, textvariable = site_name_str, width = 40)
site_name_entry.insert(0,'Site Name')
site_name_entry.grid(column = 1, row = 0, padx = 5, pady = 2)

# Company Name
co_name_label = ttk.Label(customer_frame, text ='Company', font = font_bold)
co_name_label.grid(column = 0, row = 1, padx = 5, pady = 5, sticky = 'e')

co_name_str = tk.StringVar
co_name_entry = ttk.Entry(customer_frame, justify ='left', font = font_normal, textvariable = co_name_str, width = 40)
co_name_entry.insert(0,'Company Name')
co_name_entry.grid(column = 1, row = 1, padx = 5, pady = 2)

# Company Street 1
street1_name_label = ttk.Label(customer_frame, text ='Street 1', font = font_bold)
street1_name_label.grid(column = 0, row = 2, padx = 5, pady = 5, sticky = 'e')

street1_str = tk.StringVar
street1_entry = ttk.Entry(customer_frame, justify ='left', font = font_normal, textvariable = street1_str, width = 40)
street1_entry.insert(0,'Street 1')
street1_entry.grid(column = 1, row = 2, padx = 5, pady = 2)

# Company Street 1
street2_name_label = ttk.Label(customer_frame, text ='Street 2', font = font_bold)
street2_name_label.grid(column = 0, row = 3, padx = 5, pady = 5, sticky = 'e')

street2_str = tk.StringVar
street2_entry = ttk.Entry(customer_frame, justify ='left', font = font_normal, textvariable = street2_str, width = 40)
street2_entry.insert(0,'Street 2')
street2_entry.grid(column = 1, row = 3, padx = 2, pady = 2, )

# Company City
city_label = ttk.Label(customer_frame, text ='City', font = font_bold)
city_label.grid(column = 0, row = 4, padx = 5, pady = 5, sticky = 'e')

city_str = tk.StringVar
city_entry = ttk.Entry(customer_frame, justify ='left', font = font_normal, textvariable = city_str, width = 40)
city_entry.insert(0,'City')
city_entry.grid(column = 1, row = 4, padx = 2, pady = 2, )

# Company State
state_label = ttk.Label(customer_frame, text ='State', font = font_bold)
state_label.grid(column = 0, row = 5, padx = 5, pady = 5, sticky = 'e')

state_str = tk.StringVar
state_entry = ttk.Entry(customer_frame, justify ='left', font = font_normal, textvariable = state_str, width = 40)
state_entry.insert(0,'State')
state_entry.grid(column = 1, row = 5, padx = 2, pady = 2, )

# Company Zip
zip_label = ttk.Label(customer_frame, text ='Zip', font = font_bold)
zip_label.grid(column = 0, row = 6, padx = 5, pady = 5, sticky = 'e')

zip_str = tk.StringVar
zip_entry = ttk.Entry(customer_frame, justify ='left', font = font_normal, textvariable = zip_str, width = 40)
zip_entry.insert(0,'Zip')
zip_entry.grid(column = 1, row = 6, padx = 2, pady = 2, )

# Range Length
range_length_label = ttk.Label(site_geo_frame, text = 'Range Length (m)', font = font_bold)
range_length_label.grid(column = 0, row = 0, padx = 5, pady = 5)

range_length_int = tk.IntVar
range_length_entry = ttk.Entry(site_geo_frame, justify = 'center', font = font_normal, textvariable = range_length_int)
range_length_entry.insert(0,'3')
range_length_entry.grid(column = 0, row = 1, padx = 2, pady = 2)

# Volume Diameter
volume_diameter_label = ttk.Label(site_geo_frame, text = 'Volume Diameter (m)', font = font_bold)
volume_diameter_label.grid(column = 0, row = 2, padx = 5, pady = 2)

volume_diameter_int = tk.IntVar
volume_diameter_entry = ttk.Entry(site_geo_frame, justify = 'center', font = font_normal, textvariable = volume_diameter_int)
volume_diameter_entry.insert(0,'2')
volume_diameter_entry.grid(column = 0, row = 3, padx = 2, pady = 2)

# Measurement Axis Angle
axis_angle_label = ttk.Label(site_geo_frame, text = 'Axis Angle (deg)', font = font_bold)
axis_angle_label.grid(column = 0, row = 4, padx = 5, pady = 2)

axis_angle_int = tk.IntVar
axis_angle_entry = ttk.Entry(site_geo_frame, justify = 'center', font = font_normal, textvariable = axis_angle_int)
axis_angle_entry.insert(0,'0')
axis_angle_entry.grid(column = 0, row = 5, padx = 2, pady = 2)

# Tx Antenna Height
tx_height_label = ttk.Label(antenna_frame, text = 'Tx Ant Height (m)', font = font_bold)
tx_height_label.grid(column = 0, row = 0, padx = 5, pady = 5)

tx_height_int = tk.IntVar
tx_height_entry = ttk.Entry(antenna_frame, justify = 'center', font = font_normal, textvariable = tx_height_int)
tx_height_entry.insert(0,'1')
tx_height_entry.grid(column = 0, row = 1, padx = 2, pady = 2)

# Rx Antenna Minimum Height
rx_min_height_label = ttk.Label(antenna_frame, text = 'Rx Ant Min Height (m)', font = font_bold)
rx_min_height_label.grid(column = 0, row = 2, padx = 5, pady = 5)

rx_min_height_int = tk.IntVar
rx_min_height_entry = ttk.Entry(antenna_frame, justify = 'center', font = font_normal, textvariable = rx_min_height_int)
rx_min_height_entry.insert(0,'1')
rx_min_height_entry.grid(column = 0, row = 3, padx = 2, pady = 2)

# Rx Antenna Maximum Height
rx_max_height_label = ttk.Label(antenna_frame, text = 'Rx Ant Max Height (m)', font = font_bold)
rx_max_height_label.grid(column = 0, row = 4, padx = 5, pady = 5)

rx_max_height_int = tk.IntVar
rx_max_height_entry = ttk.Entry(antenna_frame, justify = 'center', font = font_normal, textvariable = rx_max_height_int)
rx_max_height_entry.insert(0,'4')
rx_max_height_entry.grid(column = 0, row = 5, padx = 2, pady = 2)

# Antenna Polarity
ant_polarity_label = ttk.Label(antenna_frame, text = 'Polarity', font = font_bold)
ant_polarity_label.grid(column = 0, row = 6, padx = 5, pady = 5)

polarity = tk.StringVar(antenna_frame, "1")
check_vertical = tk.Radiobutton(antenna_frame, text='Vertical', variable=polarity, value='V')
check_vertical.grid(column = 0, row = 7)
check_vertical.select()

check_horizontal = tk.Radiobutton(antenna_frame, text='Horizontal', variable=polarity, value='H')
check_horizontal.grid(column = 0, row = 8, pady = 5)

# Position Buttons
pos_label = tk.Label(pos_frame, text='Run Position')
pos_label.grid(column = 0, row = 0, padx = 6, pady = 6)

center = ttk.Button(pos_frame, text='Center', width = 8, style= 'Outline.TButton')
center.grid(column = 0, row = 1, padx = 6, pady = 6)

front = ttk.Button(pos_frame, text='Front', width = 8, style='Outline.TButton')
front.grid(column = 0, row = 2, padx = 6, pady = 6)

back = ttk.Button(pos_frame, text='Back', width = 8, style='Outline.TButton')
back.grid(column = 0, row = 3, padx = 6, pady = 6)

right = ttk.Button(pos_frame, text='Right', width = 8, style='Outline.TButton')
right.grid(column = 0, row = 4, padx = 6, pady = 6)

left = ttk.Button(pos_frame, text='Left', width = 8, style='Outline.TButton')
left.grid(column = 0, row = 5, padx = 6, pady = 6)

# Data Graph Place Holder
future_graph = ttk.Label(run_info_frame, text='Future Graph Location', width=125, anchor = tk.CENTER)
future_graph.grid(column = 1, row = 0, padx = 5, rowspan = 2)



# # Margin Above Ideal
# line_num+=2
# margin_above_label = ttk.Label(test_info, text = 'Margin Above Ideal (dB)', font = font_bold)
# margin_above_label.grid(column = 0, row = line_num, sticky = 'e', padx = 5)
#
# margin_above_int = tk.IntVar
# margin_above_entry = ttk.Entry(test_info, justify = 'center', font = font_normal, textvariable = margin_above_int, width = 10)
# margin_above_entry.insert(0,'4')
# margin_above_entry.grid(column = 1, row = line_num, sticky = 'sw', padx = 0)
#
# # Margin Below Ideal
# line_num+=2
# margin_below_label = ttk.Label(test_info, text = 'Margin Below Ideal (dB)', font = font_bold)
# margin_below_label.grid(column = 0, row = line_num, sticky = 'e', padx = 5)
#
# margin_below_int = tk.IntVar
# margin_below_entry = ttk.Entry(test_info, justify = 'center', font = font_normal, textvariable = margin_below_int, width = 10)
# margin_below_entry.insert(0,'4')
# margin_below_entry.grid(column = 1, row = line_num, sticky = 'sw', padx = 0)
#
# # Data Flag Margin
# line_num+=2
# data_flag_label = ttk.Label(test_info, text = 'Flag Data from Margin (dB)', font = font_bold)
# data_flag_label.grid(column = 0, row = line_num, sticky = 'e', padx = 5)
#
# data_flag_int = tk.IntVar
# data_flag_entry = ttk.Entry(test_info, justify = 'center', font = font_normal, textvariable = data_flag_int, width = 10)
# data_flag_entry.insert(0,'1')
# data_flag_entry.grid(column = 1, row = line_num, sticky = 'sw', padx = 0)

#run
window.mainloop()