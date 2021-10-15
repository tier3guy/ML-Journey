# Matplotlib is used to draw plottings, most of the drawing utilities is under pyplot lib of matplotlib lib

# Importing pyplot from Matplotlib under alias name of pyplot
import matplotlib.pyplot as pyplot

# Importing numpy lib from creating arrays
import numpy as np

x__coordinate = np.array([0,1,3])
y__coodrinate = np.array([22,45,69])

x1__coordinate = np.array([20,54,780])
y1__coordinate = np.array([2,5,14])

# Font settings for the Tittle and the lables
__font__specification = {
  'font' : 'monospace',
  'color' : 'blue',
  'size' : '12'
}


'''
pyplot.title("Pyplot Practice", fontdict = __font__specification, loc = 'left')
pyplot.xlabel("X Lable goes here ...", fontdict = __font__specification)
pyplot.ylabel("Y Lable goes here ...", fontdict = __font__specification)

'''


# The plot() function is used to draw points (markers) in a diagram. By default, the plot() function draws a line from point to point. It takes two parametrs -> array of x-coordinates and y-coordinates
'''
pyplot.plot(x__coordinate, y__coodrinate)

'''

#If we do not specify the points in the x-axis, they will get the default values [0, 1, 2, 3] (etc. depending on the length of the y-points.
'''
pyplot.plot(y__coodrinate)

'''


# Two draw only markers use --> string notation parameter 'o' --> which means ring
'''
pyplot.plot(x__coordinate,y__coodrinate,'o')

'''

#You can use the keyword argument marker to emphasize each point with a specified marker
'''
pyplot.plot(x__coordinate,y__coodrinate, marker = '.')

'''

#You can use also use the shortcut string notation parameter to specify the marker. This parameter is also called fmt, and is written with this syntax: marker|line|color
'''
pyplot.plot(x__coordinate,y__coodrinate, '.-.b')

'''

# Other parameters are ms --> marker size, mec --> marker edge color, mfc --> marker face color
# you can pass them as parameters as ''' ms = 20, mfc = 'g', mec = 'b' ''' 
'''
More parameters for lines -->

-> liststyle or ls --> dashed or '--', solid or '-', dotted or ':', dashdot or '-.'
-> color or c --> red or r, etc.
-> linewidth or lw --> 1, 2, 3, ... etc.


pyplot.plot(x__coordinate, y__coodrinate, ls = '--', c = 'b', lw = '2', marker = 'o')

'''

# With Pyplot, you can use the grid() function to add grid lines to the plot.
'''
pyplot.grid()
Or you can pass the above explained parameters

'''


# Subplots
# With the subplots() function you can draw multiple plots in one figure. The subplots() function takes three arguments that describes the layout of the figure. The layout is organized in rows and columns, which are represented by the first and second argument. The third argument represents the index of the current plot.

pyplot.subplot(1, 2, 1)
pyplot.title('Income', fontdict = __font__specification)
pyplot.xlabel("X Lable goes here ...", fontdict = __font__specification)
pyplot.ylabel("Y Lable goes here ...", fontdict = __font__specification)
pyplot.grid(color = 'g', lw = '0.5', ls = 'dashed')

pyplot.plot(x1__coordinate, y1__coordinate, c = 'blue')



pyplot.subplot(1, 2, 2)
pyplot.title('Expenses', fontdict = __font__specification)
pyplot.xlabel("X Lable goes here ...", fontdict = __font__specification)
pyplot.ylabel("Y Lable goes here ...", fontdict = __font__specification)
pyplot.grid(color = 'r', lw = '0.5', ls = 'dashed')

pyplot.plot(x__coordinate, y__coodrinate)

# Putting super tittle i.e a tittle for the whole plot
pyplot.suptitle('My super Title')

pyplot.show()