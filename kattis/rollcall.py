(lambda n:(lambda v:(n.sort(key=lambda x:x[0]),n.sort(key=lambda x:x[1]),[print(f"{f} {l}"if f in v[1]else f)for f,l in n]))((lambda v:v if[(lambda:(v[1].add(f)if f in v[0]else 0,v[0].add(f)))()for f,l in n]else 0)([set(),set()])))([ln.split()for ln in(__import__('sys')).stdin.readlines()])