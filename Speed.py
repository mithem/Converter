def kph(ms):
    return ms * 3.6

def mph(ms):
    return ms * 2.2369362920544

def knots(ms):
    return ms * 1.9438444924574

def minPkm(ms): # minutes per kilometre
    return ms * (100 / 6)

def c(ms): # speed of light
  return ms / 299792458

def speedOfLight(ms):
  return c(ms)

def mach(ms):
  return ms / 340

def speedOfSound(ms):
  return mach(ms)