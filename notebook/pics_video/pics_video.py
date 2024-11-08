import xarray as xr
import os
import netCDF4 as nc  # Import the netCDF4 library to handle netCDF files
import numpy as np  # Import NumPy for numerical operations
import matplotlib.pyplot as plt  # Import Matplotlib for plotting
import datetime  # Import datetime for handling date and time

# Load the combined dataset
combined_ds = xr.open_dataset(r'D:\first_project_smart_meteorology\combined_dataset.nc')

# Create a directory to save the images
output_dir = 'output_images'
os.makedirs(output_dir, exist_ok=True)

# Extract the variable you want to plot (e.g., 'msl' for mean sea level pressure)
msl_data = combined_ds['msl']

# Loop through each time step and save an image
for i in range(msl_data.sizes['valid_time']):
    plt.figure(figsize=(8, 6))
    msl_data.isel(valid_time=i).plot()
    
    # Save the figure as an image
    image_path = os.path.join(output_dir, f'msl_image_{i:03d}.png')
    plt.title(f'Mean Sea Level Pressure - Time Step {i}')
    plt.savefig(image_path)
    plt.close()

print("Images saved successfully!")

from moviepy.editor import ImageSequenceClip

# Define the path to the images and get all image filenames
image_folder = 'output_images'
image_files = [os.path.join(image_folder, f) for f in sorted(os.listdir(image_folder)) if f.endswith('.png')]

# Create a video clip from the images
fps = 1  # Frames per second, adjust according to how fast you want the video to play
clip = ImageSequenceClip(image_files, fps=fps)

# Save the video
clip.write_videofile('msl_video.mp4', codec='libx264')

print("Video created successfully!")