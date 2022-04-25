#program to compute coordinates
import math

#inputs
E1 = input("Enter easting of station 1: ")
N1 = input("Enter northing of station 1: ")
st, dist, wcb = eval(input("Enter station name,dist and bearing to next/new station: "))

#function to convert DMS to Rads(0,0)
def dms2rad(dms):
    b=dms.split()
    degree=b(0)
    minute=b(1)
    seconds=b(2)
    # dec_degree = float(degree) + float(minute) / 60 = float(second)/3600
    dec_degree = float(degree) + float(minute) / 60

    return math.radians(dec_degree)

# Function to compute coordinates
def dEdN(d, b):
    wcbRads = dms2rad(b)
    DE = d * math.sin(wcbRads)
    DN = d * math.cos(wcbRads)
    return DE,DN
de, dn = dEdN(dist,wcb)
E2 = E1 + de
N2 = N1 + dn
print("{0}\t{1:0.3f}\t{2:0.3f}")
format(E2,N2)