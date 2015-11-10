#!/usr/bin/env python
import numpy
import csv
from matplotlib import pyplot as plt
from pylab import *
  
# Use numpy to import data from CSV file
data=numpy.genfromtxt('results.csv',delimiter=',')
# Create a data array for each column of data needed
nodes=data[:,0]
cores=data[:,1]
time=data[:,2]
   
# Create a plot of results
plt.figure(figsize=(20,5))
 
plt.title('Abaqus Run')
# Left Plot
   
plt.subplot( 1,2,1 ) # 1 row, 2 columns, figure 1
plt.plot(cores,time,color="green",label="Cores/Time")
plt.ylabel('Run Time')
plt.xlabel('#Cores')
legend(loc='upper right')
#plt.title('Abaqus Run')
  
# Right Plot
    
plt.subplot( 1,2,2 ) #
plt.plot(nodes,time,color="blue",label="Nodes/Time")
plt.ylabel('Run Time')
plt.xlabel('#Nodes')
#plt.title('Abaqus Run')

# Display the legend defined in the plot function
legend(loc='upper right')

# Automatically adjusts positions so there's no overlapping content
#plt.tight_layout()

# Add padding to the layout
#plt.tight_layout(pad=1.0, w_pad=2.0, h_pad=2.0)

# Display the plot on screen
plt.show()

# Or save the plot to file using 72 dpi
# savefig("results1.png",dpi=72)
	     
