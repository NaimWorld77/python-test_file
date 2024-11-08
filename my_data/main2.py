import netCDF4 as nc  # Import the netCDF4 library to handle netCDF files
import numpy as np  # Import NumPy for numerical operations
import matplotlib.pyplot as plt  # Import Matplotlib for plotting
import datetime  # Import datetime for handling date and time

# Define the path to the netCDF file containing temperature data
file_path = r'D:\first_project_smart_meteorology\my_data\ERA5_1.nc'

# Open the netCDF file and read the dataset
ds = nc.Dataset(file_path)
# Extract latitude, longitude, temperature, and valid time variables from the dataset
latitude = ds.variables['latitude'][:]
longitude = ds.variables['longitude'][:]
temperature = ds.variables['msl'][:]  # 2-meter temperature data
valid_time = ds.variables['valid_time'][:]  # Time data

# Convert valid_time from seconds since 1970 to datetime objects
start_date = datetime.datetime(1970, 1, 1)  # Define the starting date
time_data = [start_date + datetime.timedelta(seconds=int(t)) for t in valid_time]  # Create a list of datetime objects

# Define the latitude and longitude for Nanjing
nanjing_lat = 32.0615513
nanjing_lon = 118.7915619

# Find the nearest latitude index to Nanjing's latitude
lat_idx = (np.abs(latitude - nanjing_lat)).argmin()  # Get the index of the closest latitude
# Find the nearest longitude index to Nanjing's longitude
lon_idx = (np.abs(longitude - nanjing_lon)).argmin()  # Get the index of the closest longitude

# Extract temperature data for Nanjing using the determined indices
nanjing_temperature = temperature[:, lat_idx, lon_idx]
# Convert temperature from Kelvin to Celsius
nanjing_temperature_celsius = nanjing_temperature - 273.15

# Create a figure for plotting the temperature data
plt.figure(figsize=(12, 6))
# Plot the temperature data against time
plt.plot(time_data, nanjing_temperature_celsius, label='Pressure at Nanjing (hpa)', color='b')
# Set the title of the plot
plt.title('Pressure Variation in Nanjing')
# Label the x-axis
plt.xlabel('Date')
# Label the y-axis
plt.ylabel('Pressure (hpa)')
# Rotate x-axis tick labels for better readability
plt.xticks(rotation=45)
# Add a grid to the plot
plt.grid()
# Add a legend to the plot
plt.legend()
# Adjust layout to prevent clipping of labels
plt.tight_layout()

# Display the plot
plt.show()
