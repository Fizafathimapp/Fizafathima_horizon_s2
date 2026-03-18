import math

# -------- Part A: Distance Calculation --------
try:
    x1 = float(input("Enter origin x1: "))
    y1 = float(input("Enter origin y1: "))
    x2 = float(input("Enter destination x2: "))
    y2 = float(input("Enter destination y2: "))

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"Distance to destination: {distance:.2f} meters")

# -------- Part B: Motion Parameters --------
    u = float(input("Enter initial velocity (m/s): "))
    a = float(input("Enter acceleration (m/s^2): "))
    vmax = float(input("Enter maximum speed (m/s): "))

    # Time to reach max speed
    time_to_vmax = (vmax - u) / a if a != 0 else 0
    distance_accel = (u * time_to_vmax) + (0.5 * a * time_to_vmax**2)

    if distance_accel >= distance:
        # Rover reaches destination before max speed
        # Using: s = ut + 0.5at^2
        A = 0.5 * a
        B = u
        C = -distance

        discriminant = B**2 - 4*A*C
        time = (-B + math.sqrt(discriminant)) / (2*A)

    else:
        # Rover reaches max speed then continues
        remaining_distance = distance - distance_accel
        time_constant = remaining_distance / vmax
        time = time_to_vmax + time_constant

    print(f"Time required: {time:.2f} seconds")

# -------- Part C: Error Handling --------
except Exception as e:
    print("Invalid input! Please enter numeric values only.")