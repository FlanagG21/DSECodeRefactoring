import pytest
import pandas as pd
import bad_python as bp

data = bp.readData("/work/DSECodeRefactoring/data.csv")
def testBadPython():
    avg = bp.avg(data, data.columns[0])
    std = bp.standardDev(data, data.columns[0])
    assert  avg == 4.5
    assert std == pytest.approx(2.022599587, rel=0.01)
    
def testNone():
    data2 = None
    assert bp.avg(data2, "values") == None
    assert bp.standardDev(data2, "values") == None
    data3 = pd.DataFrame()
    assert bp.avg(data3, "values") == None
    assert bp.standardDev(data3, "values") == None
    
def testInvalidColumnAvg():
    with pytest.raises(IndexError):
        bp.avg(data, "blah")

def testInvalidDataAvg():
    with pytest.raises(TypeError):
        bp.avg(data, "colors")


def testInvalidColumnStd():
    with pytest.raises(IndexError):
        bp.standardDev(data, "blah")

def testInvalidDataStd():
    with pytest.raises(TypeError):
        bp.standardDev(data, "colors")
    
def testInvalidFilepath():
    data2 = bp.readData("invalidFilepath.csv")
    assert data2 == None