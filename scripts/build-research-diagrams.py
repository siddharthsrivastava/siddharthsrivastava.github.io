"""Build original conceptual illustrations, not paper figures or model outputs."""
from pathlib import Path
import math

OUT = Path(__file__).resolve().parents[1] / 'assets' / 'research'
OUT.mkdir(parents=True, exist_ok=True)
HEAD = '''<svg xmlns="http://www.w3.org/2000/svg" width="460" height="330" viewBox="0 0 460 330">
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0 10 5 0 10" fill="none" stroke="#7183a3" stroke-width="1.5"/></marker></defs>
<rect width="460" height="330" fill="#f0f4fa"/>
<style>text{font-family:Arial,sans-serif;fill:#344565;font-size:12px}.small{font-size:10px;fill:#536580}.label{font-size:11px;letter-spacing:1.2px;fill:#2446a8}</style>'''
def text(x,y,s,cls='',anchor='middle'):
    return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{s}</text>'
def line(x,y,u,v):
    return f'<path d="M{x} {y} L{u} {v}" fill="none" stroke="#7183a3" stroke-width="1.5" marker-end="url(#arrow)"/>'
def save(name,s):
    (OUT/name).write_text(HEAD+s+'</svg>\n')
# A deterministic, authored 3D chair point cloud. Orthographic projection.
s=text(30,30,'POINT CLOUD', 'label','start')
def dot(x,y,z):
    u=106+42*x-29*z; v=169-47*y+17*z+10*x
    return f'<circle cx="{u:.1f}" cy="{v:.1f}" r="1.75" fill="#2446a8" opacity="{.50+.35*(z+1)/2:.2f}"/>'
for i in range(11):
    for j in range(11):
        a,b=-1+i*.2,-1+j*.2
        s+=dot(a,0,b)
        s+=dot(a,1.6*(j/10),.95)
for x in [-.9,.9]:
    for z in [-.9,.9]:
        for i in range(9): s+=dot(x,-1.15*i/8,z)
s+=text(110,258,'Rich 3D representation','small')+line(190,145,230,145)
s+=text(293,83,'COMPACT TOKENS','label')
for i in range(4):
    for j in range(3):
        s+=f'<rect x="{246+25*i}" y="{108+25*j}" width="19" height="19" rx="3" fill="{["#2446a8","#5578c0","#9aafd5"][(i+j)%3]}"/>'
s+=text(291,205,'Distill useful structure','small')
s+='<path d="M293 220v18m-50 0h100m-100 0v15m50-15v15m50-15v15" stroke="#7183a3" fill="none"/>'
for x,label in [(238,'Classify'),(293,'Segment'),(350,'Transfer')]:
    s+=f'<rect x="{x-27}" y="258" width="54" height="26" rx="4" fill="#e2e9f5"/>'+text(x,275,label,'small')
save('foundry.svg',s)
# Preserve a deliberately drawn object while changing context.
s=text(30,30,'OBJECT IDENTITY, RETAINED','label','start')
s+='<rect x="26" y="58" width="178" height="200" rx="7" fill="#e1e8f3"/><rect x="254" y="58" width="178" height="200" rx="7" fill="#d7e7e4"/>'
s+='<path d="M26 212h178v39a7 7 0 0 1-7 7H33a7 7 0 0 1-7-7Z" fill="#ccd7e9"/><path d="M254 208h178v43a7 7 0 0 1-7 7H261a7 7 0 0 1-7-7Z" fill="#b4cec6"/>'
s+='<rect x="362" y="77" width="53" height="100" fill="#f9fcfa"/><path d="M388 77v100m-26-50h53" stroke="#d7e7e4" stroke-width="5"/><path d="M366 177 294 208h91l29-31" fill="#edf4dd" opacity=".8"/>'
for x in [115,343]:
    s+=f'<ellipse cx="{x+4}" cy="224" rx="39" ry="7" fill="#344565" opacity=".12"/><path d="M{x} 146v68" stroke="#334b7d" stroke-width="7"/><path d="M{x-29} 213q29-7 58 0v7h-58Z" fill="#334b7d"/><path d="M{x-23} 102h46l18 48h-82Z" fill="#6489c5"/><path d="M{x-23} 102h11l-9 48h-20Z" fill="#8faddb"/><ellipse cx="{x}" cy="150" rx="41" ry="4" fill="#3c6097"/>'
s+=line(215,159,242,159)+text(115,285,'Original object')+text(343,285,'New scene &amp; lighting')
save('preserve-anything.svg',s)
# Semantically labelled inputs and outputs.
s=text(30,30,'SHARING ACROSS MODALITIES','label','start')
for i,label in enumerate(['Image','Audio','Text','3D']):
    y=70+i*48
    s+=f'<rect x="25" y="{y}" width="87" height="32" rx="5" fill="#fff" stroke="#cdd8eb"/>'+text(69,y+21,label)
    s+=f'<path d="M112 {y+16}h22L170 161" fill="none" stroke="#9aaccb" stroke-width="1.2"/>'
s+='<rect x="170" y="104" width="130" height="112" rx="8" fill="#2446a8"/>'
s+='<text x="235" y="145" text-anchor="middle" style="fill:#fff;font-size:14px">Shared</text><text x="235" y="165" text-anchor="middle" style="fill:#fff;font-size:14px">representation</text>'
for i in range(6):
    s+=f'<rect x="{192+15*i}" y="184" width="10" height="10" rx="2" fill="#a9c1ee" opacity="{.4+.1*i}"/>'
for i,label in enumerate(['Recognize','Predict','Segment']):
    y=90+i*55
    s+=line(300,160,333,y+16)
    s+=f'<rect x="337" y="{y}" width="98" height="32" rx="5" fill="#e2e9f5"/>'+text(386,y+21,label)
s+=text(69,291,'Inputs','small')+text(235,291,'Learn together','small')+text(386,291,'Task heads','small')
save('omnivec.svg',s)
