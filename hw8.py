# Intro to Matplotlib

import numpy as np

#1
def make_sine_wave(x, A, w):
    return A * np.sin(w * x)

#2
x = np.linspace(0,2 * np.pi, 1000)

#3
amplitudes = np.array([0.5, 1, 1.5, 2, 2.5])

frequencies = np.array([1, 2, 3, 4, 5])

#4
import matplotlib.pyplot as plt 


plt.figure(figsize=(10, 6))

#5
for A, w in zip(amplitudes, frequencies):
    y = make_sine_wave(x, A, w)
    plt.plot(x, y, label=f"A={A}, w={w}")

#6
plt.title("Sine Waves with Different Amplitudes and Frequencies")
plt.xlabel("x (radians)")
plt.ylabel("y = A · sin(w · x)")
plt.legend()
plt.grid(True)
plt.show()

#2 Data with Pandas

import pandas as pd 

#2.1 
df = pd.read_csv("stars.csv")

df.columns = df.columns.str.strip()

#2.2
print(df.head())

print("Shape:", df.shape)

print(df.info())

# 2.3
avg_mass = df["Mass (M☉)"].mean()
avg_temp = df["Temperature (K)"].mean()
print("Average Mass:", avg_mass)
print("Average Temperature:", avg_temp)


largest_radius_star = df[df["Radius (R☉)"] == df["Radius (R☉)"].max()]
print("Star with Largest Radius:")
print(largest_radius_star)


m_type_count = df[df["Spectral_Type"].str.startswith("M")].shape[0]
print("Number of M-type Stars:", m_type_count)

# 2.4
closest_stars = df.sort_values("Distance (ly)").head(3)
print("3 Closest Stars:")
print(closest_stars)

# 2.5
m_type_stars = df[df["Spectral_Type"].str.startswith("M")]

m_type_stars.to_csv("m_type_stars.csv", index=False)

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.hist(df["Temperature (K)"], bins=10, edgecolor="black")
plt.title("Temperature Distribution of Stars")
plt.xlabel("Temperature (K)")
plt.ylabel("Number of Stars")
plt.grid(True)
plt.show()

#3 Seaborn!

import seaborn as sns 


penguins = sns.load_dataset("penguins").dropna(subset=["bill_length_mm", "bill_depth_mm", "body_mass_g", "species"])

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.scatterplot(
    data=penguins,
    x="bill_length_mm",
    y="bill_depth_mm",
    hue="species",
    ax=axes[0]
)
axes[0].set_title("Bill Length vs. Bill Depth")
axes[0].set_xlabel("Bill Length (mm)")
axes[0].set_ylabel("Bill Depth (mm)")
axes[0].legend(title="Species")

# Right plot: Histogram of body mass
sns.histplot(
    data=penguins,
    x="body_mass_g",
    bins=20,
    kde=True,
    ax=axes[1]
)
axes[1].set_title("Body Mass Distribution")
axes[1].set_xlabel("Body Mass (g)")
axes[1].set_ylabel("Number of Penguins")

# Layout adjustment
plt.tight_layout()
plt.show()

