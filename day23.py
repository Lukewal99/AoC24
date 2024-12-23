import collections
# i did some googling and found this funky algorithm on wikipedia
def bron_kerbosch(R,P,X,G,C):
    R = set(R)
    P = set(P)
    X = set(X)

    if len(P) == 0 and len(X) == 0:
        C.append(sorted(R))
        return
    
    for v in P.union(set([])):
        bron_kerbosch(R.union(set([v])), P.intersection(G[v]), X.intersection(G[v]), G, C)
        P.remove(v)
        X.add(v)

file = open("PuzzleInput.txt", "r").read().split("\n")
sum = 0
part = 2
graph = {}
global C

if part == 1:
    for connection in file:
        pcs = connection.split("-")
        if pcs[0][0] == 't':
            if pcs[0] in graph.keys():
                graph[pcs[0]].append(pcs[1])
            else:
                graph[pcs[0]] = [pcs[1]]
        
        elif pcs[1][0] == 't':
            if pcs[1] in graph.keys():
                graph[pcs[1]].append(pcs[0])
            else:
                graph[pcs[1]] = [pcs[0]]

    for value in graph.values():
        for i in range(0,len(value)):
            for j in range(i,len(value)):
                if value[i]+"-"+value[j] in file or value[j]+"-"+value[i] in file:
                    sum+=1
    print(sum)

elif part == 2:
    graph = collections.defaultdict(set)
    for connection in file:
        pcs = connection.split("-")
        graph[pcs[0]].add(pcs[1])
        graph[pcs[1]].add(pcs[0])

    C = []
    bron_kerbosch(set([]),graph.keys(),set([]),graph,C)
    maxLen = 0
    maxClique = []
    for c in sorted(C):
        if len(c) > maxLen:
            maxClique = c
            maxLen = len(c)
    print(str(maxClique).replace("'","").replace("[","").replace("]","").replace(" ",""))