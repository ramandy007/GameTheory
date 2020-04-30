def payoffdiff(VCC,VCD,VDC,VDD,prob):
    payoffdiff=prob*(VCC-VDC)-(1-prob)(VDD-VCD)
    return payoffdiff

def theta(beta,alpha,delta,zed):
    theta=((-beta)/(alpha-beta))((1-delta*((1-zed)^2))/delta*(1-2*zed))
    return theta


def seqeqpoint(zed):
    phi=((1-(3*zed)-(zed*zed))/(1-2*zed))
    return phi

print("Enter Vcc value:")
VCC=int(input())
print("Enter Vcd value:")
VCD=int(input())
print("Enter Vdc value:")
VDC=int(input())
print("Enter Vdd value:")
VDD=int(input())
print("Enter prob value:")
prob=int(input())
print("Enter beta value:")
beta=int(input())
print("Enter alpha value:")
alpha=int(input())
print("Enter delta value:")
delta=int(input())
print("Enter zed value:")
zed=int(input())
payoffdifference = payoffdiff(VCC,VCD,VDC,VDD,prob)
Probabilityfactor = theta(beta,alpha,delta,zed)
SequentialEquilibriumPoint = seqeqpoint(zed)
print(payoffdifference)
print(Probabilityfactor)
print(SequentialEquilibriumPoint)

