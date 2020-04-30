##simulation A

import Bcoop as bp
def case1():
    """ Player 1 has both packets C and D1 to send and it believes that the opponent also had these two packets in
    previous round """
    CC = (alphac - betac, alphac + betac)
    CD1 = (-betac, alphad + alphac - betad)
    D1C = (alphad + alphac - betad, -betac)
    D1D1 = (alphad - betad, alphad - betad)
    simulationResult = [[CC, CD1], [D1C, D1D1]]
    for rows in simulationResult:
        print(rows)
    print()


def case2():
    """ Player 1 has both packets C and D1 to send and it believes that the opponent had only
 cooperative packet in previous round"""
    CC = (alphac - betac, alphac - betac)
    CD2 = (-betac, alphac)
    D1C = (alphad + alphac - betad, -betac)
    D1D2 = (alphad - betad, 0)
    simulationResult = [[CC, CD2], [D1C, D1D2]]
    for rows in simulationResult:
        print(rows)
    print()


def case3():
    """Player 1 has only cooperative packet C to transmit where as it believes that the opponent had
both packets in previous round"""
    CC = (alphac - betac, alphac - betac)
    CD1 = (-betac, alphad + alphac - betad)
    D2C = (alphac, -betac)
    D2D1 = (0, alphad - betad)
    simulationResult = [[CC, CD1], [D2C, D2D1]]
    for rows in simulationResult:
        print(rows)
    print()


def case4():
    """Player 1 has only cooperative packet C to transmit and it believes that the opponent also had
only cooperative packet in previous round"""
    CC = (alphac - betac, alphac - betac)
    CD2 = (-betac, alphac)
    D2C = (alphac, -betac)
    D2D2 = (0, 0)
    simulationResult = [[CC, CD2], [D2C, D2D2]]
    for rows in simulationResult:
        print(rows)
    print()


if __name__ == '__main__':
    alphac = float(input("enter alpha_c : "))
    alphad = float(input("enter alpha_d : "))
    betac = float(input("beta_c : "))
    betad = float(input("beta_d : "))

    case1()
    case2()
    case3()
    case4()
    pck=int(input("Packets From I-J At Time t-1"))
    totalpck = int(input("Packets At Node J"))
    t = int(input("Time T"))
    residener = int(input("Residual Energy:"))
    k = int(input("Scaling Parameter:"))
    d = int(input("Distance Between Node I And J:"))

    print("Final Utility Is :",bp.utility(pck,totalpck,t,residener,k,d))