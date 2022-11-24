def my_max(p):
  return max(p)

def my_min(p):
  return min(p)

def my_mean(p):
  return sum(p)/len(p)

def my_median(p):
  import statistics
  return statistics.median(p)
  
def my_mode(p):
  try:
    import statistics
    return statistics.mode(p)
  except:
    return "Нет озназначного решения"

def my_square(p):
    s = 0
    for i in p:
      s += (i - my_mean(p))**2
    return round((s/ (len(p)-1))**0.5, 2)

def my_simmetric(p):
    raznost = abs(my_median(p) - my_mean(p))
    if raznost <= 3* ((my_square(p)/len(p))**0.5):
      return True
    else:
      return False

def razmax(p):
    return max(p) - min(p)

def qw(p):
    import pandas as pd
    df = pd.Series(p)
    qwanta = df.quantile([.25, .5, .75])
    z=[]
    for i in qwanta:
      z.append(i)
    return z

def qw_razmax(p):
    q = qw(p)
    s=[]
    for i in p:
        if i > q[0] and i <  q[2]:
          s.append(i)
    return s