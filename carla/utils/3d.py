import numpy as np


K = np.array([[914.01472431, 0.0, 640.0],
                             [0.0, 914.01472431, 480.0],
                             [0.0, 0.0, 1.0]])

sensor_refpoint= [ 1.96666723e+01 , 1.82549531e-02, -9.58280560e-01]

cords = np.zeros((8, 4))
extent = {
    "x": 2.350175619125366/2,
    "y": 0.7662330269813538/2,
    "z": 1.6494941711425781/2,   
}
cords[0, :] = np.array([extent['x'], extent['y'], -extent['z'], 1])
cords[1, :] = np.array([-extent['x'], extent['y'], -extent['z'], 1])
cords[2, :] = np.array([-extent['x'], -extent['y'], -extent['z'], 1])
cords[3, :] = np.array([extent['x'], -extent['y'], -extent['z'], 1])
cords[4, :] = np.array([extent['x'], extent['y'], extent['z'], 1])
cords[5, :] = np.array([-extent['x'], extent['y'], extent['z'], 1])
cords[6, :] = np.array([-extent['x'], -extent['y'], extent['z'], 1])
cords[7, :] = np.array([extent['x'], -extent['y'], extent['z'], 1])
cords[:, :3] += sensor_refpoint
# cords_y_minus_z_x = np.concatenate([cords[1, :], -cords[2, :], cords[0, :]])

# bbox = np.transpose(np.dot(K, cords_y_minus_z_x))

# print(cords[])
for a in cords:
    # print(a)
    x, y, z, ignore = a
    sensor_refpoint = [y, -1 * z, x]
    sensor_refpoint = np.array(sensor_refpoint)
    sensor_refpoint_column_vector = sensor_refpoint.reshape(3,1)
    b = np.transpose(np.dot(K, sensor_refpoint_column_vector))
    print(b[0][0] / b[0][2], b[0][1] / b[0][2], b[0][2])
# 

# sensor_refpoint = [y, -1 * z, x]
# sensor_refpoint = np.array(sensor_refpoint)
# print("Updated sensor_refpoint:", sensor_refpoint)

# sensor_refpoint_column_vector = sensor_refpoint.reshape(3,1)
# print("Updated sensor_refpoint:", sensor_refpoint_column_vector)
# a = np.transpose(np.dot(K, sensor_refpoint_column_vector))
# print(a)
# print(a[0][0] / a[0][2])
# print(a[0][1] / a[0][2])
