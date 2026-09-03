class Solution:
    def graphColoring(self, v, edges, m):
        
        graph = []
        for i in range(v):
            graph.append([])
        
        for v1,v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        colours = [0]*v
        
        def isSafe(vert,c):
            for i in graph[vert]:
                if colours[i] == c:
                    return False
            return True
        
        def backtrack(vertex):
            
            for i in range(1,m+1):
                if vertex == v:
                    return True
                
                if isSafe(vertex,i):
                    colours[vertex] = i
                
                    if backtrack(vertex+1):
                        return True
                    
                    colours[vertex] = 0
                    
            return False
        
        return backtrack(0)
        
                    
                    
                    
                
            
            
        