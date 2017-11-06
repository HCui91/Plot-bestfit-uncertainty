# Linear least square fit and plotting with uncertainty

## I. Introduction

This code is used as plot tool in my second year physics lab period. It can import data from a comma delimitated csv file and generate linear best fit line with residuals and uncertainties.

## II. Theory

I used method of least squares[1] in a linear function of x and y,
$$y=mx+c$$
where m is the gradient and c is the y-intercept.
$$c=\frac{\sum_i{x^2_i}\sum_iy_i-\sum_i{x_i}\sum_ix_iy_i}{\Delta}$$

$$m=\frac{N\sum_ix_iy_i\sum_ix_i\sum_iy_i}{\Delta}$$

with the uncertainty in the intercept and the gradient,
$$\alpha_c = \alpha_{CU}\sqrt{\frac{\sum_ix_i^2}{\Delta}}$$

$$\alpha_m = \alpha_{CU}\sqrt{\frac{N}{\Delta}}$$

where 
$$\Delta = N\sum_ix_i^2-(\sum_ix_i)^2$$
and $\alpha_{CU}$ is **common uncertainty** defined as
$$\alpha_{CU} = \sqrt{\frac{1}{N-2}\sum_i(y_i-mx_i-c)^2}$$

Ref:[1]I. G.Hughes and T. P.A.Hase, *Measurements and their Uncertainties A practical guide to modern error analysis*, 1st ed. Oxford: Oxford University Press, 2010, p. 58.