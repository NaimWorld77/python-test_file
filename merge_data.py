import xarray as xr
import matplotlib.pyplot as plt


# Dataset path
ds1_path = r'D:\first_project_smart_meteorology\my_data\ERA5_1.nc'
ds2_path = r'D:\first_project_smart_meteorology\my_data\ERA5_2.nc'

# Open dataset
ds1 = xr.open_dataset(ds1_path)
ds2 = xr.open_dataset(ds2_path)

#print(f'This is first part of dataset: {ds1}')
#print(f'This is second set of dataset: {ds2}')

ds = xr.merge([ds1, ds2])

# valid_time: 264, latitude: 221, longitude: 201

lat = 221
lon = 201

msl = ds['msl'].sel(longitude=lon, latitude=lat, method='nearest')


air_pressure_at_mean_sea_level = msl.resample(valid_time='1D').mean()


# Ploting
fig, ax1 = plt.subplots()  
color = 'tab:red'  
ax1.set_xlabel('Date')  
ax1.set_ylabel('Daily Mean pressure (pa)', color=color)  
ax1.plot(air_pressure_at_mean_sea_level.valid_time, air_pressure_at_mean_sea_level, color=color)
ax1.tick_params(axis='y', labelcolor=color)  
date_range = air_pressure_at_mean_sea_level.valid_time.dt.strftime('%Y-%m-%d').values

monthly_ticks = [date for date in date_range if date.endswith('-01')]
monthly_ticks.append(date_range[-1]) 
ax1.set_xticks(monthly_ticks)  
ax1.set_xticklabels(monthly_ticks, rotation=45, ha='right')  

fig.tight_layout()  
plt.subplots_adjust(top=0.9)  
plt.title('Mean sea lever pressure 2023.7.25-2023.8.04') 
plt.grid(linestyle=':')  
plt.show()  