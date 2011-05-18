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
        G.node[n]['activep']=True
    diffset=set(G.nodes())-set(subset)
    for n in diffset:
        G.node[n]['touched']=False
        G.node[n]['touched']=False
    ans=subs=subset
    while subs:
        temp_subs=[]
        for n in subs:
            for nbr in G.neighbors(n):
                if G.node[nbr]['touched']==False:
                    G.node[nbr]['activep']=try_touch(G[n][nbr]['prob'])
                    if G.node[nbr]['activep']:
                        temp_subs.append(nbr)
                    G.node[nbr]['touched']=True
        subs=temp_subs                    
        ans=ans+subs    
    return ans

def try_touch(prob):
    if random.random()<prob:
        return True
    else:
        return False

