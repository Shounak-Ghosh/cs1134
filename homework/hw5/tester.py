from sg7569_hw5_q2 import MaxStack
from sg7569_hw5_q3 import MidStack
from sg7569_hw5_q4 import StackQueue


def test_max_stack():
    max_stack = MaxStack()
    assert max_stack.is_empty()
    assert len(max_stack) == 0
    
    max_stack.push(3)
    assert not max_stack.is_empty()
    assert len(max_stack) == 1
    assert max_stack.top() == 3
    assert max_stack.max() == 3
    
    max_stack.push(1)
    assert len(max_stack) == 2
    assert max_stack.top() == 1
    assert max_stack.max() == 3
    
    max_stack.push(6)
    assert len(max_stack) == 3
    assert max_stack.top() == 6
    assert max_stack.max() == 6
    
    max_stack.push(4)
    assert len(max_stack) == 4
    assert max_stack.top() == 4
    assert max_stack.max() == 6

    print(max_stack.max())

    print(max_stack.pop())
    assert len(max_stack) == 3
    assert max_stack.top() == 6
    assert max_stack.max() == 6

    print(max_stack.pop())
    assert len(max_stack) == 2
    assert max_stack.top() == 1
    assert max_stack.max() == 3

    print(max_stack.max())

def test_mid_stack():
    pass

def test_stack_queue():
    pass


def main():
    test_max_stack()

if __name__ == '__main__':
    main()

