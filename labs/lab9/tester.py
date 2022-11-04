import MeanQueue as mq
import ArrayDeque as ad
import QueueStack as qs

def test_mean_queue():
    q = mq.MeanQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print("count: " + str(q.count))

    print("Mean: " + str(q.mean))
    print("Dequeue: " + str(q.dequeue()))
    print("Sum: " + str(q.sum()))

    try:
        q.enqueue("a")
    except TypeError:
        print("TypeError caught")

    try:
        q.dequeue()
        q.dequeue()
        q.dequeue()
        q.dequeue()
        q.dequeue()
        q.dequeue()
    except IndexError:
        print("IndexError caught")

def test_array_deque():
    d = ad.ArrayDeque()
    d.enqueue_first(1)
    d.enqueue_first(2)
    d.enqueue_first(3)
    d.enqueue_first(4)
    d.add_last(5)
    d.add_last(6)

    print("First: " + str(d.first()))
    print("Last: " + str(d.last()))

    print("Dequeue first: " + str(d.delete_first()))
    print("Dequeue last: " + str(d.delete_last()))

    print("First: " + str(d.first()))
    print("Last: " + str(d.last()))

    try:
        d.delete_first()
        d.delete_first()
        d.delete_first()
        d.delete_first()
        d.delete_first()
        d.delete_first()
        d.delete_first()
    except IndexError:
        print("IndexError caught")

def test_queue_stack():
    s = qs.QueueStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    print("Top: " + str(s.top()))
    print("Pop: " + str(s.pop()))
    print("Pop: " + str(s.pop()))
    print("Pop: " + str(s.pop()))
    print("Pop: " + str(s.pop()))
    print("Pop: " + str(s.pop()))
    
    try:
        s.pop()
    except IndexError:
        print("IndexError caught")


def main():
    # test_mean_queue()
    # test_array_deque()
    test_queue_stack()

if __name__ == "__main__":
    main()


    
