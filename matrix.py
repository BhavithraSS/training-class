x=[[12,7,3],
  [4,7,8],
  [5,8,2]]
y=[[1,8,6],
  [6,5,4],
  [2,3,4]]
result=[[0,0,0],
     [0,0,0],
     [0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j]=x[i][j]+y[i][j]
        for r in result:
            print(r)
