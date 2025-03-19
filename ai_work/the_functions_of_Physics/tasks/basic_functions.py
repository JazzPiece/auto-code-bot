def velocity(distance, time):
    return distance / time

def acceleration(velocity, time):
    return velocity / time

def force(mass, acceleration):
    return mass * acceleration

def energy(mass, velocity):
    return 0.5 * mass * velocity**2

def power(work, time):
    return work / time

def pressure(force, area):
    return force / area

def momentum(mass, velocity):
    return mass * velocity

def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity**2

def potential_energy(mass, height, gravity=9.81):
    return mass * height * gravity

def work(force, distance, angle):
    return force * distance * math.cos(math.radians(angle))

def frequency(period):
    return 1 / period

def wavelength(speed, frequency):
    return speed / frequency

def electric_power(current, voltage):
    return current * voltage

def resistance(voltage, current):
    return voltage / current

def capacitance(charge, voltage):
    return charge / voltage

def inductance(inductance, current_change_rate):
    return inductance * current_change_rate

def magnetic_field(current, length, constant=4*math.pi*1e-7):
    return constant * current / (2 * math.pi * length)