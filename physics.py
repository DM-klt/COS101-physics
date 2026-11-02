# COS 101 Physics Assignment

# 1. Speed
def speed(distance, time):
    return distance / time

# 2. Force
def force(mass, acceleration):
    return mass * acceleration

# 3. Density
def density(mass, volume):
    return mass / volume

# 4. Work Done
def work_done(force, distance):
    return force * distance

# 5. Kinetic Energy
def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

print("Speed:", speed(100, 20), "m/s")
print("Force:", force(10, 5), "N")
print("Density:", density(50, 10), "kg/m³")
print("Work Done:", work_done(20, 5), "J")
print("Kinetic Energy:", kinetic_energy(10, 4), "J")
