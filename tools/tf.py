import struct,numpy as np
from nif import Nif
def tr(n,k):
    b=n.blocks[k]; i=4; ne,=struct.unpack_from('<I',b,i); i+=4+4*ne+4+4
    t=np.array(struct.unpack_from('<3f',b,i)); R=np.array(struct.unpack_from('<9f',b,i+12)).reshape(3,3); sc,=struct.unpack_from('<f',b,i+48)
    return t,R,sc,i
def world(path):
    n=Nif(path); par={}; W={}
    for k in range(len(n.blocks)):
        if 'Node' in n.btype(k) or n.btype(k)=='BSFadeNode':
            _,ch=n.node_children(k)
            for c in ch:
                if c>=0: par[c]=k
    def w(k):
        if k in W: return W[k]
        t,R,s,_=tr(n,k)
        if k in par:
            pt,pR,ps=w(par[k]); W[k]=(pt+ps*(pR@t), pR@R, ps*s)   # nif: R stored row-major, child-to-parent with column vec? check
        else: W[k]=(t,R,s)
        return W[k]
    return n,par,w
