import itertools
import sys
import numpy as np

def find_quadrilateral(polygon):
    
    if type(polygon)!=list:
        try:
            list(polygon)
        except:
            sys.exit('Please give valid polygon')
    
    x=[i[0] for i in polygon]
    y=[i[1] for i in polygon]
    
    assert len(x)==len(y)

    m_area=area(x,y)
    areas={}

    for i in itertools.combinations(polygon,4):
        x=[j[0] for j in i]
        y=[j[1] for j in i]
    
        areas[i]=area(x,y)
    
    diffs={k:np.abs(m_area-areas[k]) for k in areas.keys()}

    minn=min(diffs.values())

    html='<svg width="800" height="500"> <polyline points="$ " fill="green" style="stroke:black;stroke-width:0"></polyline><polygon points="% " fill="none" style="stroke:black;stroke-width:3"></polygon></svg>'

    str_pol=' '.join([','.join([str(j) for j in i]) for i in polygon ])

    for k,v in diffs.items():
        if v==minn:
            p= ' '.join([','.join([str(i) for i in j]) for j in k])
            html=html.replace('$', str_pol)
            html=html.replace('%', p)
    
    with open("result.html", "w") as file:
        file.write(html)
        
    return(html)
