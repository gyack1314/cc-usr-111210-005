"""清点PIT查询、切片配置与原响应数。"""
from .io import integer

def summarize(v,root):
    integer(v['slices'],1);integer(v['global_total'])
    if not v['sort'] or v['sort'][-1]!='tie_breaker':raise ValueError('排序缺唯一尾列')
    if v['query']['term'].get('status')!='sale':raise ValueError('资料查询范围不符')
    return {'slices':v['slices'],'global_total':v['global_total'],'recorded_calls':len(v['steps']),'sort':v['sort']}
