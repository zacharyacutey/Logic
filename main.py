def double(p):
  if type(p) != list:
    return p
  else:
    if type(p[0]) == list and len(p) == 1:
      if len(p[0]) == 1:
        return double(p[0][0])
  return p
#Changes a ~~p => p in one item


def remove_double(arg):
  arg = double(arg)
  if type(arg)!=list:
    return arg
  for i in range(len(arg)):
    if type(arg[i]) == list:
      arg[i] = remove_double(arg[i])
  return arg
truths = []

def define_truth(p_):
  p = remove_double(p_)
  if p in truths:
    return False
  else:
    truths.append(p)
    return True

def contrapositive(p):
  return remove_double([[p[1]],[p[0]]])

def add_contrapositives():
  for i in truths:
    if not ( contrapositive(i) in truths ):
      define_truth(contrapositive(i))
      return True
  return False

def add_transitives():
  for i in truths:
    for j in truths:
      if i != j and len(i) == 2 and len(j) == 2 and type(i) == list and type(j) == list:
        if i[1] == j[0]:
          if not ([i[0],j[1]] in truths):
            define_truth([i[0],j[1]])
            return None
            
  return False

def add_detachments():
  for i in truths:
    for j in truths:
      if (len(i) == 1 or type(i) == str) and len(j) == 2 and type(j) == list:
        if i == j[0]:
          if not (j[1] in truths):
            define_truth(j[1])
            return True
  return False

def deduce():
  if add_contrapositives():
    deduce()
    return None
  if add_transitives():
    deduce()
    return None
  if add_detachments():
    deduce()
    return None
  return None
