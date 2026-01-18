"""
Student name : Ukeje Frank Chika

Docstring for tire volume.week02_code_along.can_sizes
"""
import math

def mai():
    can_names = [
        "#1picnic", "#1 Tall", "#2", "#2.5", "#3 Cylindser", 
        "#5", "#6z", "#8z short", "#10", "#211", "#300", "#303"
    ]
    radiuses = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40,
                6.83, 15.72, 6.83, 7.62, 8.10,

    ]
    heights = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29,
                8.89, 7.62, 17.78, 12.38, 11.27, 11.11,]
    cost_per_can = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22,
                    0.26, 1.53, 0.34, 0.38, 0.42,]
    for i in range(len(can_names)):
        name = can_names[i]
        radius = radiuses[i]
        height = heights[i]
        cost = cost_per_can[i]
        volume = can_volume(radius, height)
        area = can_surface_area(radius, height)
        efficiency = storage_efficiency(volume, area)
        cost_per_volume = cost/volume
        print(f"{name} {efficiency:.2f}")
def can_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume
def can_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area
def storage_efficiency(volume, surface_area):
    efficiency = volume/surface_area
    return efficiency                    
mai()





