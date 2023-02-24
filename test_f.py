from funciones import minValor

def test_minValor():
    assert minValor([1,2,3,4,5,6]) == 1
    assert minValor([0,3,1,5,9,4]) == 0
    assert minValor([-2,3,2,1,0,5]) == -2
    assert minValor([1,6,7,3,2,9]) == 1
    assert minValor([2,4,6,8,10,3]) == 2
    assert minValor([-4,0,1,2,4,3]) == -4
    
