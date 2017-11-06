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
$$\alpha_c = \alpha_{CU}\sqrt{\frac{\sum_ix_i^2}{\Delta}}​$$

$$\alpha_m = \alpha_{CU}\sqrt{\frac{N}{\Delta}}$$

where 
$$\Delta = N\sum_ix_i^2-(\sum_ix_i)^2$$
and $\alpha_{CU}$ is **common uncertainty** defined as
$$\alpha_{CU} = \sqrt{\frac{1}{N-2}\sum_i(y_i-mx_i-c)^2}$$

Ref:[1]I. G.Hughes and T. P.A.Hase, *Measurements and their Uncertainties A practical guide to modern error analysis*, 1st ed. Oxford: Oxford University Press, 2010, p. 58.