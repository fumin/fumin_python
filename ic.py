import networkx as nx
import random

def testg():
    G=nx.DiGraph()
    G.add_nodes_from([1,2,3,4,5,6])
    G.add_edges_from([(1,2),(1,3),(2,3),(2,4),(2,5),(2,6)])
    prob_degree(G)
    return G

def prob_degree(G):
    for n,nbrs in G.adjacency_iter():
        for nbr, eattr in nbrs.items():
            eattr['prob']=1.0/G.out_degree(n)

def iter(G, subset):
    for n in subset:
        G.node[n]['touched']=True
    diffset=set(G.nodes())-set(subset)
    for n in diffset:
        G.node[n]['touched']=False
    ans=subs=subset
    while subs:
        temp_subs=[]
        for n in subs:
            for nbr in G.neighbors(n):
                if G.node[nbr]['touched']==False:
                    if try_touch(G[n][nbr]['prob']):
                        temp_subs.append(nbr)
                    G.node[nbr]['touched']=True
        subs=temp_subs                    
        ans=ans+subs    
    return ans

def try_touch(prob):
    return True if random.random()<prob else False


