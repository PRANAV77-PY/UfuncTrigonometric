#convert degree into radians
import numpy as np

arr = np.array([90,180,270,360])

x = np.deg2rad(arr)

print(x)

#convert radiensto degree
import numpy as np

arr = np.array([np.pi/2,np.pi,1.5*np.pi,2*np.pi])

x = np.rad2deg(arr)

print(x)