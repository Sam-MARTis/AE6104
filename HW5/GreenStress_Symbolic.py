from sympy import symbols, Function, Matrix, cos, sin, sqrt, diff, simplify


def findGreenStrainTensor(ref_initial, ref_final, rvec_deformed, rvec_initial):

    g_cov_convected = [[0 for _ in range(3)] for __ in range(3)]
    G_cov_convected = [[0 for _ in range(3)] for __ in range(3)]

    for i in range(3):
        for j in range(3):
            g_cov_convected[i][j] = diff(rvec_deformed[j], ref_initial[i])
            G_cov_convected[i][j] = diff(rvec_initial[j], ref_initial[i])

    g_metric_covcov = [[0 for _ in range(3)] for __ in range(3)]
    G_metric_covcov = [[0 for _ in range(3)] for __ in range(3)]
    for i in range(3):
        for j in range(3):
            for m in range(3):
                g_metric_covcov[i][j] += g_cov_convected[i][m] * g_cov_convected[j][m]
                G_metric_covcov[i][j] += G_cov_convected[i][m] * G_cov_convected[j][m]
            g_metric_covcov[i][j] = simplify(g_metric_covcov[i][j])
            G_metric_covcov[i][j] = simplify(G_metric_covcov[i][j])


    E_actual = [[0 for _ in range(3)] for __ in range(3)]
    for i in range(3):
        for j in range(3):
            E_actual[i][j] = simplify((g_metric_covcov[i][j] - G_metric_covcov[i][j])/2)

    G_metric_concon = Matrix(G_metric_covcov).inv()

    E_physcial = [[0 for _ in range(3)] for __ in range(3)]
    for i in range(3):
        for j in range(3):
            E_physcial[i][j] = simplify(E_actual[i][j]*sqrt(G_metric_concon[i, i]) * sqrt(G_metric_concon[j, j]))

    print('\nE_actual')
    for i in range(3):
        print(E_actual[i])
    print('\n\nE_physcial')
    for i in range(3):
        print(E_physcial[i])




def Cylinder():
    """
    The cylinder is pulled/compressed in the vertical direction while being twisted and this results in uniform(with respect to theta and z) radial defomation
    """
    TH = symbols('Θ')
    PH = symbols('Φ')
    R = symbols('R')
    X3 = symbols('X3')

    f = Function('f')
    l = symbols('λ')

    r = f(R)
    th = TH + PH*X3
    x3 = l*X3
    ref_initial = [R, TH, X3]
    ref_final = [r, th, x3]
    rvec_deformed = Matrix([r*cos(th), r*sin(th), x3])
    rvec_initial = Matrix([R*cos(TH), R*sin(TH), X3])
    findGreenStrainTensor(ref_initial, ref_final, rvec_deformed, rvec_initial)

def Sphere():
    """
    The sphere is being expanded/compressed radially in a uniform manner. Ex: Balloon
    """
    R = symbols('R')
    TH = symbols('Θ')
    PH = symbols('Φ')
    f = Function('f')
    
    r = f(R)
    th = TH
    ph = PH
    
    ref_initial = [R, TH, PH]
    ref_final = [r, th, ph]
    
    rvec_deformed = Matrix([r*cos(th)*cos(ph), r*cos(th)*sin(ph), r*sin(th)])
    rvec_initial = Matrix([R*cos(TH)*cos(PH), R*cos(TH)*sin(PH), R*sin(TH)])
    findGreenStrainTensor(ref_initial, ref_final, rvec_deformed, rvec_initial)
    
def Toroid():
    """
    The circular cross section of the torois is being deformed. 
    There is no twist the phi angle is unchanged.
    Also there is no movement of the midpoint of the cross section as C is constant. 
    Can be thought of as a 2D deformation at every phi of a circle in the x-y plane with its origin being fixed.
    """
    R = symbols('R')
    TH = symbols('Θ')
    PH = symbols('Φ')
    C = symbols('C')
    f = Function('f')
    g = Function('g')
    
    r = f(R, TH)
    th = TH
    ph = g(R, TH)
    
    ref_initial = [R, TH, PH]
    ref_final = [r, th, ph]
    
    rvec_deformed = Matrix([(C - r*cos(th))*cos(ph), (C - r*cos(th))*sin(ph), r*sin(th)])
    rvec_initial = Matrix([(C - R*cos(TH))*cos(PH), (C - R*cos(TH))*sin(PH), R*sin(TH)])
    
    findGreenStrainTensor(ref_initial, ref_final, rvec_deformed, rvec_initial)
    
    
    
if __name__ == "__main__":
    print("\033c")
    print("Spherical strain tensor E")
    Sphere()
    print("\n\n\n\nCylindrical strain tensor E")
    Cylinder()
    print("\n\n\n\nToroidal strain tensor E")
    Toroid()
    








