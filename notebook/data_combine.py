import xarray as xr

import matplotlib.pyplot as plt

# Load the newly combined dataset
combined_ds = xr.open_dataset(r'D:\first_project_smart_meteorology\combined_dataset.nc')

# Print the dimensions and variables to check if it was combined correctly
print("Combined Dataset Dimensions:", combined_ds.dims)
print("Combined Dataset Variables:", combined_ds.data_vars)

# You can also print the first few entries of each variable to explore the data
print(combined_ds)

# For specific variables, use this:
# e.g., print mean sea level pressure variable
print(combined_ds['msl'])  # Replace 'msl' with the variable name you want to check

# You can also plot a variable if you'd like to visualize the data (if you're using Jupyter or similar):
combined_ds['msl'].isel(valid_time=0).plot()  # Plot the first time step for the 'msl' variable
