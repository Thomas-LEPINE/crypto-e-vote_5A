def EuclideEtendu(a, b):
    (r, u, v, rp, up, vp) = (a, 1, 0, b, 0, 1)
    q = 0
    while (rp != 0):
        q = (r // rp)
        (r, u, v, rp, up, vp) = (rp, up, vp, r-q*rp, u-q*up, v-q*vp)
    return (r, u, v)