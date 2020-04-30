"""
12 -> μCc
13 -> μCd
14 -> μDc
15 -> μDd

"""
#μCc
def mue_Cc(mue, z):
    val = ( mue*((1-z)**2) ) / ( (mue*(1-z))+(z*(1-mue)) )
    return val

#μCd
def mue_Cd(mue,z):
    val = ( mue*(1-z)*z ) / ( (mue*z)+((1-z)*(1-mue)) )
    return val

#μDc
def mue_Dc(mue, z):
    val = ( mue*(1-z)*z ) / ( (mue*(1-z))+(z*(1-mue)) )
    return val

#μDd
def mue_Dd(mue,z):
    val = ( mue*(z**2) ) / ( (mue*z)+((1-z)*(1-mue)) )
    return val