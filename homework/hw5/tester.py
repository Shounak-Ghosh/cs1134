from sg7569_hw5_q2 import MaxStack
from sg7569_hw5_q3 import MidStack
from sg7569_hw5_q4 import StackQueue


def test_max_stack():
    print("Testing MaxStack")
    max_stack = MaxStack()
    assert max_stack.is_empty()
    assert len(max_stack) == 0

    max_stack.push(3)
    assert not max_stack.is_empty()
    assert len(max_stack) == 1
    assert max_stack.top() == 3
    assert max_stack.max() == 3
    print("pushed:", max_stack.top())

    max_stack.push(1)
    assert len(max_stack) == 2
    assert max_stack.top() == 1
    assert max_stack.max() == 3
    print("pushed:", max_stack.top())

    max_stack.push(6)
    assert len(max_stack) == 3
    assert max_stack.top() == 6
    assert max_stack.max() == 6
    print("pushed:", max_stack.top())

    max_stack.push(4)
    assert len(max_stack) == 4
    assert max_stack.top() == 4
    assert max_stack.max() == 6
    print("pushed:", max_stack.top())

    print("max:", max_stack.max())

    print("popped:", max_stack.pop())
    assert len(max_stack) == 3
    assert max_stack.top() == 6
    assert max_stack.max() == 6

    print("popped:", max_stack.pop())
    assert len(max_stack) == 2
    assert max_stack.top() == 1
    assert max_stack.max() == 3

    print("max:", max_stack.max())


def test_mid_stack():
    print("Testing MidStack")
    ms = MidStack()
    assert ms.is_empty()
    assert len(ms) == 0

    print("test 1")

    ms.push(2)
    assert not ms.is_empty()
    assert len(ms) == 1
    assert ms.top() == 2
    print("pushed:", ms.top())

    ms.push(4)
    assert len(ms) == 2
    assert ms.top() == 4
    print("pushed:", ms.top())

    ms.push(6)
    assert len(ms) == 3
    assert ms.top() == 6
    print("pushed:", ms.top())

    ms.push(8)
    assert len(ms) == 4
    assert ms.top() == 8
    print("pushed:", ms.top())

    ms.mid_push(10)
    assert len(ms) == 5
    assert ms.top() == 8
    print("mid pushed:", 10)

    print("popped:", ms.pop())
    assert len(ms) == 4
    assert ms.top() == 6

    print("popped:", ms.pop())
    assert len(ms) == 3
    assert ms.top() == 10

    print("popped:", ms.pop())
    assert len(ms) == 2
    assert ms.top() == 4

    print("popped:", ms.pop())
    assert len(ms) == 1
    assert ms.top() == 2

    print("popped:", ms.pop())
    assert ms.is_empty()
    assert len(ms) == 0

    print("test 2")

    ms.push(2)
    ms.push(4)
    ms.push(6)
    ms.push(8)
    ms.push(10)

    ms.mid_push(12)
    assert len(ms) == 6
    assert ms.top() == 10
    print("mid pushed:", 12)

    print("popped:", ms.pop())
    assert len(ms) == 5
    assert ms.top() == 8

    print("popped:", ms.pop())
    assert len(ms) == 4
    assert ms.top() == 12

    print("popped:", ms.pop())
    assert len(ms) == 3
    assert ms.top() == 6

    print("popped:", ms.pop())
    assert len(ms) == 2
    assert ms.top() == 4

    print("popped:", ms.pop())
    assert len(ms) == 1
    assert ms.top() == 2

    print("popped:", ms.pop())
    assert ms.is_empty()
    assert len(ms) == 0


def test_stack_queue():
    print("Testing StackQueue")
    sq = StackQueue()
    assert sq.is_empty()
    assert len(sq) == 0

    sq.enqueue(1)
    assert not sq.is_empty()
    assert len(sq) == 1
    assert sq.first() == 1
    print("enqueued:", 1)

    sq.enqueue(2)
    assert len(sq) == 2
    assert sq.first() == 1
    print("enqueued:", 2)

    sq.enqueue(3)
    assert len(sq) == 3
    assert sq.first() == 1
    print("enqueued:", 3)

    print("dequeued:", sq.dequeue())
    assert len(sq) == 2
    assert sq.first() == 2

    sq.enqueue(4)
    assert len(sq) == 3
    assert sq.first() == 2
    print("enqueued:", 4)

    print("dequeued:", sq.dequeue())
    assert len(sq) == 2
    assert sq.first() == 3

    print("dequeued:", sq.dequeue())
    assert len(sq) == 1
    assert sq.first() == 4

    print("dequeued:", sq.dequeue())
    assert sq.is_empty()
    assert len(sq) == 0


def main():
    test_max_stack()
    print()
    test_mid_stack()
    print()
    test_stack_queue()


if __name__ == '__main__':
    main()
