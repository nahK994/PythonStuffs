'''
import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 2)
fig.suptitle('Sin and Cos Graph')
x = np.arange(-2*np.pi, 2*np.pi+0.1, 0.2)

y = np.sin(x)

#axs[0, 0].set_title('Sin graph (Continuous)')
axs[0, 0].plot(x, y, color = 'g')
axs[0, 0].grid(True)
axs[0, 0].set_xticks(np.arange(-2*np.pi, 2*np.pi+0.1, np.pi/2))
axs[0, 0].set_yticks(np.arange(-1, 1.1, 0.25))
axs[0, 0].axhline(lw = 1, color = 'r')
axs[0, 0].axvline(lw = 1, color = 'r')

#axs[0, 1].set_title('Sin graph (Discrete)')
axs[0, 1].scatter(x, y, color = 'g', s = 10)
axs[0, 1].grid(True)
axs[0, 1].set_xticks(np.arange(-2*np.pi, 2*np.pi+0.1, np.pi/2))
axs[0, 1].set_yticks(np.arange(-1, 1.1, 0.25))
axs[0, 1].axhline(lw = 1, color = 'r')
axs[0, 1].axvline(lw = 1, color = 'r')

y = np.cos(x)

#axs[1, 0].set_title('Cos graph (Continuous)')
axs[1, 0].plot(x, y, color = 'b')
axs[1, 0].grid(True)
axs[1, 0].set_xticks(np.arange(-2*np.pi, 2*np.pi+0.1, np.pi/2))
axs[1, 0].set_yticks(np.arange(-1, 1.1, 0.25))
axs[1, 0].axhline(lw = 1, color = 'r')
axs[1, 0].axvline(lw = 1, color = 'r')

#axs[1, 1].set_title('Cos graph (Discrete)')
axs[1, 1].scatter(x, y, color = 'b', s = 10)
axs[1, 1].grid(True)
axs[1, 1].set_xticks(np.arange(-2*np.pi, 2*np.pi+0.1, np.pi/2))
axs[1, 1].set_yticks(np.arange(-1, 1.1, 0.25))
axs[1, 1].axhline(lw = 1, color = 'r')
axs[1, 1].axvline(lw = 1, color = 'r')

plt.show()
'''
'''
# sample code 3
import numpy as np
import matplotlib.pyplot as plt
 
x = np.arange(0, 6*np.pi, 0.2)
y = np.sin(x)
y1 = np.cos(x)

plt.title('Sin Curve')
plt.xlabel('x')
plt.ylabel('sin(x)')

#plt.scatter(x, y, color = 'g', s = 25)
plt.plot(x, y1, color = 'b', lw = 1.0)

plt.xticks(np.arange(0, 6.01*np.pi, np.pi/2))
plt.yticks(np.arange(-1, 1.1, 0.25))

plt.axhline(lw = 1, color = 'r')
plt.axvline(lw = 1, color = 'r')

plt.grid(True)
plt.show()
'''
'''
from matplotlib import pyplot as plt 
  
# x-axis values 
x = [5, 2, 9, 4, 7] 
  
# Y-axis values 
y = [10, 5, 8, 4, 2] 

# Function to plot 
plt.plot(x,y)
# Function to show grid
plt.grid(True)
# function to show the plot 
plt.show()
'''

'''
# importing matplotlib module  
from matplotlib import pyplot as plt 
  
# x-axis values 
x = [5, 2, 9, 4, 7] 
  
# Y-axis values 
y = [10, 5, 8, 4, 2] 
  
# Function to plot the bar 
plt.bar(x,y, width=0.5, color = 'g')

# function to show the plot 
plt.show()
'''


'''
# importing matplotlib module  
from matplotlib import pyplot as plt 
  
# points of set 1 
x = [5, 2, 9, 4, 7] 
y = [10, 5, 8, 4, 2]

# points of set 2 
x1 = [2, 5, 6, 4, 6]
y1 = [5, 2, 7, 9, 3]
  
# Function to plot scatter 
plt.scatter(x, y, color = 'g')
plt.scatter(x1, y1, color = 'r')
  
# function to show the plot 
plt.show() 
'''

import matplotlib.pyplot as plt
 
days = [1,2,3,4,5]
 
sleeping =[7,8,6,11,7]
eating = [2,3,4,3,2]
working =[7,8,7,2,2]
playing = [8,5,7,8,13]
slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['#b2ebf2','#4fc3f7','#009688','#00bfa5']
 
plt.pie(slices,
  labels=activities,
  colors=cols,
  startangle=90,
  shadow= True,
  explode=(0,0.1,0,0),
  autopct='%1.1f%%')
 
plt.title('Pie Plot')
plt.show()

'''
from matplotlib import pyplot as plt 
  
# x-axis values 
x = [5, 2, 9, 4, 7] 
  
# Y-axis values 
y = [10, 5, 8, 4, 2] 

# Function to plot 
plt.plot(x,y)
# Function to show grid
plt.grid(True)
# function to show the plot 
plt.show()
'''
'''
from matplotlib import pyplot as plt
import numpy as np
 
x = ['C', 'C++', 'Java', 'Python', 'PHP']
y = [7, 10, 8, 9, 2] 

plt.title('Programming Languages')  
plt.bar(x,y, width=0.4, color = '#4db6ac')
plt.show()
'''