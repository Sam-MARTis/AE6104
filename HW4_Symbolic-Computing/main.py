from sympy import *
import numpy as np
init_printing()
r = symbols('r')
th = symbols('th')
ph = symbols('ph')

u = [r, th, ph]
# x, y, z = r*cos(ph)*cos(th),  r*cos(ph)*sin(th), r*sin(ph)
def fx1(u1, u2, u3):
    return u1*cos(u3)*cos(u2)
def fx2(u1, u2, u3):
    return u1*cos(u3)*sin(u2)
def fx3(u1, u2, u3):
    return u1*sin(u3)

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

rvec, gCovCov, gConCon, christoffelFirstKind, christoffelSecondKind = getFeaturesOfCoordinates(fx1, fx2, fx3, r, th, ph)

print(latex(christoffelFirstKind))



a1 = symbols('a1')
a2 = symbols('a2')
a3 = symbols('a3')

a = [a1, a2, a3]
amiCovDiff = [[0 for _ in range(3)] for __ in range(3)]

for m in range(3):
    for i in range(3):
        a[m][i] = diff(a[m], u[i])
        for k in range(3):
            amiCovDiff[m][i] += a[k]*christoffelFirstKind[k][i][m]




# Tij = [[0 for _ in range(3)] for __ in range(3)]
# TijDiff = [[[0 for _ in range(3)] for __ in range(3)] for __ in range(3)]
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             TijDiff