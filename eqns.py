def mue_cd(mue, z):

    val=(mue*(1-z)*(1-z))/(mue*(1-z)+z*(1-mue))
    return val


def mue_dc(mue, z):

    val = (mue*(1 - z) *z)/ (mue*(1 - z) + z*(1 - mue))
    return val
