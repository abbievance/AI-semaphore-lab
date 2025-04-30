import pytest
from main import Buffer, Producer, Consumer
 
@pytest.fixture
def buffer():
    return Buffer(5)
 
def test_initial_state(buffer):
    assert buffer.size == 5
    assert len(buffer.items) == 5
    assert buffer.in_pointer == 0
    assert buffer.out_pointer == 0
 
def test_produce_consume(buffer):
    producer = Producer(buffer, 1)
    consumer = Consumer(buffer, 1)
 
    producer.produce(10)
    assert buffer.items[0] == 10
    assert buffer.in_pointer == 1
 
    item = consumer.consume()
    assert item == 10
    assert buffer.out_pointer == 1
 
def test_buffer_full(buffer):
    producer = Producer(buffer, 1)
    for i in range(buffer.size):
        producer.produce(i)
    assert buffer.in_pointer == 0
    assert buffer.items == [0, 1, 2, 3, 4]
 
def test_producer_produce(buffer):
    producer = Producer(buffer, 1)
    producer.produce(10)
    assert buffer.items[0] == 10
    assert buffer.in_pointer == 1
 
def test_consumer_consume(buffer):
    producer = Producer(buffer, 1)
    consumer = Consumer(buffer, 1)
    producer.produce(10)
    item = consumer.consume()
    assert item == 10
    assert buffer.out_pointer == 1
 
if __name__ == "__main__":
    pytest.main()