from sympy import *
import numpy as np
init_printing()


# u = [r, th, ph]
# x, y, z = r*cos(ph)*cos(th),  r*cos(ph)*sin(th), r*sin(ph)

def getFeaturesOfCoordinates(fx1, fx2, fx3, u1, u2, u3):
    x = fx1(u1, u2, u3)
    y = fx2(u1, u2, u3)
    z = fx3(u1, u2, u3)

    uvec = [u1, u2, u3]
    rvec= [x, y, z]
    gcov = [[0 for _ in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            gcov[i][j] = diff(rvec[j], uvec[i])
    gCovCov = [[0 for i in range(3)] for j in range(3)]

    for i in range(3):
        for j in range(3):
            for m in range(3):
                gCovCov[i][j] += simplify(gcov[i][m]*gcov[j][m])
            gCovCov[i][j] = simplify(gCovCov[i][j])

    gCovCov = gCovCov
    gConCon =np.reshape(Matrix(gCovCov).inv(), shape=(3, 3))

    # print(np.reshape(gConCon, shape=(3, 3)))

    gCovCovDerivatives = [[[0 for _ in range(3)] for __ in range(3)] for ____ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                gCovCovDerivatives[i][j][k] = simplify(diff(gCovCov[i][j], uvec[k]))



    christoffelFirstKind = [[[0 for _ in range(3)] for __ in range(3)] for ____ in range(3)]
    christoffelSecondKind = [[[0 for _ in range(3)] for __ in range(3)] for ____ in range(3)]

    for i in range(3):
        for j in range(3):
            for k in range(3):
                christoffelFirstKind[i][j][k] = simplify((1/2) * (-gCovCovDerivatives[i][j][k] + gCovCovDerivatives[j][k][i] + gCovCovDerivatives[k][i][j]) )
    for m in range(3):
        for j in range(3):
            for k in range(3):
                for i in range(3):
                    christoffelSecondKind[j][k][m] += gConCon[m][i]*christoffelFirstKind[i][j][k]
                christoffelSecondKind[j][k][m] = simplify(christoffelSecondKind[j][k][m])

    # print(christoffelFirstKind[1][1][2])
    # print(christoffelFirstKind)

    return rvec, gCovCov, gConCon, christoffelFirstKind, christoffelSecondKind



# For spherial coordinates
r_sph = symbols('r')
th_sph = symbols('th')
ph_sph = symbols('ph')


def fx1_sph(r, theta, phi):
    return r*cos(phi)*cos(theta)
def fx2_sph(r, theta, phi):
    return r*cos(phi)*sin(theta)
def fx3_sph(r, theta, phi):
    return r*sin(phi)


rvec_sph, gCovCov_sph, gConCon_sph, christoffelFirstKind_sph, christoffelSecondKind_sph = getFeaturesOfCoordinates(fx1_sph, fx2_sph, fx3_sph, r_sph, th_sph, ph_sph)


# For cylindrical coordinates
z_cyl = symbols('z')
r_cyl = symbols('r')
th_cyl = symbols('th')
def fx1_cyl(r, theta, z):
    return r*cos(theta)
def fx2_cyl(r, theta, z):
    return r*sin(theta)
def fx3_cyl(r, theta, z):
    return z

rvec_cyl, gCovCov_cyl, gConCon_cyl, christoffelFirstKind_cyl, christoffelSecondKind_cyl = getFeaturesOfCoordinates(fx1_cyl, fx2_cyl, fx3_cyl, r_cyl, th_cyl, z_cyl)


# Toroidal coordinates
r_tor = symbols('r')
th_tor = symbols('th')
ph_tor = symbols('ph')
R = symbols('R')
def fx1_tor(r, theta, phi):
    return (R - r*cos(theta))*cos(phi)
def fx2_tor(r, theta, phi):
    return (R - r*cos(theta))*sin(phi)
def fx3_tor(r, theta, phi):
    return r*sin(theta)

rvec_tor, gCovCov_tor, gConCon_tor, christoffelFirstKind_tor, christoffelSecondKind_tor = getFeaturesOfCoordinates(fx1_tor, fx2_tor, fx3_tor, r_tor, th_tor, ph_tor)

print(gCovCov_sph[1][1])
print(gCovCov_cyl[1][1])
print(gCovCov_tor[1][1])



# print(latex(christoffelFirstKind))
# print(christoffelFirstKind)



# a1 = symbols('a1')
# a2 = symbols('a2')
# a3 = symbols('a3')

# a = [a1, a2, a3]
# amiCovDiff = [[0 for _ in range(3)] for __ in range(3)]

# for m in range(3):
#     for i in range(3):
#         a[m][i] = diff(a[m], u[i])
#         for k in range(3):
#             amiCovDiff[m][i] += a[k]*christoffelFirstKind[k][i][m]




# Tij = [[0 for _ in range(3)] for __ in range(3)]
# TijDiff = [[[0 for _ in range(3)] for __ in range(3)] for __ in range(3)]
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             TijDiff