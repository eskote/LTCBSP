# Alien List
alien_o = {'color': 'green', 'points': 5}

print(alien_o)

alien_o['x_position'] = 0
alien_o['y_position'] = 25

print(alien_o)

alien_m = {}

alien_m['color'] = 'red'
alien_m['points'] = 15

print(alien_m)

print(f"The alien o is {alien_o['color']} and is worth {alien_o['points']} \
points!")

alien_o['color'] = 'yellow'
print(f"You have hit alien o and it has changed color to\
 {alien_o['color']}!")

alien_o = {'x_position': 0, 'y_position': 25, 'speed': 'medium', 'points': 5}
print(f"Original position: {alien_o['x_position']}")

if alien_o['speed'] == 'slow':
    x_increment = 1
elif alien_o['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

alien_o['x_position'] = alien_o['x_position'] + x_increment
print(f"New position: {alien_o['x_position']}")

alien_o['speed'] = 'fast'

if alien_o['speed'] == 'slow':
    x_increment = 1
elif alien_o['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

alien_o['x_position'] = alien_o['x_position'] + x_increment
print(f"New position: {alien_o['x_position']}")

del alien_o['points']
print(alien_o)

point_value = alien_o.get('point', 'no point value assigned')
print(point_value)