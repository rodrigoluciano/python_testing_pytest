"""Test the Task data type"""

from collections import namedtuple

Task = namedtuple('Task', ['sumary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


def test_asdict():
    """asdict() should return a dictionary"""

    t_tast = Task('do something', 'okken', True, 21)
    t_dict = t_tast._asdict()
    expected = {'sumary': 'do something',
                'owner': 'okken',
                'done': True,
                'id': 21}
    assert t_dict == expected


def test_replace():
    """replace() should change passed in fields"""
    t_before = Task('finish book', 'brian', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'brian', True, 10)
    assert t_after == t_expected
