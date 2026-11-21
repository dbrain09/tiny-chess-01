import json,os,urllib.request as r,base64,struct,zlib
E=os.environ.get("MAKEFUN_ENV_URL")
V=[0,100,320,330,500,900,0]
H='0011240'
W=[[-33,-31,-18,-14,14,18,31,33],[-17,-15,15,17],[-16,-1,1,16]]
D=struct.unpack("384b",zlib.decompress(base64.b85decode("c-n=Js}2J(3<Q^$n1q;=1Rw5~^ve$i8wZ<&bbawj1ywuJDwZcN1AwSbS-}b>q7PN;Pl7^;kxmYh?nTm_!+lJMi#A6y7Y5qcyIgs&r`)6WdixoK_XI>3tw{FLm6wpq?^Hea(Vr~tS-F18zMqo|f-^4ui_f=;ru*luE6n)+NjR#Haen6Xg!6}WkACd1W-r|vYtD;(")))
def T(p,b):
 q=r.Request(E+p,json.dumps(b).encode(),{"content-type":"application/json"})
 try:return json.load(r.urlopen(q))
 except:return {}
class B:
 def __init__(s,f):
  s.b=[0]*128;p=f.split();s.t=(8,16)[p[1]=='b'];s.c=sum(1<<i for i,x in enumerate("KQkq") if x in p[2])
  s.e=-1 if p[3]=='-' else(8-int(p[3][1]))*16+ord(p[3][0])-97
  for i,l in enumerate(p[0].split('/')):
   c=0
   for x in l:
    if x.isdigit():c+=int(x)
    else:s.b[i*16+c]=(8 if x.isupper() else 16)|" pnbrqk".index(x.lower());c+=1
  s.kw=s.kb=-1
  for i in range(128):
   if s.b[i]==14:s.kw=i
   if s.b[i]==22:s.kb=i
 def A(s,q,l):
  for d in W[0]:
   j=q+d
   if not j&0x88 and s.b[j]==l|2:return 1
  for d in W[1]+W[2]:
   j=q+d
   if not j&0x88 and s.b[j]==l|6:return 1
  for d in[(15,17),(-15,-17)][l==16]:
   j=q+d
   if not j&0x88 and s.b[j]==l|1:return 1
  for d in W[1]+W[2]:
   j=q+d
   while not j&0x88:
    v=s.b[j]
    if v:
     if v&l and(v&7==5 or v&7==(3 if d in W[1] else 4)):return 1
     break
    j+=d
  return 0
 def M(s):
  r_=[]
  for i in range(128):
   if s.b[i]&s.t:
    p=s.b[i]&7
    if p==1:
     o=16-(s.t==8)*32;ts=[]
     if not(i+o)&0x88 and not s.b[i+o]:
      ts.append(i+o)
      if i>>4==6-(s.t==16)*5 and not s.b[i+2*o]:ts.append(i+2*o)
     for d in [o-1,o+1]:
      if not(i+d)&0x88 and((s.b[i+d] and not s.b[i+d]&s.t) or i+d==s.e):ts.append(i+d)
     for t in ts:
      for x in[5,4,3,2]if t>>4 in[0,7]else[0]:r_.append((i,t,x))
    else:
     for d in ((W[1] if p in [3,5,6] else [])+(W[2] if p in [4,5,6] else []) if p!=2 else W[0]):
      j=i+d
      while not j&0x88:
       if not s.b[j] or not s.b[j]&s.t:r_.append((i,j,0))
       if s.b[j] or p in [2,6]:break
       j+=d
     if p==6:
      for z,u in([(1,1),(2,-1)]if s.t==8 else[(4,1),(8,-1)]):
       if s.c&z and not s.b[i+u] and not s.b[i+2*u] and(u>0 or not s.b[i+3*u]) and not any(s.A(i+j*u,24^s.t) for j in range(3)):r_.append((i,i+2*u,0))
  return [m for m in r_ if not(n:=s.K(*m)).A((n.kw,n.kb)[s.t==16],24^s.t)]
 def K(s,f,t,x):
  n=B.__new__(B);n.b,n.t,n.c,n.e,n.kw,n.kb=s.b[:],s.t^24,s.c,-1,s.kw,s.kb
  p=s.b[f]
  if(p&7)==1:
   if t==s.e:n.b[t+(s.t==8)*32-16]=0
   if abs(f-t)==32:n.e=f+16-(s.t==8)*32
  n.b[t]=(s.t|x) if x else p;n.b[f]=0
  if p==14:n.kw=t
  if p==22:n.kb=t
  if(p&7)==6:
   if abs(f-t)==2:
    z=t+1 if t>f else t-2;n.b[z]=0;n.b[t-1 if t>f else t+1]=s.t|4
   n.c&=~(3 if s.t==8 else 12)
  for z,m in [(119,1),(112,2),(7,4),(0,8)]:
   if f==z or t==z:n.c&=~m
  return n
 def E(s):
  mg=eg=ph=0
  for i in range(128):
   if(v_:=s.b[i]):
    p=v_&7;c=v_&8;v=2*(c>0)-1;w=v*V[p];mg+=w;eg+=w;ph+=int(H[p])
    q=(i>>4)*4+min(i&7,7-(i&7))
    if not c:q^=28
    mg+=v*D[(p-1)*64+q];eg+=v*D[(p-1)*64+32+q]
  ph=min(ph,16)
  return(mg*ph+eg*(16-ph))//16*(-1,1)[s.t==8]
def U(m):
 f,t,x=m;s=chr(97+(f&7))+str(8-(f>>4))+chr(97+(t&7))+str(8-(t>>4))
 if x:s+="  nbrq"[x]
 return s
def S_(b,d,a,bt):
 if d<=0:
  s=b.E()
  if s>=bt:return bt
  if a<s:a=s
  ms=[m for m in b.M() if b.b[m[1]]]
 else:
  ms=b.M()
  if not ms:return-20000 if b.A((b.kw,b.kb)[b.t==16],24^b.t) else 0
 ms.sort(key=lambda m:-(b.b[m[1]]&7))
 for m in ms:
  s=-S_(b.K(*m),d-1,-bt,-a)
  if s>=bt:return bt
  if s>a:a=s
 return a
def C(fen,legal):
 b=B(fen);best=-30000;bm=legal[0];ms=b.M()
 ms.sort(key=lambda m:-(b.b[m[1]]&7))
 for m in ms:
  u=U(m)
  if u in legal:
   s=-S_(b.K(*m),2,-30000,-best)
   if s>best:best=s;bm=u
 return bm
if __name__=="__main__":
 while 1:
  g=T("/game",{})
  if not g or g.get("status")=="done":break
  while g.get("status")=="your_move":g=T("/move",{"game":g["game"],"move":C(g["fen"],g["legal_moves"])})
