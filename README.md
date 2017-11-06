# Linear least square fit and plotting with uncertainty

## I. Introduction

This code is used as plot tool in my second year physics lab period. It can import data from a comma delimitated csv file and generate linear best fit line with residuals and uncertainties.

## II. Theory

I used method of least squares[1] in a linear function of x and y,

y=mx+c

where m is the gradient and c is the y-intercept.

![This is the rendered form of the equation. You can not edit this directly. Right click will give you the option to save the image, and in most browsers you can drag the image onto your desktop or another program.](https://latex.codecogs.com/gif.latex?%5Cbg_white%20c%3D%5Cfrac%7B%5Csum_i%7Bx%5E2_i%7D%5Csum_iy_i-%5Csum_i%7Bx_i%7D%5Csum_ix_iy_i%7D%7B%5CDelta%7D)

![](https://latex.codecogs.com/gif.latex?%5Cbg_white%20m%3D%5Cfrac%7BN%5Csum_ix_iy_i%5Csum_ix_i%5Csum_iy_i%7D%7B%5CDelta%7D)

with the uncertainty in the intercept and the gradient,
![alpha c](https://latex.codecogs.com/gif.latex?%5Cbg_white%20%5Calpha_c%20%3D%20%5Calpha_%7BCU%7D%5Csqrt%7B%5Cfrac%7B%5Csum_ix_i%5E2%7D%7B%5CDelta%7D%7D)

![alpha m](https://latex.codecogs.com/gif.latex?%5Cbg_white%20%5Calpha_m%20%3D%20%5Calpha_%7BCU%7D%5Csqrt%7B%5Cfrac%7BN%7D%7B%5CDelta%7D%7D)

where 

![](https://latex.codecogs.com/gif.latex?%5Cbg_white%20%5CDelta%20%3D%20N%5Csum_ix_i%5E2-%28%5Csum_ix_i%29%5E2)

and $\alpha_{CU}$ is **common uncertainty** defined as

![](https://latex.codecogs.com/gif.latex?%5Cbg_white%20%5Calpha_%7BCU%7D%20%3D%20%5Csqrt%7B%5Cfrac%7B1%7D%7BN-2%7D%5Csum_i%28y_i-mx_i-c%29%5E2%7D)

Ref:[1]I. G.Hughes and T. P.A.Hase, *Measurements and their Uncertainties A practical guide to modern error analysis*, 1st ed. Oxford: Oxford University Press, 2010, p. 58.