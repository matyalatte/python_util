import pytest
from matyautil.dataset_util import split_datalist

data_lists=(
    [list(range(20)),16,4],[list(range(19)),15,4]
    )

@pytest.fixture(params=data_lists)
def split_task(request):
    return request.param

def test_split_datalist(split_task):
    splitted = split_datalist(split_task[0])
    assert len(splitted["train_list"])==split_task[1]
    assert len(splitted["test_list"])==split_task[2]