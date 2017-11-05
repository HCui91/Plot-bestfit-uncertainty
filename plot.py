# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 12:13:37 2017

@author: HCui
"""

import numpy as np
import matplotlib.pyplot as plt

#Load data from files
x,d_x,y,d_y = np.loadtxt("demo.csv",delimiter=",",unpack=True)

################################################
# Any modulation of data set can be done here  #
################################################

#Calculate the gradient and y-intercept
#Reference: Page 58, method of Measurements and their Uncertainties by Ifan Hughes and Thomas Hase
N = np.size(x)
delta = N*np.sum(x**2)-np.sum(x)**2
c = (np.sum(x**2)*np.sum(y)-np.sum(x)*np.sum(x*y))/delta
m = (N*np.sum(x*y)-np.sum(x)*np.sum(y))/delta

#Uncertainty of c and m
d_cu = np.sqrt(np.sum((y-m*x-c)**2)/(N-2))
d_c = d_cu*np.sqrt(np.sum(x**2)/delta)
d_m = d_cu*np.sqrt(N/delta)

#Generate a line with calculated gradient and interception
x_p = np.linspace(np.min(x)*0.9,np.max(x)*1.1,1000) # Adjust this if x max/min is 0
y_p = x_p * m + c

#Plot with residuals
fig1 = plt.figure(1,figsize=(10,9))
frame1=fig1.add_axes((.1,.3,.8,.6))
plt.plot(x_p, y_p, '-', color='black') 
plt.plot(x,y,'o',color='blue')
plt.ylabel(r'$X axis$',fontsize=15)
plt.autoscale(enable=True, axis=u'both', tight=True)
plt.title(r'Title')
plt.grid()

frame2=fig1.add_axes((.1,.1,.8,.2))
difference = y-(m*x+c)
plt.plot(x, difference, 'bo')
plt.errorbar(x,difference,xerr=d_x,yerr=np.sqrt((d_y*m)**2+c**2),linestyle="None",color='blue')
frame2.set_ylabel(r'$Residual$',fontsize=11)
plt.xlabel(r'X axis',fontsize=15)
plt.grid()
plt.savefig("plot")
print("Uncertainty of slope",d_m,"Uncertainty of y-intercept",d_c)