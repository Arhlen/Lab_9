from main import get_pass_count
def test_true():
    lines = ['0,1,1,2,3,4,5,age']
    assert get_pass_count(lines) == ()