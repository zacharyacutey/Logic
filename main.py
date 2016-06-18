def double(p):
  if len(p) == 1 and type(p) == list:
    if len(p[0]) == 1 and type(p[0]) == list:
      return p[0][0]
  return p

def is_dead(p):
  s = True
  for i in p:
    if type(i) == list:
      return True
  return False
  
def remove_double(p):
  if type(i) != list:
    return
  p = double(p)
  for i in range(len(p)):
    remove_double(p[i])
