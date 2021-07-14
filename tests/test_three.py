"""Test the Task data type"""

from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


def test_defaults():
    """Using no parameters should invoke defaults."""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2


def test_member_access():
    """Check .field functionality of namedtuple"""
    t = Task('buy milk', 'brain')
    assert t.summary == 'buy milk'
    assert t.owner == 'brain'
    assert (t.done, t.id) == (False, None)

"""you can use __new__.__defaults__ to create Task objects 
without having to specify all the fields. The test_defaults()
test is there to demonstrate and validate hoow the dedaults work.
The test_member_access() test is to demosntrate how to access
 members by name andnot by index, which is one of the mains
 reasons to use namedtuples"""