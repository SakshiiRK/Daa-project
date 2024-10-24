import heapq
import matplotlib.pyplot as plt
import numpy as np

def prims_algorithm(V, adj):
    pq = []  
    heapq.heappush(pq, (0, 0))  
    key = [float('inf')] * V
    key[0] = 0
    in_mst = [False] * V
    result = 0
    
    while pq:
        weight, u = heapq.heappop(pq)
        
        if in_mst[u]:
            continue
        in_mst[u] = True
        result += weight
        
        
        for v, wt in adj[u]:
            if not in_mst[v] and wt < key[v]:
                key[v] = wt
                heapq.heappush(pq, (key[v], v))
    
    return result


V = int(input("Enter the number of vertices: "))
E = int(input("Enter the number of edges: "))


adj = [[] for _ in range(V)]


print("Enter the edges in the format: vertex1 vertex2 weight")
for _ in range(E):
    u, v, wt = map(int, input().split())
    adj[u].append((v, wt))
    adj[v].append((u, wt))  


result = prims_algorithm(V, adj)
print(f"Total weight of the Minimum Spanning Tree (MST): {result}")


V_values = np.arange(1, 101)  
E_values = np.linspace(1, 1000, 100)  


time_V2 = V_values**2


time_E_logV = E_values * np.log(V_values)


plt.figure(figsize=(10, 6))
plt.plot(V_values, time_V2, label="O(V^2) - Original Prim's", color="red")
plt.plot(V_values, time_E_logV, label="O(E log V) - Optimized Prim's", color="blue")
plt.title("Time Complexity Comparison of Prim's Algorithm")
plt.xlabel("Number of Vertices (V)")
plt.ylabel("Time Complexity")
plt.legend()
plt.grid(True)
plt.show()
