# two_wattmeter_method.py
# Program to calculate total power and power factor
# using the Two-Wattmeter Method

import math

print("=== Two-Wattmeter Method ===")

# Input wattmeter readings
W1 = float(input("Enter Wattmeter 1 reading (W): "))
W2 = float(input("Enter Wattmeter 2 reading (W): "))

# Total three-phase active power
total_power = W1 + W2

# Calculate tan(phi)
if total_power == 0:
    print("Invalid readings: total power cannot be zero.")
else:
    tan_phi = math.sqrt(3) * (W1 - W2) / total_power

    # Calculate phase angle
    phi = math.atan(tan_phi)

    # Calculate power factor
    power_factor = abs(math.cos(phi))

    # Display results
    print("\n--- Two-Wattmeter Results ---")
    print(f"Wattmeter 1 = {W1:.2f} W")
    print(f"Wattmeter 2 = {W2:.2f} W")
    print(f"Total Active Power = {total_power:.2f} W")
    print(f"Phase Angle = {math.degrees(phi):.2f} degrees")
    print(f"Power Factor = {power_factor:.3f}")

    # Determine the type of power factor
    if W1 < W2:
        print("Power Factor Type = Leading")
    elif W1 > W2:
        print("Power Factor Type = Lagging")
    else:
        print("Power Factor Type = Unity")
