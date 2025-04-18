from CurvilinearObjectsCalculator import rvec_cyl, rvec_sph, rvec_tor, christoffelSecondKind_cyl, christoffelSecondKind_sph, christoffelSecondKind_tor, r_cyl, th_cyl, z_cyl,  r_sph, th_sph, ph_sph,  r_tor, ph_tor, R, th_tor
from sympy import *
print("\033c")
def covariantDerivativeVector(rvec, christoffelSecondKind, u1, u2, u3):
    u = [u1, u2, u3]
    covDerivative = [[0 for _ in range(3)] for i in range(3)]
    for i in range(3):
        for m in range(3):
            covDerivative[m][i] = diff(rvec[m], u[i])
            for l in range(3):
                covDerivative[m][i] += christoffelSecondKind[l][i][m] * rvec[l]
            covDerivative[m][i] = simplify(covDerivative[m][i])
    return covDerivative


def covariantDerivativeTensor(T, christoffelSecondKind, u1, u2, u3):
    u = [u1, u2, u3]
    covDerivative = [[[0 for _ in range(3)] for __ in range(3)] for ____ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                covDerivative[i][j][k] = diff(T[i][j], u[k])
                for m in range(3):
                    covDerivative[i][j][k] += christoffelSecondKind[m][k][i]*T[m][j] + christoffelSecondKind[m][k][j]*T[i][m]
                covDerivative[i][j][k] = simplify(covDerivative[i][j][k])
        
    return covDerivative


def computeDivergenceVector(covDerivative):
    divergence = 0
    for i in range(3):
        divergence += covDerivative[i][i]
    return simplify(divergence)

def computeDivergenceTensor(covDerivative):
    divergence = [0 for _ in range(3)]
    for i in range(3):
        for m in range(3):
            divergence[i] += covDerivative[i][m][m]
        divergence[i] = simplify(divergence[i])
    return divergence

if __name__ == "__main__":
    r1, r2, r3 = [Function(name)(r_sph, th_sph, ph_sph) for name in ('r1', 'r2', 'r3')]
    c1, c2, c3 = [Function(name)(r_cyl, th_cyl, z_cyl) for name in ('c1', 'c2', 'c3')]
    t1, t2, t3 = [Function(name)(r_tor, th_tor, ph_tor) for name in ('t1', 't2', 't3')]
    a_sph = [r1, r2, r3]
    a_cyl = [c1, c2, c3]
    a_tor = [t1, t2, t3]

    covDer_sph = covariantDerivativeVector(a_sph, christoffelSecondKind_sph, r_sph, th_sph, ph_sph)
    covDer_cyl = covariantDerivativeVector(a_cyl, christoffelSecondKind_cyl, r_cyl, th_cyl, z_cyl)
    covDer_tor = covariantDerivativeVector(a_tor, christoffelSecondKind_tor, r_tor, ph_tor , th_tor)


    for i in covDer_sph:
        print(i)
    print()
    for i in covDer_cyl:
        print(i)
    print()
    for i in covDer_tor:
        print(i)
    print(diff(c1, r_cyl))
    print("\n\n\n\n\n\n")

    """
    [Derivative(r1(r, th, ph), r), 1.0*r*r2(r, th, ph)*cos(ph)**2 + Derivative(r1(r, th, ph), th), 1.0*r*r3(r, th, ph) + Derivative(r1(r, th, ph), ph)]
    [Derivative(r2(r, th, ph), r) - 1.0*r2(r, th, ph)/r, -1.0*r3(r, th, ph)*tan(ph) + Derivative(r2(r, th, ph), th) + 1.0*r1(r, th, ph)/r, 1.0*r2(r, th, ph)*tan(ph) + Derivative(r2(r, th, ph), ph)]
    [Derivative(r3(r, th, ph), r) - 1.0*r3(r, th, ph)/r, -0.5*r2(r, th, ph)*sin(2*ph) + Derivative(r3(r, th, ph), th), Derivative(r3(r, th, ph), ph) + 1.0*r1(r, th, ph)/r]

    [Derivative(c1(r, th, z), r), 1.0*r*c2(r, th, z) + Derivative(c1(r, th, z), th), Derivative(c1(r, th, z), z)]
    [Derivative(c2(r, th, z), r) - 1.0*c2(r, th, z)/r, Derivative(c2(r, th, z), th) + 1.0*c1(r, th, z)/r, Derivative(c2(r, th, z), z)]
    [Derivative(c3(r, th, z), r), Derivative(c3(r, th, z), th), Derivative(c3(r, th, z), z)]

    [Derivative(t1(r, th, ph), r), 1.0*r*t2(r, th, ph) + Derivative(t1(r, th, ph), ph), -1.0*(R - r*cos(th))*t3(r, th, ph)*cos(th) + Derivative(t1(r, th, ph), th)]
    [Derivative(t2(r, th, ph), r) - 1.0*t2(r, th, ph)/r, Derivative(t2(r, th, ph), ph) + 1.0*t1(r, th, ph)/r, (r*Derivative(t2(r, th, ph), th) + 1.0*(R - r*cos(th))*t3(r, th, ph)*sin(th))/r]
    [((R - r*cos(th))*Derivative(t3(r, th, ph), r) + 1.0*t3(r, th, ph)*cos(th))/(R - r*cos(th)), (-1.0*r*t3(r, th, ph)*sin(th) + (R - r*cos(th))*Derivative(t3(r, th, ph), ph))/(R - r*cos(th)), (1.0*r*t2(r, th, ph)*sin(th) + (R - r*cos(th))*Derivative(t3(r, th, ph), th) - 1.0*t1(r, th, ph)*cos(th))/(R - r*cos(th))]
    """
    
    rT11, rT12, rT13, rT21, rT22, rT23, rT31, rT32, rT33 = symbols('rT11 rT12 rT13 rT21 rT22 rT23 rT31 rT32 rT33')
    cT11, cT12, cT13, cT21, cT22, cT23, cT31, cT32, cT33 = symbols('cT11 cT12 cT13 cT21 cT22 cT23 cT31 cT32 cT33')
    tT11, tT12, tT13, tT21, tT22, tT23, tT31, tT32, tT33 = symbols('tT11 tT12 tT13 tT21 tT22 tT23 tT31 tT32 tT33')
    T_sph = [[rT11, rT12, rT13], [rT21, rT22, rT23], [rT31, rT32, rT33]]
    T_cyl = [[cT11, cT12, cT13], [cT21, cT22, cT23], [cT31, cT32, cT33]]
    T_tor = [[tT11, tT12, tT13], [tT21, tT22, tT23], [tT31, tT32, tT33]]
    
    covDer_sphT = covariantDerivativeTensor(T_sph, christoffelSecondKind_sph, r_sph, th_sph, ph_sph)
    covDer_cylT = covariantDerivativeTensor(T_cyl, christoffelSecondKind_cyl, r_cyl, th_cyl, z_cyl)
    covDer_torT = covariantDerivativeTensor(T_tor, christoffelSecondKind_tor, r_tor, ph_tor , th_tor)
    
    for i in covDer_sphT:
        for j in i:
            print(j)
        print()
    print()
    for i in covDer_cylT:
        for j in i:
            print(j)
        print()
    print()
    for i in covDer_torT:
        for j in i:
            print(j)
        print()
        # print(i)
    """
    [0, 1.0*r*(rT12 + rT21)*cos(ph)**2, 1.0*r*(rT13 + rT31)]
    [-1.0*rT12/r, 1.0*(r*(r*rT22*cos(ph)**2 - rT13*tan(ph)) + rT11)/r, 1.0*r*rT32 + 1.0*rT12*tan(ph)]
    [-1.0*rT13/r, 1.0*r*rT23*cos(ph)**2 - 0.5*rT12*sin(2*ph), 1.0*r*rT33 + 1.0*rT11/r]

    [-1.0*rT21/r, 1.0*(r*(r*rT22*cos(ph)**2 - rT31*tan(ph)) + rT11)/r, 1.0*r*rT23 + 1.0*rT21*tan(ph)]
    [-2.0*rT22/r, 1.0*(-r*(rT23 + rT32)*tan(ph) + rT12 + rT21)/r, 2.0*rT22*tan(ph)]
    [-2.0*rT23/r, -0.5*rT22*sin(2*ph) - 1.0*rT33*tan(ph) + 1.0*rT13/r, 1.0*rT23*tan(ph) + 1.0*rT21/r]

    [-1.0*rT31/r, 1.0*r*rT32*cos(ph)**2 - 0.5*rT21*sin(2*ph), 1.0*r*rT33 + 1.0*rT11/r]
    [-2.0*rT32/r, -0.5*rT22*sin(2*ph) - 1.0*rT33*tan(ph) + 1.0*rT31/r, 1.0*rT32*tan(ph) + 1.0*rT12/r]
    [-2.0*rT33/r, -0.5*(rT23 + rT32)*sin(2*ph), 1.0*(rT13 + rT31)/r]


    [0, 1.0*r*(cT12 + cT21), 0]
    [-1.0*cT12/r, 1.0*cT11/r + 1.0*cT22*r, 0]
    [0, 1.0*cT23*r, 0]

    [-1.0*cT21/r, 1.0*cT11/r + 1.0*cT22*r, 0]
    [-2.0*cT22/r, 1.0*(cT12 + cT21)/r, 0]
    [-1.0*cT23/r, 1.0*cT13/r, 0]

    [0, 1.0*cT32*r, 0]
    [-1.0*cT32/r, 1.0*cT31/r, 0]
    [0, 0, 0]


    [0, 1.0*r*(tT12 + tT21), -1.0*(R - r*cos(th))*(tT13 + tT31)*cos(th)]
    [-1.0*tT12/r, 1.0*r*tT22 + 1.0*tT11/r, 1.0*(R - r*cos(th))*(-r*tT32*cos(th) + tT13*sin(th))/r]
    [1.0*tT13*cos(th)/(R - r*cos(th)), 1.0*r*(-tT13*sin(th) + tT23*(R - r*cos(th)))/(R - r*cos(th)), 1.0*(r*tT12*sin(th) - tT11*cos(th) - tT33*(R - r*cos(th))**2*cos(th))/(R - r*cos(th))]

    [-1.0*tT21/r, 1.0*r*tT22 + 1.0*tT11/r, 1.0*(R - r*cos(th))*(-r*tT23*cos(th) + tT31*sin(th))/r]
    [-2.0*tT22/r, 1.0*(tT12 + tT21)/r, 1.0*(R - r*cos(th))*(tT23 + tT32)*sin(th)/r]
    [1.0*tT23*(R - 2*r*cos(th))/(r*(-R + r*cos(th))), 1.0*(-r**2*tT23*sin(th) + tT13*(R - r*cos(th)))/(r*(R - r*cos(th))), 1.0*(r*(r*tT22*sin(th) - tT21*cos(th)) + tT33*(R - r*cos(th))**2*sin(th))/(r*(R - r*cos(th)))]

    [1.0*tT31*cos(th)/(R - r*cos(th)), 1.0*r*(-tT31*sin(th) + tT32*(R - r*cos(th)))/(R - r*cos(th)), 1.0*(r*tT21*sin(th) - tT11*cos(th) - tT33*(R - r*cos(th))**2*cos(th))/(R - r*cos(th))]
    [1.0*tT32*(R - 2*r*cos(th))/(r*(-R + r*cos(th))), 1.0*(-r**2*tT32*sin(th) + tT31*(R - r*cos(th)))/(r*(R - r*cos(th))), 1.0*(r*(r*tT22*sin(th) - tT12*cos(th)) + tT33*(R - r*cos(th))**2*sin(th))/(r*(R - r*cos(th)))]
    [2.0*tT33*cos(th)/(R - r*cos(th)), 2.0*r*tT33*sin(th)/(-R + r*cos(th)), 1.0*(r*tT23*sin(th) + r*tT32*sin(th) - tT13*cos(th) - tT31*cos(th))/(R - r*cos(th))]
    """
    
    
    print("Diverence of vector")
    div_sph = computeDivergenceVector(covDer_sph)
    div_cyl = computeDivergenceVector(covDer_cyl)
    div_tor = computeDivergenceVector(covDer_tor)
    print("Spherical Divergence", div_sph)
    print("Cylindrical Divergence", div_cyl)
    print("Toroidal Divergence", div_tor)
    print()
    print("Divergence of tensor")
    div_sphT = computeDivergenceTensor(covDer_sphT)
    div_cylT = computeDivergenceTensor(covDer_cylT)
    div_torT = computeDivergenceTensor(covDer_torT)
    print("Spherical Divergence", div_sphT)
    print("Cylindrical Divergence", div_cylT)
    print("Toroidal Divergence", div_torT)
    
    """
    Diverence of vector
    Spherical Divergence -1.0*r3(r, th, ph)*tan(ph) + Derivative(r1(r, th, ph), r) + Derivative(r2(r, th, ph), th) + Derivative(r3(r, th, ph), ph) + 2.0*r1(r, th, ph)/r
    Cylindrical Divergence Derivative(c1(r, th, z), r) + Derivative(c2(r, th, z), th) + Derivative(c3(r, th, z), z) + 1.0*c1(r, th, z)/r
    Toroidal Divergence (r*(R - r*cos(th))*(Derivative(t1(r, th, ph), r) + Derivative(t2(r, th, ph), ph)) + r*(1.0*r*t2(r, th, ph)*sin(th) + (R - r*cos(th))*Derivative(t3(r, th, ph), th) - 1.0*t1(r, th, ph)*cos(th)) + 1.0*(R - r*cos(th))*t1(r, th, ph))/(r*(R - r*cos(th)))

    Divergence of tensor
    Spherical Divergence [1.0*r*rT22*cos(ph)**2 + 1.0*r*rT33 - 1.0*rT13*tan(ph) + 2.0*rT11/r, 1.0*(-r*rT32*tan(ph) + rT12 + rT21)/r, (-r*(0.5*rT22*sin(2*ph) + 1.0*rT33*tan(ph)) + 1.0*rT13 + 1.0*rT31)/r]
    Cylindrical Divergence [1.0*cT11/r + 1.0*cT22*r, 1.0*cT12/r, 1.0*cT31/r]
    Toroidal Divergence [1.0*(r**2*tT22*(R - r*cos(th)) + r*(r*tT12*sin(th) - tT11*cos(th) - tT33*(R - r*cos(th))**2*cos(th)) + tT11*(R - r*cos(th)))/(r*(R - r*cos(th))), 1.0*(r*(r*tT22*sin(th) - tT21*cos(th)) + tT12*(R - r*cos(th)) + tT33*(R - r*cos(th))**2*sin(th))/(r*(R - r*cos(th))), 1.0*(-R*tT31 - r**2*tT23*sin(th) + r*tT13*cos(th) + r*tT31*cos(th))/(r*(-R + r*cos(th)))]
"""
    
        
     
    
    
    
    
