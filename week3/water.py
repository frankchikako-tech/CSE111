


def water_column_height(tower_height, tank_height):

 h = tower_height + 3 * tank_height / 4
 return h

def pressure_gain_from_water_height(height):
  p = (998.2 * 9.80665 * height) / 1000
  return p

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
  p = (friction_factor * pipe_length * 998.2 * fluid_velocity**2) / (2 * pipe_diameter * 1000)
  return p

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
  p = (-0.04 * 998.2 * fluid_velocity**2 * quantity_fittings) / (2 * 1000)
  return p

def reynolds_number(hydraulic_diameter, fluid_velocity):
  Re = (998.2 * fluid_velocity * hydraulic_diameter) / 0.001003
  return Re

def pressure_loss_from_pipe_reduction(large_diameter, fluid_velocity_large, reynolds_number, small_diameter):
  k = (0.1+50/reynolds_number)*((large_diameter/small_diameter)**4-1)
  p = (k * 998.2 * fluid_velocity_large**2) / (2 * 1000)