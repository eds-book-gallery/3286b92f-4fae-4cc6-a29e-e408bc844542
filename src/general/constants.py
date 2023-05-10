# Paths
figs_path = '../../outputs/figures/'
data_raw_path = '../../data/raw/'    
data_interm_path = '../../data/interim/' 

# Averages
start=500
skip=14

# Plots raw data: depth, cross-sections, colorbars
time = 2500
point = [2, 8, 6]
level = point[0]
y_coord = point[1]
x_coord = point[2]
lat_arange = [0, 8.36, 15.5, 21.67, 27.25, 32.46, 37.5, 42.54, 47.75, 53.32, 59.5, 66.64, 75.5]
lon_arange = [0, 4.5, 9.5]
diff_min_value = -.001
diff_max_value = .001
lat_label = 'Latitude ('+u'\xb0'+' N)'
lon_label = 'Longitude ('+u'\xb0'+' E)'
depth_label = 'Depth (m)'
cbar_label = 'Temperature ('+u'\xb0'+'C)'
cbar_diff_label = 'Temperature Change ('+u'\xb0'+'C)'
