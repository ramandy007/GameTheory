#utlity function callculation for a packet at time t.
def utility(packets,totalpackatj,t,residenergy,k,d):
    owngain=ogcalc(packets,totalpackatj)
    cost=costcaln(residenergy,k,d)
    util=owngain-cost
    return util

def costcaln(residenergy,k,d):
    energy=calcenergy(k,d)
    cost=residenergy/energy
    return energy

def ogcalc(packets,totalpacketatj):
    owngain=packets/totalpacketatj
    return owngain

def calcenergy(k,d):
    energy=k*d*d
    return energy




