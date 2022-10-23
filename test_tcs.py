import pytest
from tcs import DataCapture
from operations.stats_op import Stats


def tests_data_capture_add():
    capture = DataCapture()
    capture.add(4)
    assert capture.collection == {4:'4'}
    capture.add(4)
    assert capture.collection == {4:'44'}


@pytest.fixture
def stats():
    capture = DataCapture()
    capture.add(3)
    capture.add(0)
    capture.add(9)
    capture.add(3)
    capture.add(6)
    capture.add(4)
    capture.add(2)
    capture.add(1)
    capture.add(0)
    stats = capture.build_stats()
    return stats


@pytest.mark.parametrize('x, target', [
    (4, ['00','1','2','33']),
    (11, ['00', '1','2', '33', '4', '6', '9'])
    ])
def test_lessers(stats, x, target):
    st = stats.less(x)
    assert st  == target


@pytest.mark.parametrize('x,target', [
    (4, ['6','9']),
    (11, [])
])
def test_greater(stats, x, target):
    st = stats.greater(x)
    assert st == target


@pytest.mark.parametrize('x, y, target', [
    (4,9,['6']),
    (9,9 ,[])
])
def test_between(stats, x,y, target):
    st = stats.between(x,y)
    assert st == target


def test_greater_raises_value_error(stats):
    with pytest.raises(ValueError) as err:
        stats.between(100,10)
    assert err.value.args[0] == "start can't be greater than end"


def test_empty_collection_data_capture():
    capture = DataCapture()
    st = capture.build_stats()
    assert st.greater(1) == []
    assert st.less(1) == []
    assert st.between(1,0)  == []


def test_stats():
    st = Stats(collection = {}, max_value=10)
    assert st.collection == {}
    assert st.max_value == 10


