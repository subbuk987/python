vertices = int(input("Enter the Number of vertices:"))
noOfEdges= int(input("Enter the number of edges:"))
test = {}
for i in range(vertices):
  test[i+1] = 0;
edges = []
for i in range(noOfEdges):
  print(f"Enter edge {i+1}")
  temp = list(map(int,input().split()))
  temp.sort()
  edges.append(temp)
edges.sort()
flag = True
count=0
while(flag):
  for i in range(1,noOfEdges+1):
    if (test[edges[i-1][0]]==test[edges[i-1][1]]):
      test[edges[i-1][1]]+=1
  for i in range(1,noOfEdges+1):
    if (test[edges[i-1][0]]!=test[edges[i-1][1]]):
      count+=1
  if count==noOfEdges:
    flag=False

print(test)
