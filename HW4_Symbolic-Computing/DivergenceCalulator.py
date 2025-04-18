from CurvilinearObjectsCalculator import rvec_cyl, rvec_sph, rvec_tor, christoffelSecondKind_cyl, christoffelSecondKind_sph, christoffelSecondKind_tor, r_cyl, th_cyl, z_cyl,  r_sph, th_sph, ph_sph,  r_tor, ph_sph, R, th_tor
from sympy import *

# print()
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

if __name__ == "__main__":
    covDer_sph = covariantDerivativeVector(rvec_sph, christoffelSecondKind_sph, r_sph, th_sph, ph_sph)
    covDer_cyl = covariantDerivativeVector(rvec_cyl, christoffelSecondKind_cyl, r_cyl, th_cyl, z_cyl)
    covDer_tor = covariantDerivativeVector(rvec_tor, christoffelSecondKind_tor, r_tor, ph_sph, th_tor)


    for i in covDer_sph:
        print(i)
    print()
    for i in covDer_cyl:
        print(i)
    print()
    for i in covDer_tor:
        print(i)

    """
    [cos(ph)*cos(th), r*(1.0*r*cos(ph)**2 - 1.0)*sin(th)*cos(ph), 1.0*r*(r - cos(th))*sin(ph)]
    [0, -1.0*r*sin(ph)*tan(ph) + 1.0*r*cos(ph)*cos(th) + 1.0*cos(ph)*cos(th), 0]
    [0, -0.5*r*sin(2*ph)*sin(th)*cos(ph), 1.0*(r + cos(th))*cos(ph)]

    [cos(th), r*(1.0*r - 1)*sin(th), 0]
    [0, (r + 1.0)*cos(th), 0]
    [0, 0, 1]

    [-cos(ph)*cos(th), (R - r*cos(th))*(1.0*r - 1)*sin(ph), r*(-1.0*(R - r*cos(th))*cos(th) + cos(ph))*sin(th)]
    [-1.0*R*sin(ph)/r, (R - r*cos(th))*(r + 1.0)*cos(ph)/r, (r*sin(ph) + 1.0*(R - r*cos(th))*sin(th))*sin(th)]
    [R*sin(th)/(R - r*cos(th)), 1.0*r**2*sin(th)**2/(-R + r*cos(th)), 1.0*r*sin(ph)*sin(th) + 1.0*r*cos(th) - 1.0*cos(ph)*cos(th)]
    """
    
    
    
