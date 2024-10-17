def calculate_motion():
    # DEFINE VARIABLES
    initial_position = float(input("Enter the initial position (x0) in meters: "))
    initial_velocity = float(input("Enter the initial velocity (v0) in m/s: "))
    acceleration = float(input("Enter the acceleration (a) in m/s²: "))
    time = float(input("Enter the time (t) in seconds: "))

    #DEFINE THE FORMULAS:"x = x0 + v0 * t + 0.5 * a * t²" and "v = v0 + a * t" USING THE VARIABLES ALREADY DEFINED
    final_position = initial_position + initial_velocity * time + 0.5 * acceleration * (time ** 2)
    final_velocity = initial_velocity + acceleration * time

    #PRINT THE RESULTS
    print("Results:")
    print(f"Final Position (x): {final_position:.2f} meters")
    print(f"Final Velocity (v): {final_velocity:.2f} m/s")
    print(f"Acceleration (a): {acceleration:.2f} m/s²")
calculate_motion()