import lab2

def test_find_min_max():
    result=[]
    input_arr=[2,34,32,1]
    test_arr=[1,34]
    result=lab2.find_min_max(input_arr)
    assert(result==test_arr)

    
def test_calc_average():
    result=[]
    input_arr=[32,12,4,6]
    test_arr=13.5
    result=lab2.calc_average(input_arr)
    assert(result==test_arr)

def test_calc_median_temperature():
    result=[]
    input_arr=[32,12,4,6]
    test_arr=9.0
    result=lab2.calc_median_temperature(input_arr)
    assert(result==test_arr)
