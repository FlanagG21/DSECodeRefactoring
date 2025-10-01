import pytest
import pandas as pd
import bad_python as bp

data = bp.readData("/work/DSECodeRefactoring/data.csv")
def testBadPython():
    """tests avg and standardDev
    """
    avg = bp.avg(data, data.columns[0])
    std = bp.standardDev(data, data.columns[0])
    assert  avg == 4.5
    assert std == pytest.approx(2.022599587, rel=0.01)
    
def testNone():
    """tests avg and standardDev
    """
    data2 = None
    assert bp.avg(data2, "values") == None
    assert bp.standardDev(data2, "values") == None
    data3 = pd.DataFrame()
    assert bp.avg(data3, "values") == None
    assert bp.standardDev(data3, "values") == None
    
def testInvalidColumnAvg():
    """tests avg and standardDev
    """
    with pytest.raises(IndexError):
        bp.avg(data, "blah")

def testInvalidDataAvg():
    """tests avg and standardDev
    """
    with pytest.raises(TypeError):
        bp.avg(data, "colors")


def testInvalidColumnStd():
    """tests avg and standardDev
    """
    with pytest.raises(IndexError):
        bp.standardDev(data, "blah")

def testInvalidDataStd():
    """tests avg and standardDev
    """
    with pytest.raises(TypeError):
        bp.standardDev(data, "colors")

def testInvalidDataRandom():
    """tests print5Random
    """
    with pytest.raises(ValueError):
        bp.print5Random(None)
        
def testInvalidDataRandom2():
    """tests print5Random
    """
    data2 = pd.DataFrame()
    with pytest.raises(ValueError):
        bp.print5Random(data2)
        
def testInvalidDataPlot():
    """tests plotVals
    """
    with pytest.raises(ValueError):
        bp.plotVals(None, "values")
        
def testInvalidDataPlot2():
    """tests plotVals
    """
    data2 = pd.DataFrame()
    with pytest.raises(ValueError):
        bp.plotVals(data2, "values")
        
def testInvalidDataPlot():
    """tests plotVals
    """
    with pytest.raises(IndexError):
        bp.plotVals(data, "blah")
    
def testInvalidFilepath():
    """tests readData
    """
    data2 = bp.readData("invalidFilepath.csv")
    assert data2 == None
    
