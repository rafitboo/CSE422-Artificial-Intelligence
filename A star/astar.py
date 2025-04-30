import heapq
import math
def astar(graph,heuristic,source,destination):
    distance={}
    parent={}
    visited=[]

    for i in graph.keys():
        distance[i]=math.inf
        parent[i]=None
    distance[source]=0

    q=[[heuristic[source],source]]

    while q:
        w1,n1=heapq.heappop(q)
        visited.append(n1)
        if n1==destination:
            break
        adj=graph[n1]
        for n2,w2 in adj.items():
            distance[n2]=distance[n1]+w2
            if n2 not in visited:
                heapq.heappush(q,[distance[n2]+heuristic[n2],n2])
                parent[n2]=n1

    total_distance=distance[destination]

    reverse_path=[]
    reverse_path.append(destination)
    
    while parent[destination]!=None:
        node=parent[destination]
        reverse_path.append(node)
        destination=node

    path_list=reverse_path[::-1]
    return path_list,total_distance



f1=open(r"A star\input.txt","r")
f2=open(r"A star\output.txt","w")

heuristic={}
graph={}

for i in range(20):
    var=f1.readline().split(" ")
    heuristic[var[0]]=int(var[1])
    temp={}
    for j in range(2,len(var),2):
        temp[var[j]]=int(var[j+1])
    graph[var[0]]=temp

source,destination="Arad","Bucharest"
path_list, total_distance=astar(graph,heuristic,source,destination)  

if path_list==[] and total_distance==math.inf:
    print("No Path Found")
    f2.write("No Path Found")
else:
    path="Path: "
    path+=" -> ".join(path_list)
    f2.write(str(path) + "\n")
    print(path)
    f2.write("Total Distance: "+str(total_distance)+" km")
    print("Total Distance: "+str(total_distance)+" km")


f1.close()
f2.close()











