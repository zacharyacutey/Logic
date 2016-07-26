def replace(rules,string,default=''):
 _ = True
 lower=0
 result=''
 while lower < len(string):
  _ = True
  upper = len(string)
  while upper > lower:
   if string[lower:upper] in rules:
    result+=rules[string[lower:upper]]
    lower += len(string[lower:upper])
    upper = lower
    _ = False
   else:
    upper -= 1
  if _:
   result += default
   lower += 1
 return result
def sreplace(rules,string):
 _ = True
 lower=0
 result=''
 while lower < len(string):
  _ = True
  upper = len(string)
  while upper > lower:
   if string[lower:upper] in rules:
    result+=rules[string[lower:upper]]
    lower += len(string[lower:upper])
    upper = lower
    _ = False
   else:
    upper -= 1
  if _:
   result += string[lower]
   lower += 1
 return result
