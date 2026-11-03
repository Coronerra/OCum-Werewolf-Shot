# Builds OCum_WerewolfUrethra.esp (ESL): werewolf-only urethra node on ABC's WWD 9 tip bone.
import struct,sys
SRC=sys.argv[1] if len(sys.argv)>1 else 'input/OCum.esp'
d=open(SRC,'rb').read()
def recs(b,o,end):
    while o<end:
        t=b[o:o+4];sz=struct.unpack_from('<I',b,o+4)[0]
        if t==b'GRUP': yield from recs(b,o+24,o+sz); o+=sz
        else: yield t,b[o:o+24],b[o+24:o+24+sz]; o+=24+sz
def subs(p):
    o=0;r=[]
    while o<len(p):
        t=p[o:o+4];s=struct.unpack_from('<H',p,o+4)[0];r.append([t,p[o+6:o+6+s]]);o+=6+s
    return r
def join(ss): return b''.join(t+struct.pack('<H',len(v))+v for t,v in ss)
hdr=struct.unpack_from('<I',d,4)[0]
R={}
for t,h,p in recs(d,24+hdr,len(d)):
    fid=struct.unpack_from('<I',h,12)[0]
    if fid&0xFFFFFF in(0x818,0x819): R[fid&0xFFFFFF]=(t,h,p)
WW=0x000CDD84; NEWID=0x04000800   # masters: Skyrim, Dawnguard, OStim, OCum (same as OCum.esp) -> self = 04
def rec(t,fid,data,flags=0):
    h=bytearray(t+struct.pack('<IIIIHH',len(data),flags,fid,0,44,0)); return bytes(h)+data
# overridden ARMA 0x819: drop WerewolfBeastRace
t,h,p=R[0x819]; ss=subs(p)
ss=[x for x in ss if not(x[0]==b'MODL' and struct.unpack('<I',x[1])[0]==WW)]
arma_old=rec(b'ARMA',0x03000819,join(ss))
# new ARMA for werewolf
ss=subs(p); new=[]
for k,v in ss:
    if k==b'EDID': v=b'OCumUrethraNodeWerewolfAA\0'
    if k in(b'MOD2',b'MOD3'): v=b'OCum\\UrethraNodeWerewolf.nif\0'
    if k==b'RNAM': v=struct.pack('<I',WW)
    if k==b'MODL': continue
    if k in(b'MO2T',b'MO3T',b'MO2S',b'MO3S'): continue
    new.append([k,v])
# put additional race list right after MOD3 position: append is fine for ARMA (MODL follows models); place before NAM0/NAM1? keep order: insert after last MOD*
idx=max(i for i,(k,_) in enumerate(new) if k.startswith(b'MOD'))+1
new.insert(idx,[b'MODL',struct.pack('<I',WW)])
arma_new=rec(b'ARMA',NEWID,join(new))
# ARMO 0x818: werewolf ARMA first
t,h,p=R[0x818]; ss=subs(p); out=[]; done=False
for k,v in ss:
    if k==b'MODL' and not done: out.append([b'MODL',struct.pack('<I',NEWID)]); done=True
    out.append([k,v])
armo=rec(b'ARMO',0x03000818,join(out))
def grup(lbl,body): return b'GRUP'+struct.pack('<I',24+len(body))+lbl+struct.pack('<IIHH',0,0,44,0)+body
masters=[b'Skyrim.esm',b'Dawnguard.esm',b'OStim.esp',b'OCum.esp']
th=[[b'HEDR',struct.pack('<fII',1.71,3,0x801)],[b'CNAM',b'That Guy (Coronerra)\0'],[b'SNAM',b'Werewolf OCum shot: attaches OCum\'s Urethra node to the ABC werewolf tip bone (WWD 9).\0']]
for m in masters: th+= [[b'MAST',m+b'\0'],[b'DATA',b'\0'*8]]
tes4=b'TES4'+struct.pack('<IIIIHH',len(join(th)),0x200,0,0,44,0)+join(th)
out=tes4+grup(b'ARMO',armo)+grup(b'ARMA',arma_old+arma_new)
open('build/pkg/OCum_WerewolfUrethra.esp','wb').write(out); print(len(out))
