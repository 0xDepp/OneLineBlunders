[(lambda _,d,m:print((lambda v:v if[(d.__setitem__(v[0],d[v[0]]+1),v.__setitem__(0,v[0]+x),v.__setitem__(1,v[1]+d[v[0]-47])if v[0]-47 in d else 0)for x in m]else 0)([0,0])[1]))((input(),input()),(__import__('collections')).defaultdict(lambda:0),map(int,input().split()))for _ in range(int(input()))]