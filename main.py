# All important libraries
import netCDF4 as nc 
import numpy as np 
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import datetime
import os
from moviepy.editor import ImageSequenceClip

# Dataset Handling
file_path = r'D:\first_project_smart_meteorology\my_data\ERA5_1.nc'
ds = nc.Dataset(file_path)

# Extracting variables from the dataset
longitude = ds.variables['longitude'][:]
latitude = ds.variables['latitude'][:]
valid_time = ds.variables['valid_time'][:]

'''
print(f'this is Longitude: {longitude}')
print(f'this is Latitude : {latitude}')
print(f'this is Valid_time: {valid_time}')
'''

# Convert time data 
start_date = datetime.datetime(2023,7,25)
time_data = [start_date + datetime.timedelta(seconds=int(t)) for t in valid_time]

# Create Directory for Images
output_dir = "pictures"
os.makedirs(output_dir, exist_ok=True)

# Generating Visualizations for Each Time Step
for time_index in range(len(time_data)):
    msl_data = ds.variables['msl'][time_index, :, :]

# Visualization Process
fig = plt.figure(figsize=(12,8))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS)
ax.add_feature(cfeature.LAKES, facecolor='none')
ax.add_feature(cfeature.RIVERS)  

# Contour Plot
contour = ax.contourf(longitude, latitude, msl_data / 100,
                    levels=np.arange(950, 1050, 5),
                    cmap='coolwarm', extend='both', transform=ccrs.PlateCarree())

# Color Bar and Title
cbar = plt.colorbar(contour, orientation='vertical', pad=0.02)
cbar.set_label('Mean Sea Level Pressure (hpa)')
plt.title(f'Mean Sea Level Pressure - Time: {time_data[time_index]}')


# Save the Plot
plt.savefig(os.path.join(output_dir, f'pressure_{time_index:03d}.png'))
plt.close(fig)

'''
# Creating a Video form Images
image_filepaths = [os.path.join(output_dir, f) for f in sorted(os.listdir(output_dir)) if f.endswith('.png')]

# Create a video
clip = ImageSequenceClip(image_filepaths, fps=30)

#Save the Video
output_video_path = 'output_video.mp4'
clip.write_videofile(output_video_path, codec='libx264')
'''
# Complete Message
print(f'All images saved in {output_dir}')
#print(f"All images saved in '{output_dir}', and video saved as '{output_video_path}'.")