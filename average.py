
import pandas as pd

# Create a list of data
data = [
    ["Toyota Camry", 30, 2.5, 170, 3, 8.5, 2019, "Japan"],
    ["Honda Accord", 33, 2.4, 185, 3, 7.5, 2020, "Japan"],
    ["Ford Fusion", 28, 2.0, 165, 3, 8.0, 2017, "United States"],
    ["Chevy Malibu", 29, 1.5, 155, 3, 8.5, 2018, "United States"],
    ["Nissan Altima", 31, 2.5, 180, 3, 7.0, 2019, "Japan"],
]

# Create a DataFrame
df = pd.DataFrame(data, columns=[
    "manufacturer_and_model",
    "fuel_economy",
    "engine_displacement",
    "horsepower_rating",
    "vehicle_weight",
    "acceleration_time",
    "production_year",
    "country_of_origin"
])

# Filter for cars with a fuel economy of at least 30 mpg
df_filtered = df[df['fuel_economy'] >= 30]

# Calculate the average acceleration time
average_acceleration_time = df_filtered["acceleration_time"].mean()

# Print the average acceleration time
print(average_acceleration_time)