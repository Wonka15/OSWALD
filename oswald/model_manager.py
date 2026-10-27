"""OSWALD 2.1 local-only Ollama model manager."""
import re
import time
from urllib.parse import urlparse
import requests

TAG = re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9._/-]{0,119}(?::[a-zA-Z0-9][a-zA-Z0-9._-]{0,79})?$')

def validate_tag(tag):
    if not isinstance(tag, str) or not TAG.fullmatch(tag) or '..' in tag or '//' in tag:
        raise ValueError('Invalid Ollama model tag')
    return tag

def _base(settings):
    p = urlparse(settings['ollama_url'])
    if p.scheme != 'http' or p.hostname not in ('localhost','127.0.0.1') or p.port != 11434 or p.username or p.password or p.path not in ('','/') or p.query or p.fragment:
        raise ValueError('Only local Ollama at port 11434 is permitted')
    return settings['ollama_url'].rstrip('/')

def _session():
    s = requests.Session()
    s.trust_env = False
    return s

def installed(settings):
    with _session() as s:
        r=s.get(_base(settings)+'/api/tags',timeout=5,allow_redirects=False)
        r.raise_for_status()
        return [{'name':m.get('name'),'size_bytes':m.get('size',0)} for m in r.json().get('models',[]) if isinstance(m,dict)]

def activate(settings,tag):
    tag=validate_tag(tag)
    if tag not in {m['name'] for m in installed(settings)}:
        raise ValueError('Model must be installed before activation')
    return tag

def benchmark(settings,tag,prompt='Reply with one short sentence about a friendly robot.'):
    tag=activate(settings,tag)
    start=time.perf_counter()
    with _session() as s:
        r=s.post(_base(settings)+'/api/generate',json={'model':tag,'prompt':prompt[:300],'stream':False,'keep_alive':0,'options':{'num_predict':96,'num_ctx':2048,'temperature':0}},timeout=180,allow_redirects=False)
        r.raise_for_status()
        result=r.json()
    elapsed=time.perf_counter()-start
    count=int(result.get('eval_count') or 0)
    duration=int(result.get('eval_duration') or 0)
    return {'model':tag,'wall_seconds':round(elapsed,2),'tokens_per_second':round(count*1e9/duration,2) if duration>0 else None,'generated_tokens':count,'note':'Single-prompt local benchmark, not VRAM or safety certification.'}

def pull(settings,tag,approval):
    tag=validate_tag(tag)
    if approval != 'DOWNLOAD '+tag:
        raise ValueError('Explicit download confirmation required')
    with _session() as s:
        r=s.post(_base(settings)+'/api/pull',json={'model':tag,'stream':False},timeout=1800,allow_redirects=False)
        r.raise_for_status()
        return {'model':tag,'status':r.json().get('status','completed')}
