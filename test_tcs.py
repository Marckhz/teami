from pydantic import ValidationError
import pytest
from tcs import DataCapture
from dto.data_capture_dto import DataCaptureDTO
from operations.stats_op import Stats


def test_data_caputure_attrs():
    capture = DataCapture()
    for id, (key, value) in enumerate(capture.collection.items()):
        assert value == 0
        assert key == id
    assert capture.count == 0


def test_data_capture():
    capture = DataCapture()
    for i in range(1000):
        capture.add(i)
        assert capture.collection[i] == 1
        assert capture.count == i + 1

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

@pytest.mark.parametrize('x, output',[
    (4, 6),
    (1,2),
    (15, 9),
    ])
def test_lessers(stats, x, output):
    st = stats.less(x)
    assert st  == output


@pytest.mark.parametrize('x, output', [
    (4, 2),
    (15,0),
    (17,0),
    (1, 6),
    (0, 7)
])
def test_greater(stats, x, output):
    st = stats.greater(x)
    assert st == output


@pytest.mark.parametrize('x, y, output', [
    (4, 6, 2),
    (0, 1, 3),
    (11,12, 0),
])
def test_between(stats, x,y, output):
    st = stats.between(x,y)
    assert st == output


@pytest.mark.parametrize('x, y, output', [
    (10, 2, "start can't be greater than end"),
    (-1, 2, "wrong index" )
    ])
def test_greater_raises_value_error(stats, x, y, output):
    with pytest.raises(ValueError) as err:
        stats.between(x,y)
    assert err.value.args[0] == output

@pytest.mark.parametrize('x', [(1), ('1'), (1.5)])
def test_data_caputure_dto(x):
   dto = DataCaptureDTO()
   dto.value = x
   assert dto.value == 1



def test_data_capture_error():
    capture = DataCapture()
    with pytest.raises(ValidationError) as e:
        capture.add(-1)



def test_data_capture_return():
    capture = DataCapture()
    stats = capture.build_stats()
    assert type(stats) == Stats

@pytest.mark.parametrize('x, y', [(1,2),
                                  (10, 15),
                                  (100, 1500)])
def test_stats_methods(stats, x, y):
    assert stats.collection != {}
    assert stats.total > 0
    assert type(stats.less(x)) == int
    assert type(stats.between(x, y)) == int
    assert type(stats.greater(x)) == int


@pytest.mark.parametrize('x, y', [(1001, 2000),
                                  (5000, 9000),
                                  (8000, 9000)])
def test_retrieve_value_outside_max(stats, x, y):
    assert stats.less(x) == 0
    assert stats.greater(x) == 0
    assert stats.between(x, y) == 0