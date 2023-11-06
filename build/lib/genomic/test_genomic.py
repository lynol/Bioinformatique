from tools import tool
def test_is_identifiant():
    assert tool.is_identifiant(">test") == True
    assert tool.is_identifiant("test") == False