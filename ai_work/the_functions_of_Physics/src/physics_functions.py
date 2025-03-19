import math

def kinematics(v_initial, v_final, time):
    acceleration = (v_final - v_initial) / time
    displacement = ((v_initial + v_final) / 2) * time
    return acceleration, displacement

def newton_laws(force, mass):
    acceleration = force / mass
    return acceleration

def work_energy(force, displacement, angle):
    work = force * displacement * math.cos(angle)
    return work

def momentum(mass, velocity):
    momentum = mass * velocity
    return momentum

def gravitation(mass1, mass2, distance):
    force = (6.67e-11) * (mass1 * mass2) / (distance ** 2)
    return force

def thermodynamics(heat_added, work_done):
    change_in_internal_energy = heat_added - work_done
    return change_in_internal_energy

def optics(focal_length, object_distance):
    image_distance = (1 / focal_length - 1 / object_distance) ** -1
    return image_distance

def electromagnetism(charge, electric_field):
    force = charge * electric_field
    return force