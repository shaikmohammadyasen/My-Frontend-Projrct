v,e=map(int,input().split())
adj=[[0 for i in range (v)]for j in range(v)]
for i in range(e):
  a,b=map(int,input().split())
  adj[a][b]=1
  adj[b][a]=1
  print(adj)
