import pytest
from oswald import model_manager as m

@pytest.mark.parametrize('tag',['../../secret','x;whoami','http://evil','','x y','a//b'])
def test_bad_tags(tag):
    with pytest.raises(ValueError): m.validate_tag(tag)

def test_valid_tag():
    assert m.validate_tag('library/model:Q4_K_M')=='library/model:Q4_K_M'

def test_nonlocal_rejected():
    with pytest.raises(ValueError): m._base({'ollama_url':'http://example.org:11434'})

def test_download_approval_required():
    with pytest.raises(ValueError): m.pull({'ollama_url':'http://127.0.0.1:11434'},'qwen3:4b','yes')

def test_activation_installed_only(monkeypatch):
    monkeypatch.setattr(m,'installed',lambda s:[{'name':'qwen3:4b'}])
    with pytest.raises(ValueError): m.activate({},'unknown:1b')
    assert m.activate({},'qwen3:4b')=='qwen3:4b'
