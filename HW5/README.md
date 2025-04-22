## HW5

The online repo of this and other completed assignments can be accessed here:
[https://github.com/Sam-MARTis/AE6104](https://github.com/Sam-MARTis/AE6104)


For questions 1, 2, 3 - refer to pdf solution
For quesions 4, 5, 6 - refer to `GreenStress_Symbolic.py`
The comments on the deformation mapping are written inside the functions. 
To verify results, kindly run the function.



#### Output:

```sh
Spherical strain tensor E

E_actual
[Derivative(f(R), R)**2/2 - 1/2, 0, 0]
[0, -R**2/2 + f(R)**2/2, 0]
[0, 0, (-R**2 + f(R)**2)*cos(Θ)**2/2]


E_physcial
[Derivative(f(R), R)**2/2 - 1/2, 0, 0]
[0, (-R**2 + f(R)**2)/(2*R**2), 0]
[0, 0, (-R**2 + f(R)**2)/(2*R**2)]




Cylindrical strain tensor E

E_actual
[Derivative(f(R), R)**2/2 - 1/2, 0, 0]
[0, -R**2/2 + f(R)**2/2, Φ*f(R)**2/2]
[0, Φ*f(R)**2/2, Φ**2*f(R)**2/2 + λ**2/2 - 1/2]


E_physcial
[Derivative(f(R), R)**2/2 - 1/2, 0, 0]
[0, (-R**2 + f(R)**2)/(2*R**2), Φ*sqrt(R**(-2))*f(R)**2/2]
[0, Φ*sqrt(R**(-2))*f(R)**2/2, Φ**2*f(R)**2/2 + λ**2/2 - 1/2]




Toroidal strain tensor E

E_actual
[C**2*Derivative(g(R, Θ), R)**2/2 - C*f(R, Θ)*cos(Θ)*Derivative(g(R, Θ), R)**2 + f(R, Θ)**2*cos(Θ)**2*Derivative(g(R, Θ), R)**2/2 + Derivative(f(R, Θ), R)**2/2 - 1/2, C**2*Derivative(g(R, Θ), R)*Derivative(g(R, Θ), Θ)/2 - C*f(R, Θ)*cos(Θ)*Derivative(g(R, Θ), R)*Derivative(g(R, Θ), Θ) + f(R, Θ)**2*cos(Θ)**2*Derivative(g(R, Θ), R)*Derivative(g(R, Θ), Θ)/2 + Derivative(f(R, Θ), R)*Derivative(f(R, Θ), Θ)/2, 0]
[C**2*Derivative(g(R, Θ), R)*Derivative(g(R, Θ), Θ)/2 - C*f(R, Θ)*cos(Θ)*Derivative(g(R, Θ), R)*Derivative(g(R, Θ), Θ) + f(R, Θ)**2*cos(Θ)**2*Derivative(g(R, Θ), R)*Derivative(g(R, Θ), Θ)/2 + Derivative(f(R, Θ), R)*Derivative(f(R, Θ), Θ)/2, C**2*Derivative(g(R, Θ), Θ)**2/2 - C*f(R, Θ)*cos(Θ)*Derivative(g(R, Θ), Θ)**2 - R**2/2 + f(R, Θ)**2*cos(Θ)**2*Derivative(g(R, Θ), Θ)**2/2 + f(R, Θ)**2/2 + Derivative(f(R, Θ), Θ)**2/2, 0]
[0, 0, -(C - R*cos(Θ))**2/2]


E_physcial
[C**2*Derivative(g(R, Θ), R)**2/2 - C*f(R, Θ)*cos(Θ)*Derivative(g(R, Θ), R)**2 + f(R, Θ)**2*cos(Θ)**2*Derivative(g(R, Θ), R)**2/2 + Derivative(f(R, Θ), R)**2/2 - 1/2, (C**2*Derivative(g(R, Θ), R)*Derivative(g(R, Θ), Θ) - 2*C*f(R, Θ)*cos(Θ)*Derivative(g(R, Θ), R)*Derivative(g(R, Θ), Θ) + f(R, Θ)**2*cos(Θ)**2*Derivative(g(R, Θ), R)*Derivative(g(R, Θ), Θ) + Derivative(f(R, Θ), R)*Derivative(f(R, Θ), Θ))*sqrt(R**(-2))/2, 0]
[(C**2*Derivative(g(R, Θ), R)*Derivative(g(R, Θ), Θ) - 2*C*f(R, Θ)*cos(Θ)*Derivative(g(R, Θ), R)*Derivative(g(R, Θ), Θ) + f(R, Θ)**2*cos(Θ)**2*Derivative(g(R, Θ), R)*Derivative(g(R, Θ), Θ) + Derivative(f(R, Θ), R)*Derivative(f(R, Θ), Θ))*sqrt(R**(-2))/2, (C**2*Derivative(g(R, Θ), Θ)**2 - 2*C*f(R, Θ)*cos(Θ)*Derivative(g(R, Θ), Θ)**2 - R**2 + f(R, Θ)**2*cos(Θ)**2*Derivative(g(R, Θ), Θ)**2 + f(R, Θ)**2 + Derivative(f(R, Θ), Θ)**2)/(2*R**2), 0]
[0, 0, -1/2]
```
