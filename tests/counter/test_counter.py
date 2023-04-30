from src.pre_built.counter import count_ocurrences
from unittest.mock import mock_open, patch

fake_text = 'Lorem ipsum dolor sit amet consectetur adipisicing elit'


def test_counter():
    with patch('builtins.open', mock_open(read_data=fake_text)):
        data = count_ocurrences('test', 'lorem')
        assert data == 1
