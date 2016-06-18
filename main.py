def double(p):
  if type(p) != list:
    return p
  else:
    if type(p[0]) == list:
      if type(p[0][0]) == list:
        return double(p[0][0])
#Changes a ~~p => p in one item

def remove_double(p):
  pass
#remove_double should remove all [[p]]'s and replace them with p's
"""
TODO: FIX THIS remove_double
I CAN'T GET IT TO WORK!!!!!
SCREW YOU PASS BY VALUE!
"""
